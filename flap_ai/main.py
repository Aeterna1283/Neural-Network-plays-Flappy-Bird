import pygame
from sys import exit
import config
import components
import population

#pygame is initialized, and the clock is created
pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def generate_pipes():
    config.pipes.append(components.Pipes(config.width))
    

#function for quitting if the x is pressed on the window, hence the name
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#Main loop of the program
def main():
    pipes_spawn_time = 10
    
    while True:
        quit_game() #if user closes window, loop is set to false
        
        #the window is refreshed each frame, and filled to black
        config.window.fill((0,0,0))
        
        #creates the ground
        config.ground.draw(config.window)
        
        #spawn pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1
        
        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
        
        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()
            
        
        #frame rate 
        clock.tick(200)
        #updates the display 
        pygame.display.flip()

main()