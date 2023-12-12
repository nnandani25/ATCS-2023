# Chat GPT helped with this code
import pygame
import gameconstants as gc
from blood import Blood
from fsm import FSM

class Player(pygame.sprite.Sprite):

    NUETRAL = "nuetral"
    IMMUNITY = "immunity"
    STOPPED = "stopped"

    def __init__(self):
        super().__init__()
        # Initialzes player variables (image, location, speed, etc.).
        self.image = pygame.image.load("ATCS-2023/Images/girl2.png")
        self.rect = self.image.get_rect()
        self.width, self.height = 50, 50
        self.rect.x = (gc.WIDTH - self.width) // 2
        self.rect.y = gc.HEIGHT - self.height - 80
        self.speed = 5

        self.pressed_keys = {'left': False, 'right': False}

        # Timer variables.
        self.stopped_time = 0
        self.stopped_duration = 5000 

        # Immunity timer variables.
        self.immunity_time = 0
        self.immunity_duration = 5000 

        # Initalizes FSM.
        self.fsm = FSM(self.NUETRAL)
        self.init_fsm()

    def draw(self, screen, font):
        screen.blit(self.image, self.rect)

        # Prints the immunity timer.
        if self.fsm.current_state == self.IMMUNITY:
            time_left = max(0, (self.immunity_duration - (pygame.time.get_ticks() - self.immunity_time)) // 1000)
            immunity_text = font.render(f"Immunity: {time_left} seconds", True, gc.WHITE)
            screen.blit(immunity_text, (10, 60))

        # Prints the stopped timer.
        elif self.fsm.current_state == self.STOPPED:
            time_left = max(0, (self.stopped_duration - (pygame.time.get_ticks() - self.stopped_time)) // 1000)
            stopped_text = font.render(f"Stopped: {time_left} seconds", True, gc.WHITE)
            screen.blit(stopped_text, (10, 60))
        else:
            return

    def move(self, direction):
        # Set the corresponding pressed_keys entry to True when a key is pressed.
        if self.fsm.current_state == self.STOPPED:
         # Player is in the "stopped" state, do not allow movement.
            return
        else:
            if direction == "Right":
                self.pressed_keys['right'] = True
            elif direction == "Left":
                self.pressed_keys['left'] = True

    def stop_move(self, direction):
        # Set the corresponding pressed_keys entry to False when a key is released.
            if direction == "Right":
                self.pressed_keys['right'] = False
            elif direction == "Left":
                self.pressed_keys['left'] = False
        
    
    def init_fsm(self):
        self.fsm.add_transition("hit blood", self.NUETRAL, self.start_immunity_timer, self.IMMUNITY)
        self.fsm.add_transition("hit blood", self.STOPPED, self.start_immunity_timer, self.IMMUNITY)
        self.fsm.add_transition("hit blood", self.IMMUNITY, None, self.IMMUNITY)

        self.fsm.add_transition("hit glass", self.NUETRAL, self.start_stopped_timer, self.STOPPED)
        self.fsm.add_transition("hit glass", self.STOPPED, None, self.STOPPED)
        self.fsm.add_transition("hit glass", self.IMMUNITY, None, self.IMMUNITY)

        self.fsm.add_transition("hit water", self.NUETRAL, None, self.NUETRAL)
        self.fsm.add_transition("hit water", self.STOPPED, None, self.STOPPED)
        self.fsm.add_transition("hit water", self.IMMUNITY, None, self.IMMUNITY)


    def get_state(self):
        return self.fsm.current_state

    def start_stopped_timer(self):
        self.stopped_time = pygame.time.get_ticks()
    
    def start_immunity_timer(self):
        self.immunity_time = pygame.time.get_ticks()

    def update(self, input=None):
        if input:
            self.fsm.process(input)

        # Handles the stopped timer and sets the current state back to nuetral once the timer it up.
        if self.fsm.current_state == self.STOPPED:
            current_time = pygame.time.get_ticks()
            if current_time - self.stopped_time > self.stopped_duration:
                self.fsm.current_state = self.NUETRAL

        # Handles the immunity timer and sets the current state back to nuetral once the timer it up.
        if self.fsm.current_state == self.IMMUNITY:
            current_time = pygame.time.get_ticks()
            if current_time - self.immunity_time > self.immunity_duration:
                self.fsm.current_state = self.NUETRAL

        # Allows for key movement and stops the player from going off the screen.
        if self.fsm.current_state != self.STOPPED:
            if self.pressed_keys['right'] and self.rect.x + self.speed < gc.WIDTH - self.width - 130:
                self.rect.x += self.speed
            if self.pressed_keys['left'] and self.rect.x - self.speed > 0:
                self.rect.x -= self.speed

