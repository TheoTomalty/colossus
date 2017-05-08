import pygame

num_squares = 20
bar_squares = 8
world_squares = 6

pixels_per_square = 16
pixel_size = 2
border = 3
    
white = (255, 255, 255)
grey = (200, 200, 200)
dark_grey = (100, 100, 100)
black = (0, 0, 0)
    
frame_rate = 30 # frames per second
    
screen_size = num_squares * pixels_per_square * pixel_size
bar_size = bar_squares * pixels_per_square * pixel_size
world_size = world_squares * pixels_per_square * pixel_size
box_size = screen_size - world_size - border

square_size = pixels_per_square * pixel_size

pygame.init()
title_font = pygame.font.SysFont('helveticaneuedeskinterface', 20)
body_font = pygame.font.SysFont('helveticaneuedeskinterface', 15)

run_manager = None
character = None
