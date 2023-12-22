import pygame
from colors import *
import os


class PygameText:
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
        

class PygameButton:
    def __init__(
            self,
            screen,
            text="Default",
            background_color=LIGHT,
            coordinates=(0, 0),
            border_color=GREY,
            text_color=VERY_DARK_BG,
            font_size=24,
            border_radius=3,
            border_size=3,
            on_clicked=None
        ):
        if not on_clicked:
            on_clicked = self.on_clicked
        self.border_radius = border_radius
        self.border_size = border_size
        self.on_clicked = on_clicked
        self.text_color = text_color
        self.border_color = border_color
        self.coordinates = coordinates
        self.screen = screen
        self.text = text
        self.font_size = font_size
        self.background_color = background_color
        self.update()
    
    def pressed(self, mouse_position):
        if all([
            mouse_position[0] >= self.coordinates[0] - self.coordinates[2] // 2,
            mouse_position[0] <= self.coordinates[0] + self.coordinates[2] // 2,
            mouse_position[1] >= self.coordinates[1] - self.coordinates[3] // 2,
            mouse_position[1] <= self.coordinates[1] + self.coordinates[3] // 2
        ]):
            self.on_clicked()
    
    def on_clicked(self):
        print('CLICKED')
    
    def update(self):
        coord = list(self.coordinates)
        coord[0] -= coord[2] // 2
        coord[1] -= coord[3] // 2
        pygame.draw.rect(
            self.screen, 
            self.background_color, 
            pygame.Rect(coord), 25, self.border_radius
        )
        pygame.draw.rect(
            self.screen, 
            self.border_color,
            pygame.Rect(coord), self.border_size, self.border_radius
        )
        self.update_label()
    
    def update_label(self):
        try:
            del self.label
        except:
            ...
        coord = list(self.coordinates[:2])
        self.label = PygameText(
            self.screen, 
            text=self.text, 
            coordinates=coord, 
            text_color=self.text_color,
            font_size=self.font_size
        )
        
        del coord


class PygameImage:
    def __init__(
        self,
        screen,
        name="chemistry.png",
        coordinates=(0, 0),
        image_size=64
    ) -> None:
        fullname = os.path.join('assets', name)
        if not os.path.isfile(fullname):
            return
        self.screen = screen
        self.image_size = image_size
        self.coordinates = coordinates
        self.image = pygame.transform.scale(pygame.image.load(fullname), (image_size, image_size))
        self.update()
        
    def update(self):
        self.screen.blit(self.image, [int(i) - self.image_size // 2 for i in self.coordinates])