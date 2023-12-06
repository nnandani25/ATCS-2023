import pygame
from fsm import FSM
from fallingobject import FallingObject

class Water(FallingObject):
    def __init__(self):
        super().__init__('ATCS-2023/Images/water.png', speed=4)