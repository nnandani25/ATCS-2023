import pygame
import sys
import random
import gameconstants as gc
from glass import Glass
from blood import Blood
from water import Water

class FallingObject(pygame.sprite.Sprite):

    active_objects = pygame.sprite.Group()


    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(gc.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > gc.HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.y = random.randrange(-100, -50)
        self.rect.x = random.randrange(gc.WIDTH - self.rect.width)


    # def load(self):
    #     if something == "hit glass":
    #         self.active_objects.add(Glass())