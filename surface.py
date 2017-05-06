import pygame
import flags
from ops import *

class Surface(pygame.Surface):
    def __init__(self, size=None, position=(0, 0), parent=None, shape=None, **kwargs):
        if shape is not None:
            size = (len(shape)*flags.pixel_size, len(shape[0])*flags.pixel_size)
        super().__init__(size, **kwargs)
        
        self.position = position
        self.parent = parent
        self.shape = shape
        
        if shape is not None:
            self.load_pixels(shape)
    
    @property
    def rect(self):
        return self.get_rect()
    
    @property
    def width(self):
        return self.get_width()
    
    @property
    def height(self):
        return self.get_height()
    
    @property
    def size(self):
        return self.get_size()
    
    def print(self):
        self.parent.blit(self, self.position)
    
    def render(self):
        ancestor = self
        while hasattr(ancestor, 'parent'):
            ancestor.print()
            ancestor = ancestor.parent
    
    def initialize(self):
        self.fill(flags.white)
        self.print()
    
    def contains(self, coords):
        position = self.global_coords
        return 0 <= coords[0] - position[0] < self.get_width() and  0 <= coords[1] - position[1] < self.get_height()
    
    @property
    def global_coords(self):
        ancestor = self
        position = (0, 0)
        while hasattr(ancestor, 'parent'):
            position = add(position, ancestor.position)
            ancestor = ancestor.parent
        
        return position
    
    def load_pixels(self, shape):
        pixel_array = pygame.PixelArray(self)
        
        for row, i in zip(shape, range(len(shape))):
            for j in range(len(row)):
                val = shape[i][j]
                
                size = flags.pixel_size
                indices = [[(size*i + k, size*j + l) for l in range(size)] for k in range(size)]
                
                for row in indices:
                    for k, l in row:
                        pixel_array[k][l] = self.pixel_val(val)
    
    def pixel_val(self, val):
        if isinstance(val, int):
            return flags.black if val else flags.white
        else:
            return val
