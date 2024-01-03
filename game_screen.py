import pygame
from colors import *
from widgets import *
from sql_manager import Database
from tkinter import messagebox


def load_level(lvl, db, screen, menu, main_obj):
    lvl_id, summand_1, summand_2, result, passed = db.query('SELECT * FROM levels WHERE id = {}'.format(lvl))[0]
    main_obj.buttons.clear()
    main_obj.levels.clear()
    game = Game(
        screen,
        lvl_id,
        db.get_element(summand_1),
        db.get_element(summand_2),
        db.get_element(result),
        menu,
        main_obj
    )


def show_level(*args):
    lvl, screen, menu, main_obj = args[0]
    db = Database()
    if lvl in db.get_levels():
        load_level(lvl, db, screen, menu, main_obj)
    else:
        messagebox.showerror("Ошибка", "Уровень еще не создан или не найден.")
    del db

class GameScreen:
    def __init__(self, screen: pygame.Surface, menu) -> None:
        self.menu = menu
        self.clock = pygame.time.Clock()
        self.width, self.height = screen.get_size()
        self.screen = screen
        screen.fill(VERY_DARK_BG)
        
        self.background = PygameImage(screen, 'background.png', image_size=self.width * 2, opacity=50)
        self.title = PygameText(screen, text="Выберите уровень", coordinates=(self.width // 2, 30))
        
        self.buttons = list()
        self.buttons.append(PygameButton(
            screen=screen,
            text='Назад',
            background_color=LIGHT_BLUE,
            border_color=DARK_BG,
            text_color=LIGHT,
            font_size=14,
            border_size=1,
            coordinates=(50, 30, 80, 30)
        ))
        self.buttons[0].on_clicked = self.on_back_clicked
    
        self.levels = list()
        for i in range(1, max(Database().get_levels()) + 1):
            side = 60
            x = (i * (side + self.width // side)) % self.width
            y = (i * (side + self.width // side)) // self.width
            
            passed = Database().query("SELECT passed FROM levels WHERE id = {}".format(i))
            if passed:
                passed = bool(passed[0][0])
            color = BLUE if not passed else GREEN
            
            self.levels.append(PygameButton(
                screen=screen,
                text=f"{i}",
                background_color=DARK_BG,
                border_color=color,
                border_size=1,
                border_radius=8,
                text_color=LIGHT,
                coordinates=(
                    x if x else side + self.width // side,   
                    side * 1.5 + y * (side + self.width // side),  
                    side, side)
            ))
            
            self.levels[i - 1].on_clicked = show_level
            self.levels[i - 1].args = (i, screen, menu, self)
    
    
    def on_back_clicked(self):
        self.menu.InitUI()
        self.buttons.clear()
        

class Game:
    def __init__(self, screen: pygame.Surface, lvl, summand_1, summand_2, result, menu, main_obj) -> None:
        self.screen = screen
        self.lvl = lvl
        self.summand_1 = summand_1
        self.summand_2 = summand_2
        self.result = result
        self.menu = menu
        self.width, self.height = screen.get_size()
        self.main_obj = main_obj
        self.screen.fill(VERY_DARK_BG)
        main_obj.buttons = list()
        main_obj.buttons.append(PygameButton(
            screen=screen,
            text='В главное меню',
            background_color=RED,
            border_color=DARK_BG,
            text_color=LIGHT,
            font_size=14,
            border_size=1,
            coordinates=(80, 30, 130, 30)
        ))
        main_obj.buttons[0].on_clicked = main_obj.on_back_clicked
        
        self.title = PygameText(self.screen, text=f"Ваша задача: Получить {result[1]}", coordinates=(self.width // 2, 30), font_size=22, text_color=LIGHT)
        self.divider = PygameLine(self.screen, (self.width // 2 - 150, 45), (self.width // 2 + 150, 45), GREY, 1)
        
        self.right_tube = PygameTube(self.screen, 'tube.png', image_size=256, coordinates=(self.width - 128, self.height // 2))
        self.left_tube = PygameTube(self.screen, 'tube.png', image_size=256, coordinates=(128, self.height // 2))
        self.right_tube.checker, self.left_tube.checker = self.check_for_victory, self.check_for_victory
        main_obj.buttons.append(self.left_tube)
        main_obj.buttons.append(self.right_tube)
    
    def check_for_victory(self):
        if any([
            self.left_tube.element == self.summand_1[1] and self.right_tube.element == self.summand_2[1],
            self.left_tube.element == self.summand_2[1] and self.right_tube.element == self.summand_1[1]
        ]):
            self.right_tube.clickable = False
            self.left_tube.clickable = False
            self.victory_message = PygameText(self.screen, text=f"Вы выйграли!", coordinates=(self.width // 2, self.height // 2))
            for button in self.main_obj.buttons:
                button.checker = lambda: ...

            Database().query('UPDATE levels SET passed = 1 WHERE id = {}'.format(self.lvl))
                