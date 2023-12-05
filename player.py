import pygame
from fsm import FSM

class player(pygame.sprite.Sprite):

    def __init__(self, game, x=50, y=50):
        super().__init__()

        self.game = game
