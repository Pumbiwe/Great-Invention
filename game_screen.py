import pygame
from colors import *
import time
from widgets import *

def show_level(lvl):
    print(f"Level {lvl}")

class GameScreen:
    def __init__(self, screen: pygame.Surface, menu) -> None:
        self.menu = menu
        self.clock = pygame.time.Clock()
        self.width, self.height = screen.get_size()
        self.screen = screen
        screen.fill(VERY_DARK_BG)
        
        self.background = PygameImage(screen, 'background.png', image_size=self.width * 2, opacity=50)
        self.title = PygameText(screen, text="Choose a level", coordinates=(self.width // 2, 30))
        
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
        for i in range(1, 10):
            side = 60
            x = (i * (side + self.width // side)) % self.width
            y = (i * (side + self.width // side)) // self.width
            self.levels.append(PygameButton(
                screen=screen,
                text=f"{i}",
                background_color=DARK_BG,
                border_color=BLUE,
                border_size=1,
                border_radius=8,
                text_color=LIGHT,
                coordinates=(
                    x if x else side + self.width // side,   
                    side * 1.5 + y * (side + self.width // side),  
                    side, side)
            ))
            
            # FIXME: Как работает эта хрень? Если передать i в show_level, передастся последняя i
            if i == 1:
                call = lambda: show_level(0)
            elif i == 2:
                call = lambda: show_level(1)
            else:
                call = lambda: show_level(i - 1)
            self.levels[i - 1].on_clicked = call
            del call
    
    
    def on_back_clicked(self):
        self.menu.InitUI()
        self.buttons.clear()