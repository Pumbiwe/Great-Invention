import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from colors import *
from widgets import *
from PIL import Image 
from game_screen import GameScreen


def show_periodic_table():
    image = Image.open(os.path.join(os.getcwd(), 'assets', 'periodic-table.png'))
    image.show()
    

def show_solubility_table():
    image = Image.open(os.path.join(os.getcwd(), 'assets', 'solubility-table.png'))
    image.show()


def start_game():
    global game
    game = GameScreen(screen, menu)
    menu.buttons.clear()
    for sprite in menu.sprites:
        sprite.kill()
    del menu.main_image


class MainMenu:
    def __init__(self, screen: pygame.Surface, sprites) -> None:
        self.screen = screen
        self.sprites = sprites
        self.InitUI()
    
    def InitUI(self):
        self.screen.fill(VERY_DARK_BG)
        self.greeting = PygameText(self.screen, text="Приветствуем тебя, странник!", coordinates=(width // 2, height - 100))
        self.description = PygameText(self.screen, text="Ты находишься на главном окне. Здесь можно начать игру или посмотреть справочную информацию", coordinates=(width // 2, height - 100 + 22), font_size=12, text_color=GREY)
        
        self.buttons = list()
        self.buttons.append(PygameButton(
            self.screen, text="Начать", coordinates=(width - 60, height - 35, 100, 50),
            border_color=DARK_BG,
            background_color=DARK_BG,
            text_color=LIGHT,
            border_radius=10,
            border_size=2,
            font_size=18
        ))
        self.buttons[0].on_clicked = start_game
        
        self.buttons.append(PygameButton(
            self.screen, text="Таблица Менделеева", coordinates=(115, 45, 200, 50),
            text_color=LIGHT,
            border_color=DARK_BG,
            border_radius=12,
            border_size=5,
            font_size=16,
            background_color=BLUE
        ))
        self.buttons[1].on_clicked = show_periodic_table
        
        self.buttons.append(PygameButton(
            self.screen, text="Таблица растворимости", coordinates=(width - 115, 45, 200, 50),
            text_color=LIGHT,
            border_color=DARK_BG,
            border_radius=12,
            border_size=5,
            font_size=16,
            background_color=BLUE
        ))
        self.buttons[2].on_clicked = show_solubility_table
        
        self.main_image = PygameImage(
            self.screen,
            'chemistrylogo.png',
            (width // 2, height // 2),
            image_size=160,
            movable=(True, False),
            sprites=self.sprites
        )
    


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("The world of chemistry: Great Invention")
    
    programIcon = pygame.image.load(f'{os.getcwd()}/assets/chemistry.png')
    pygame.display.set_icon(programIcon)
    
    size = width, height = 720, 500
    screen = pygame.display.set_mode(size)
    
    sprites = pygame.sprite.Group()
    running = True
    
    screen.fill(VERY_DARK_BG)
    menu = MainMenu(screen, sprites)
    
    while running:
        try:
            for tube in game.buttons:
                if type(tube) is PygameTube:
                    tube.checker()
        except:
            ...
        
        btn_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    try:
                        menu.main_image.on_mouse(pygame.mouse.get_pos())
                    except AttributeError:
                        ...
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for button in menu.buttons:
                    button.pressed(event.pos)
                try:
                    for button in game.buttons:
                        button.pressed(event.pos)
                    for lvl in game.levels:
                        lvl.pressed(event.pos)
                except Exception as e:
                    ...
        
        pygame.display.flip()

pygame.quit()