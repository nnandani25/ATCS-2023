import pygame
from fsm import FSM
from fallingobject import FallingObject

class blood(FallingObject):
    def __init__(self):
            super().__init__('ATCS-2023/Images/blood.png', speed=2)
        