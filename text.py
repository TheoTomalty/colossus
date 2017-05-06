import pygame
import flags
from ops import *
from textrect.textrect import render_textrect
from surface import Surface

class Text(Surface):
    def __init__(self, text='', font=None, margin=5, no_margin=None, **kwargs):
        super().__init__(**kwargs)
        
        self.text = text
        self.font = font
        self.margin = margin
        
        if no_margin == None:
            self.no_margin = []
        else:
            self.no_margin = no_margin
    
    @property
    def top_margin(self):
        if 'top' in self.no_margin:
            return 0
        
        return self.margin
    
    @property
    def bottom_margin(self):
        if 'bottom' in self.no_margin:
            return 0
        
        return self.margin
    
    @property
    def left_margin(self):
        if 'left' in self.no_margin:
            return 0
        
        return self.margin
    
    @property
    def right_margin(self):
        if 'right' in self.no_margin:
            return 0
        
        return self.margin
    
    @property
    def text_box_size(self):
        return sub(
                self.size,
                (self.left_margin + self.right_margin, self.top_margin + self.bottom_margin)
            )
    
    def print(self):
        self.fill(flags.white)
        rect = pygame.Rect((0, 0), self.text_box_size)
        
        paragraph = render_textrect(self.text, self.font, rect, flags.black, flags.white)
        self.blit(paragraph, (self.left_margin, self.top_margin))
        
        self.parent.blit(self, self.position)
    
    def print_text(self, text):
        self.text = text
        self.print()
