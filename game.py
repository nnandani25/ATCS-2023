import pygame
import sys
import random
from fallingobject import FallingObject
import gameconstants as gc
from glass import Glass
from water import Water
from blood import Blood
from player import Player

def main():
    # Initialize Pygame
    pygame.init()

    # Initialize screen
    screen = pygame.display.set_mode((gc.WIDTH, gc.HEIGHT))
    pygame.display.set_caption("Falling Objects Game")
    clock = pygame.time.Clock()
    player = Player() 

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update and draw active objects
        player.update()
        FallingObject.active_objects.update()
        
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    
        keys = pygame.key.get_pressed()
        player.move(keys)


        # if event.type == pygame.KEYDOWN:
        #         if something == "hit glass":
        #             player.fsm.trigger("hit glass")
        #         elif event.key == pygame.K_b:
        #             player.fsm.trigger("hit blood")
        #         elif event.key == pygame.K_w:
        #             player.fsm.trigger("hit water")
                
        screen.fill(gc.BLACK)
        FallingObject.active_objects.draw(screen)
        player.draw(screen)

        # Create new objects if needed
        if len(FallingObject.active_objects) < gc.MAX_OBJECTS:
            random_object_class = random.choice([Glass, Water, Blood]) 
            obj = random_object_class()
            FallingObject.active_objects.add(obj)

        pygame.display.flip()
        clock.tick(gc.FPS)



if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()





        # for event in pygame.event.get():
        #     print(event)
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:
        #             player.move("RIGHT")
        #         elif event.key == pygame.K_LEFT:
        #             player.move("LEFT")