import pygame
import os
from colors import *
from widgets import *


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("The world of chemistry: Great Invention")
    
    programIcon = pygame.image.load(f'{os.getcwd()}/assets/chemistry.png')
    pygame.display.set_icon(programIcon)
    
    size = width, height = 720, 500
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(VERY_DARK_BG)
        hz = Text(screen, text="Here is the name of the game...", coordinates=(width // 2, height // 2))
        new = Text(screen, text="Why am I doing it???", coordinates=(width // 2, height // 2 + 22), font_size=12, text_color=GREY)
        pygame.display.flip()

