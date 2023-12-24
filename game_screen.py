import pygame
from colors import *
import time
from widgets import *


class GameScreen:
    def __init__(self, screen: pygame.Surface, menu) -> None:
        self.menu = menu
        self.clock = pygame.time.Clock()
        self.width, self.height = screen.get_size()
        self.screen = screen
        screen.fill(VERY_DARK_BG)
        
        self.buttons = list()
        self.buttons.append(PygameButton(
            screen=screen,
            text='Назад',
            background_color=LIGHT_BLUE,
            border_color=LIGHT_BLUE,
            text_color=LIGHT,
            font_size=14,
            coordinates=(50, 30, 80, 30)
        ))
        self.buttons[0].on_clicked = self.on_back_clicked
    
        self.img = PygameImage(self.screen, '404.png', (self.width // 2, self.height // 2), image_size=256)
        self.description = PygameText(self.screen, text="Упс... Тут еще ничего нет", text_color=LIGHT, coordinates=(self.width // 2, self.height - 40), font_size=24)
    
    def on_back_clicked(self):
        self.menu.InitUI()
        self.buttons.clear()