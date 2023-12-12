# Made by Chat GPT
import pygame
import sys
import random
import gameconstants as gc

class FallingObject(pygame.sprite.Sprite):

    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(gc.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed = speed

    def update(self):
        # Changes the location when it goes off the screen.
        self.rect.y += self.speed
        if self.rect.y > gc.HEIGHT:
            self.reset_position()

    def reset_position(self):
        # Sets a random position.
        self.rect.y = random.randrange(-100, -50)
        self.rect.x = random.randrange(gc.WIDTH - self.rect.width)