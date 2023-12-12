import pygame
from fsm import FSM
from fallingobject import FallingObject
import random

class Water(FallingObject):
    def __init__(self):
        super().__init__('ATCS-2023/Images/water.png', speed=4)


    def reset_position(self):
        self.rect.y = random.randrange(-100, -50)

        if pygame.time.get_ticks() < 10000:
            self.speed = 8
                