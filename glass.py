import pygame
from fsm import FSM
from fallingobject import FallingObject

class glass(FallingObject):
    def __init__(self):
        super().__init__('ATCS-2023/Images/glass.png', speed=3)