import pygame
from fsm import FSM
import gameconstants as gc
from blood import Blood

class Player(pygame.sprite.Sprite):

    def __init__(self):

        NUETRAL = "nuetral"
        IMMUNITY = "immunity"
        STOPPED = "stopped"
        self.fsm.add_state(self.NEUTRAL)
        self.fsm.add_state(self.IMMUNITY)
        self.fsm.add_state(self.STOPPED)
        self.fsm.set_state(self.NEUTRAL)
        self.init_fsm()

        super().__init__()
        self.image = pygame.image.load("ATCS-2023/Images/girl.png")
        self.rect = self.image.get_rect()
        self.width, self.height = 50, 50
        self.rect.x = (gc.WIDTH - self.width) // 2
        self.rect.y = gc.HEIGHT - self.height - 80  # Place the player at the bottom of the screen
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < gc.WIDTH - self.width:
            self.rect.x += self.speed
    
    def init_fsm(self):
        self.fsm.add_transition("hit blood", self.NUETRAL, self.get_immunity, self.IMMUNITY)
        self.fsm.add_transition("hit blood", self.STOPPED, self.get_immunity, self.IMMUNITY)
        self.fsm.add_transition("hit blood", self.IMMUNITY, None, self.IMMUNITY)

        self.fsm.add_transition("hit glass", self.NUETRAL, self.stopped, self.STOPPED)
        self.fsm.add_transition("hit glass", self.STOPPED, None, self.STOPPED)
        self.fsm.add_transition("hit glass", self.IMMUNITY, None, self.IMMUNITY)

        self.fsm.add_transition("hit water", self.NUETRAL, None, self.NUETRAL)
        self.fsm.add_transition("hit water", self.STOPPED, None, self.NUETRAL)
        self.fsm.add_transition("hit water", self.IMMUNITY, None, self.NUETRAL)


    def get_immunity(self):
        pass

    def stopped(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time > self.stop_duration:
            self.last_hit_time = current_time
            self.fsm.set_state(self.NEUTRAL)