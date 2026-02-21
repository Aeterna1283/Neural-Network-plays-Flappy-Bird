import pygame
import random

#class for the game's ground
class Ground:
    ground_level = 500
    
    #constructor for Ground class, which is creating the self and width objects
    def __init__(self, width):
        self.x, self.y = 0, Ground.ground_level
        #coordinates of where to display the ground
        self.rect = pygame.Rect(self.x, self.y, width, 5)
        
    #draws the window, after the line is created
    def draw(self, window):
        #arguments are where to draw the rectangle (in window), color (white), and rectangle
        pygame.draw.rect(window, (255, 255, 255), self.rect)


#class for the game's pipes: each pipe is equal distant apart
#but the hole is random each time
class Pipes:
    width = 15
    opening = 100
    
    #constructor for Pipes class, which instantiates pipe objects
    def __init__(self, width):
        self.x = width
        self.bottom_height = random.randint(10, 300)
        self.top_height = Ground.ground_level - self.bottom_height - self.opening
        self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.off_screen = False
        
    def draw(self, window):
        self.bottom_rect = pygame.Rect(self.x, Ground.ground_level - self.bottom_height, self.width, self.bottom_height)
        pygame.draw.rect(window, (255, 255, 255), self.bottom_rect)
        
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        pygame.draw.rect(window, (255, 255, 255), self.top_rect)
    
    def update(self):
        self.x -= 1
        if self.x + Pipes.width <= 50:
            self.passed = True
        if self.x <= -self.width:
            self.off_screen = True