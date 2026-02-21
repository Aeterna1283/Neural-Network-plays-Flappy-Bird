import components
import pygame

#height and width for the window
height = 720
width = 550

window = pygame.display.set_mode((width, height))

ground = components.Ground(width)
pipes = []

