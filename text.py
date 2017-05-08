import pygame
import flags
from ops import *
from textrect.textrect import render_textrect
from surface import Surface

class Text(Surface):
    def __init__(self, text='', fixed_width=None, font=flags.body_font, margin=5, no_margin=None, justify_under=None, **kwargs):
        super().__init__(**kwargs)
        
        if fixed_width is None:
            fixed_width = self.parent.width
        self.fixed_width = fixed_width
        
        self.text = text
        self.font = font
        self.margin = margin
        self.justify_under = justify_under
        
        if no_margin == None:
            self.no_margin = []
        elif isinstance(no_margin, str):
            self.no_margin = [no_margin]
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
    def line_width(self):
        return self.fixed_width - self.left_margin - self.right_margin
    
    def print_text(self, text):
        self.load_text(text)
        self.print()
    
    def justify(self):
        if self.justify_under is not None:
            self.position = (self.position[0], self.justify_under.position[1] + self.justify_under.height)
    
    def load_text(self, text, text_colour=flags.black, background_colour=flags.white):
        final_lines = []
        
        requested_lines = text.splitlines()
        
        for requested_line in requested_lines:
            words = requested_line.split(' ')
            too_big = lambda x: self.font.size(x)[0] >= self.line_width
            
            line = ''
            for word in words:
                new_string = line + (' ' if line else '') + word
                if too_big(new_string):
                    final_lines.append(line)
                    line = ''
                line += (' ' if line else '') + word
            final_lines.append(line)
        
        line_heights = [self.font.size(line)[1] for line in final_lines]
        total_height = sum(line_heights) + self.bottom_margin + self.top_margin
        
        self.surface = pygame.Surface((self.fixed_width, total_height))
        self.surface.fill(background_colour)
        self.justify()
        
        for line, i in zip(final_lines, range(len(line_heights))):
            tempsurface = self.font.render(line, 1, text_colour)
            self.blit(tempsurface, (self.left_margin, self.top_margin + sum(line_heights[:i])))
        
        return total_height
                
            
