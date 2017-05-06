import pygame
import flags
from input_manager import InputManager
from display_manager import DisplayManager

class RunManager(object):
    def __init__(self):
        self.input_manager = InputManager()
        self.display_manager = DisplayManager()
        
    def start_game(self):
        running = True
        
        clock = pygame.time.Clock()
        
        self.display_manager.initialize()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.input_manager.get_input()
            self.display_manager.update()
            pygame.display.flip()
            
            clock.tick_busy_loop(flags.frame_rate)
