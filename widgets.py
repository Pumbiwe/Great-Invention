import pygame
from colors import *
import os
import tkinter as tk
from tkinter import ttk

from sql_manager import Database


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
            coordinates: tuple[int, int, int, int]=(100, 100, 100, 50),
            border_color=GREY,
            text_color=VERY_DARK_BG,
            font_size=24,
            border_radius=3,
            border_size=3,
            on_clicked=None
        ):
        if not on_clicked:
            on_clicked = self.on_click
        self.args = None
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
            if self.args:
                self.on_clicked(self.args)
            else:
                self.on_clicked()

    def on_click(self):
        print('CLICKED')
    
    def update(self):
        coord = list(self.coordinates)
        coord[0] -= coord[2] // 2
        coord[1] -= coord[3] // 2
        pygame.draw.rect(
            self.screen, 
            self.background_color, 
            pygame.Rect(coord), 
            border_radius=self.border_radius
        )
        pygame.draw.rect(
            self.screen, 
            self.border_color,
            pygame.Rect(coord), 
            self.border_size, 
            border_radius=self.border_radius
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


class PygameImage(pygame.sprite.Sprite):
    def __init__(
        self,
        screen,
        name="chemistry.png",
        coordinates=(0, 0),
        image_size=64,
        opacity=255,
        movable: tuple[bool, bool] | list[bool, bool] = (False, False),
        sprites=None,
        menu=None
    ) -> None:
        
        super().__init__()
        self.menu = menu
        self.opacity = opacity
        self.sprites = sprites
        self.movable = movable
        self.screen = screen
        self.image_size = image_size
        self.coordinates = coordinates
        self.on_mouse = self.onMouseClicked
        self.setImage(name)
    
    def setImage(self, image):
        fullname = os.path.join('assets', image)
        if not os.path.isfile(fullname):
            return
        self.image = pygame.transform.scale(pygame.image.load(fullname), (self.image_size, self.image_size))
        self.image.set_alpha(self.opacity)
        self.rect = self.image.get_rect()
        self.update()
    
    def onMouseClicked(self, mouse_position):
        if all([
            mouse_position[0] >= self.coordinates[0] - self.image_size // 2,
            mouse_position[0] <= self.coordinates[0] + self.image_size // 2,
            mouse_position[1] >= self.coordinates[1] - self.image_size // 2,
            mouse_position[1] <= self.coordinates[1] + self.image_size // 2,
            self.rect.colliderect(self.screen.get_rect()),
            mouse_position[0] > self.image_size // 2,
            mouse_position[0] <= self.screen.get_rect()[2] - self.image_size // 2
        ]):
            if self.sprites:
                self.sprites.clear(self.screen, self.screen)
                for sprite in self.sprites:
                    sprite.kill()
            
            self.coordinates = (mouse_position[0] if self.movable[0] else self.coordinates[0], 
                                mouse_position[1] if self.movable[1] else self.coordinates[1])
            self.update()
            if self.menu:
                self.menu.InitUI()
    
    def update(self):
        if self.image:
            self.rect = self.image.get_rect(center=self.coordinates)
        else:
            return

        if self.sprites is not None:
            self.sprites.add(self)
            self.sprites.draw(self.screen)
        else:
            self.screen.blit(self.image, [int(i) - self.image_size // 2 for i in self.coordinates])
        
class PygameImageButton(PygameImage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.on_clicked = self.on_click
    
    def pressed(self, mouse_position):
        if all([
            mouse_position[0] >= self.coordinates[0] - self.image_size // 2,
            mouse_position[0] <= self.coordinates[0] + self.image_size // 2,
            mouse_position[1] >= self.coordinates[1] - self.image_size // 2,
            mouse_position[1] <= self.coordinates[1] + self.image_size // 2
        ]):
            self.on_clicked()
        
    def on_click(self):
        print("CLICKED IMAGE")


class PygameTube(PygameImageButton):
    def __init__(self, *args, **kwargs) -> None:
        self.color = VERY_DARK_BG
        self.element = ""
        self.clickable = True
        self.checker = lambda: ...
        super().__init__(*args, **kwargs)
    
    def check_if_victory(self):
        self.checker()
    
    def on_click(self):
        if not self.clickable:
            return
        self.main_window = tk.Tk()
        self.main_window.config(width=250, height=75)
        self.main_window.resizable(False, False)
        self.main_window.title("Выберите элемент")
        self.main_window.eval('tk::PlaceWindow . center')
        
        self.combo = ttk.Combobox(state="readonly", values=Database().get_elements())
        self.combo.place(x=50, y=5)
        self.combo.set(Database().get_elements()[0])
        
        ok = ttk.Button(text="OK", command=self.onOkClick)
        ok.place(x=125-40, y=35)
        self.main_window.mainloop()

    def update(self):
        size_x, size_y = self.image_size * 0.8, self.image_size // 4
        pygame.draw.ellipse(
            self.screen,
            self.color,
            (self.coordinates[0] - size_x // 2, self.coordinates[1] + size_y * 1.015, size_x, size_y),
        )
        self.screen.blit(self.image, [int(i) - self.image_size // 2 for i in self.coordinates])
        if self.element:
            self.title = PygameButton(self.screen, background_color=DARK_BG, text_color=LIGHT, border_color=DARK_BG, coordinates=(self.coordinates[0], self.coordinates[1] + self.image_size * 0.6, 80, 30), text=self.element)
        
    def fill(self, element):
        self.color = colors[Database().get_color(element)]
        self.element = element
        self.update()

    def onOkClick(self):
        self.fill(self.combo.get())
        self.main_window.destroy()


class PygameLine:
    def __init__(self, screen, start, end, color, width) -> None:
        pygame.draw.line(screen, color, start, end, width)
