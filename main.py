import pygame
import os
from colors import *
from widgets import *


def show_periodic_table():
    print('TABLE')


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("The world of chemistry: Great Invention")
    
    programIcon = pygame.image.load(f'{os.getcwd()}/assets/chemistry.png')
    pygame.display.set_icon(programIcon)
    
    size = width, height = 720, 500
    screen = pygame.display.set_mode(size)
    running = True
    
    screen.fill(VERY_DARK_BG)
    hz = Text(screen, text="Here is the name of the game...", coordinates=(width // 2, height // 2))
    new = Text(screen, text="Why am I doing it???", coordinates=(width // 2, height // 2 + 22), font_size=12, text_color=GREY)
    
    buttons = list()
    buttons.append(Button(
        screen, text="Start", coordinates=(width - 100, height - 65, 100, 50),
        border_color=GREY,
        border_radius=10,
        border_size=4
    ))
    buttons.append(Button(
        screen, text="Таблица Менделеева", coordinates=(115, 45, 200, 50),
        border_color=GREY,
        border_radius=10,
        border_size=4,
        font_size=16
    ))
    buttons[1].on_clicked = show_periodic_table
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.pressed(event.pos)
        
        pygame.display.flip()

