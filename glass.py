import pygame
from fsm import FSM
from fallingobject import FallingObject
import random
import gameconstants as gc

class Glass(FallingObject):

    def __init__(self, player):
        super().__init__('ATCS-2023/Images/glass.png', speed=3)
        self.player = player


    def reset_position(self):
        self.rect.y = random.randrange(-100, -50)
        
        # Has the objects going in random places for the first 5 seconds
        if pygame.time.get_ticks() < 5000:
            print("RANDOM")
            self.rect.x = random.randrange(gc.WIDTH - self.rect.width)
        
        # Has the objects going to the player between 5 and 10 seconds
        elif pygame.time.get_ticks() < 10000:
            print("PLAYER")
            self.rect.x = self.player.rect.x

        # After 10 seconds it goes in the direction of where the player will be at next
        elif self.player.pressed_keys["left"] == True:
            print("LEFT")
            self.rect.x = self.player.rect.x - 30
            self.speed = 6
        
        elif self.player.pressed_keys["right"] == True:
            print("RIGHT")
            self.speed = 6
            
            self.rect.x = self.player.rect.x + 30
        
        # Otherwise, it will go to the player
        else:
            print("PLAYER")
            self.rect.x = self.player.rect.x