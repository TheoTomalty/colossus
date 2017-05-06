import flags
import pygame
from ops import *
from surface import Surface
from text import Text

class Box(Surface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.button_bar = Surface(
            parent=self,
            position=(0, self.get_height() - flags.square_size),
            size=(flags.bar_size, flags.square_size)
        )
        self.body = Page(self)
        self.buttons = []
        
        for i in range(flags.bar_squares):
            self.buttons.append(
                Button(parent=self.button_bar, position=(i*flags.square_size, 0))
            )
    
    def initialize(self):
        self.body.initialize()
        
        for button in self.buttons:
            button.print()
        
        self.button_bar.print()
        self.print()
    
    def mouse(self, coords, pressed=False):
        for button in self.buttons:
            if button.contains(coords):
                button.mouse(pressed=pressed)
            elif button.is_hovered or button.is_pressed:
                button.clear()


class Button(Surface):
    def __init__(self, **kwargs):
        if 'shape' not in kwargs:
            kwargs['shape'] = [[1] + [0]*(flags.pixels_per_square - 1)]*(flags.pixels_per_square - 1) + \
                              [[1]*flags.pixels_per_square]
        super().__init__(**kwargs)
        
        self.is_hovered = False
        self.is_pressed = False
    
    def mouse(self, pressed=False):
        self.is_hovered = not pressed
        self.is_pressed = pressed
        shape = [[0]*flags.pixels_per_square for _ in range(flags.pixels_per_square)]
        
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                val = self.shape[i][j]
                shape[i][j] = val if val else (flags.dark_grey if pressed else flags.grey)
        
        self.load_pixels(shape)
        self.render()
    
    def clear(self):
        self.is_hovered = False
        self.is_pressed = False
        
        self.load_pixels(self.shape)
        self.render()


class Page(Surface):
    def __init__(self, parent=None, title='Page'):
        super().__init__(
            parent=parent,
            position=(0, 0),
            size=(flags.bar_size, flags.box_size - flags.square_size),
        )
        
        self.title = title
        self.title_block = Text(parent=self,
            size=(self.width, flags.title_line_height),
            position=(0, 0),
            font=flags.title_font,
        )
        self.body_block = Text(
            parent=self, 
            size=(self.width, self.height - flags.title_line_height), 
            position=(0, flags.title_line_height), 
            font=flags.body_font,
            no_margin='top',
            margin=20
        )
        
    def initialize(self):
        self.fill(flags.white)
        self.title_block.print_text(self.title)
        self.body_block.print_text(self.body)
        self.print()
    
    @property
    def body(self):
        return 'body'
