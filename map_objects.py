import pygame
import flags
from math import floor
from ops import *
from surface import Surface


class MapObject(Surface):
    def __init__(self, shape=None, **kwargs):
        if shape is None:
            shape = [[1]*flags.pixels_per_square]*flags.pixels_per_square
        super().__init__(shape=shape, parent=flags.run_manager.display_manager.map, **kwargs)
    
    @property
    def map_centre(self):
        return int((flags.screen_size - self.get_width())/2), int((flags.screen_size - self.get_height())/2)
    
    def index_square(self, k, l):
        return flags.pixels_per_square*flags.pixel_size*k, flags.pixels_per_square*flags.pixel_size*l
    
    def square_index(self, i, j):
        return int(floor(i/(flags.pixels_per_square*flags.pixel_size))), int(floor(j/(flags.pixels_per_square*flags.pixel_size)))
    
    def print(self, image=None):
        if image is None:
            image = self.parent
        image.blit(self.surface, self.position)
    
    def erase(self):
        flags.run_manager.display_manager.map.erase(self.position, self.get_size())


class MovingObject(MapObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def move(self, direction, distance):
        self.erase()
        
        pixel_distance = int(distance * flags.pixels_per_square * flags.pixel_size)
        new_pos = add(self.position, mult(pixel_distance, direction))
        
        bad_quadrant = self.check_overlap(new_pos)
        
        if bad_quadrant is None:
            self.position = new_pos
        else:
            interior_position = self.quadrant(bad_quadrant, new_pos)
            local_pos = sub(interior_position, self.index_square(*self.square_index(*interior_position)))
            
            overstep = dot(local_pos, direction)
            if overstep < 0:
                overstep += flags.pixels_per_square*flags.pixel_size
            else:
                overstep += 1
                
            self.position = add(self.position, mult(pixel_distance - overstep, direction))
        
        self.render()
    
    def quadrant(self, n, position=None):
        assert 0 <= n < 4
        
        if position is None:
            position = self.position
        
        dx = (0, self.get_width() - 1)
        dy = (self.get_height() - 1, 0)
        
        if n == 0:
            return add(add(position, dx), dy)
        elif n == 1:
            return add(position, dy)
        elif n == 2:
            return position
        elif n == 3:
            return add(position, dx)
    
    def overlap(self, position=None):
        return [self.square_index(*self.quadrant(n, position)) for n in range(4)]
    
    def check_overlap(self, position=None):
        indices = flags.run_manager.display_manager.map.get_impassable()
        
        for index in indices:
            for quadrant, i in zip(self.overlap(position), range(4)):
                if quadrant == index:
                    return i
        
        return None


class EmbeddedObject(MapObject):
    def __init__(self, location=None, passable=False, **kwargs):
        super().__init__(**kwargs)
        
        self.location = location if location is not None else (0, 0)
        self.position = self.index_square(*self.location)
        self.passable = passable
        
    
