import pygame
import os
from colors import *


def create_label(
    font_name: str = f"{os.getcwd()}/fonts/NunitoSans.ttf",
    font_size: int = 22,
    text: str = "Default text",
    text_color: tuple | list | str = LIGHT,
    coordinates: tuple = (0, 0)
):
    """
    :font_name: Name of the font
    :font_size: Size of the font
    :text: Text
    :text_color: Color of the text
    :coordinates: Center coordinates
    
    create_label creates a new text on screen
    """
    font = pygame.font.Font(font_name, font_size)
    text = font.render(text, True, text_color)
    text_rect = text.get_rect(center=coordinates)
    screen.blit(text, text_rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 720, 500
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(VERY_DARK_BG)
        create_label(text="Here is the name of the game...", coordinates=(width // 2, height // 2))
        create_label(text="Why am I doing it???", coordinates=(width // 2, height // 2 + 22), font_size=12, text_color=GREY)
        pygame.display.flip()

