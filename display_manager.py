import flags
import pygame
from ops import *
from map import Map
from box import Box
from world import World

class DisplayManager(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((
            flags.screen_size + flags.bar_size + 3*flags.border,
            flags.screen_size + 2*flags.border
        ))
        
        self.map = Map(
            size=(flags.screen_size, flags.screen_size),
            position=(flags.border, flags.border),
            parent=self.screen
        )
        self.box = Box(
            size=(flags.bar_size, flags.box_size),
            position= (flags.screen_size + 2*flags.border, 2*flags.border + flags.world_size),
            parent=self.screen
        )
        self.world = World(
            size=(flags.bar_size, flags.world_size), 
            position=(flags.screen_size + 2*flags.border, flags.border),
            parent=self.screen
        )
    
    def update(self):
        self.map.update()
    
    def initialize(self):
        self.map.initialize()
        self.box.initialize()
        self.world.initialize()
    
    def get_region(self, coords):
        if self.map.contains(coords):
            return "map", sub(coords, self.map.position)
        elif self.box.contains(coords):
            return "box", sub(coords, self.box.position)
        
        return "outside", coords
    
    def clear_mouse(self):
        self.box.clear_mouse()
