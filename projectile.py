import flags
import pygame
from map_objects import MovingObject
from ops import *

class Projectile(MovingObject):
    def __init__(self, speed=8, mouse=(0, 0), **kwargs):
        #kwargs['shape'] = [[2]*flags.pixels_per_square]*flags.pixels_per_square
        if 'shape' not in kwargs:
            kwargs['shape'] = [[1]*8]*8
        MovingObject.__init__(self, **kwargs)
        
        self.speed = speed
        self.direction = unit(sub(mouse, self.position))
        self.true_pos = self.position
        
        self.elapsed_time = 0
        self.clock = pygame.time.Clock()
    
    def place(self):
        self.render()
    
    def update(self):
        self.clock.tick()
        
        time = self.clock.get_time() /1000 # in seconds
        self.elapsed_time += time
        
        if self.elapsed_time > 3:
            self.delete()
            return
        
        self.erase()
        
        distance = self.speed * (flags.pixels_per_square*flags.pixel_size) * time
        self.true_pos = add(self.true_pos, mult(distance, self.direction))
        self.position = closest(self.true_pos)
        
        self.render()
    
    def delete(self):
        self.erase()
        flags.run_manager.display_manager.map.projectiles.pop(flags.run_manager.display_manager.map.projectiles.index(self))
        
