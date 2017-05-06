import pygame
import flags
from map_objects import EmbeddedObject
from projectile import Projectile
from surface import Surface

class Map(Surface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.objects = []
        self.projectiles = []
        self.background = None
    
    def load_background(self):
        self.background = pygame.Surface((flags.screen_size, flags.screen_size))
        self.background.fill(flags.white)
        
        for obj in self.objects:
            obj.print(self.background)
    
    def initialize(self):
        self.load_background()
        self.blit(self.background, (0, 0))
        
        flags.character.print()
        self.print()
    
    def update(self):
        flags.character.print()
        for projectile in self.projectiles:
            projectile.update()
        
        self.print()
    
    def erase(self, position, dims):
        y_min = max(position[0], 0)
        y_max = min(position[0] + dims[0], flags.screen_size)
        x_min = max(position[1], 0)
        x_max = min(position[1] + dims[1], flags.screen_size)
        
        self.blit(
            self.background.subsurface(y_min, x_min, y_max - y_min, x_max - x_min),
            (y_min, x_min)
        )
    
    def get_impassable(self):
        impassable = []
        
        for obj in self.objects:
            if not obj.passable:
                impassable.append(obj.location)
        
        return impassable
    
    def add_object(self, obj):
        assert isinstance(obj, EmbeddedObject)
        
        self.objects.append(obj)

    def add_projectile(self, obj):
        assert isinstance(obj, Projectile)
        
        self.projectiles.append(obj)
        obj.place()
