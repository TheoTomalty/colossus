import flags
from map_objects import MovingObject
from projectile import Projectile

class Character(object):
    def __init__(self):
        shape = [[1]*flags.pixels_per_square] + \
                [[1] + [0]*(flags.pixels_per_square - 2) + [1]]*(flags.pixels_per_square - 2) + \
                [[1]*flags.pixels_per_square]
        self.surface = MovingObject(shape=shape)
        self.speed = 6 # squares per second
    
    def move(self, direction):
        distance = self.speed / flags.frame_rate
        self.surface.move(direction, distance)
    
    def fire(self, mouse):
        spell = Projectile(mouse=mouse, position=self.surface.position)
        self.surface.parent.add_projectile(spell)
    
    def print(self):
        self.surface.print()
