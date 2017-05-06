import pygame
import flags

class InputManager(object):
    def __init__(self):
        self.move_map = {pygame.K_w: ( 0, -1),
                         pygame.K_s: ( 0,  1),
                         pygame.K_a: (-1,  0),
                         pygame.K_d: ( 1,  0)}
    
    def get_input(self):
        pressed = pygame.key.get_pressed()
        
        for i, val in zip(range(len(pressed)), pressed):
            if val and i in self.move_map:
                flags.character.move(self.move_map[i])
        
        mouse_pos = pygame.mouse.get_pos()
        region, coords = flags.run_manager.display_manager.get_region(mouse_pos)
        
        # If pressed
        mouse = pygame.mouse.get_pressed()
        left_button = bool(mouse[0])
        
        flags.run_manager.display_manager.box.mouse(mouse_pos, pressed=left_button)
        
        if mouse[0]:
            if region == 'map':
                flags.character.fire(coords)
