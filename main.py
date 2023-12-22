import pygame
import os
from colors import *
from widgets import *
from PIL import Image 


def show_periodic_table():
    image = Image.open(os.path.join(os.getcwd(), 'assets', 'periodic-table.png'))
    image.show()
    

def show_solubility_table():
    image = Image.open(os.path.join(os.getcwd(), 'assets', 'solubility-table.png'))
    image.show()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("The world of chemistry: Great Invention")
    
    programIcon = pygame.image.load(f'{os.getcwd()}/assets/chemistry.png')
    pygame.display.set_icon(programIcon)
    
    size = width, height = 720, 500
    screen = pygame.display.set_mode(size)
    running = True
    
    screen.fill(VERY_DARK_BG)
    hz = PygameText(screen, text="Приветствуем тебя, странник!", coordinates=(width // 2, height - 100))
    new = PygameText(screen, text="Ты находишься на главном окне. Здесь можно начать игру или посмотреть справочную информацию", coordinates=(width // 2, height - 100 + 22), font_size=12, text_color=GREY)
    
    buttons = list()
    buttons.append(PygameButton(
        screen, text="Начать", coordinates=(width - 60, height - 35, 100, 50),
        border_color=LIGHT,
        background_color=DARK_BG,
        text_color=LIGHT,
        border_radius=10,
        border_size=2,
        font_size=18
    ))
    
    buttons.append(PygameButton(
        screen, text="Таблица Менделеева", coordinates=(115, 45, 200, 50),
        text_color=LIGHT,
        border_color=DARK_BG,
        border_radius=12,
        border_size=5,
        font_size=16,
        background_color=BLUE
    ))
    buttons[1].on_clicked = show_periodic_table
    
    buttons.append(PygameButton(
        screen, text="Таблица растворимости", coordinates=(width - 115, 45, 200, 50),
        text_color=LIGHT,
        border_color=DARK_BG,
        border_radius=12,
        border_size=5,
        font_size=16,
        background_color=BLUE
    ))
    buttons[2].on_clicked = show_solubility_table
    
    main_image = PygameImage(
        screen,
        'chemistrylogo.png',
        (width // 2, height // 2),
        image_size=160
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.pressed(event.pos)
        
        pygame.display.flip()

