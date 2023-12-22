import pygame
from colors import *
import os


class Text:
    def __init__(
        self,
        screen,
        font_name: str = f"{os.getcwd()}/fonts/NunitoSans.ttf",
        font_size: int = 22,
        text: str = "Default text",
        text_color: tuple | list | str = LIGHT,
        coordinates: tuple = (0, 0)
):
        self.screen, self.font_name, self.font_size, self.text, self.text_color, self.coordinates = screen, font_name, text,  font_size, text_color, coordinates
        self.font = pygame.font.Font(font_name, font_size)
        self.text = self.font.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center=coordinates)
        self.update()
    
    def change_font(self, font):
        self.font = pygame.font.Font(font, self.font_size)
    
    def update(self):
        self.screen.blit(self.text, self.text_rect)
        

