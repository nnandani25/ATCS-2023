# Chat GPT helped me with a lot of the code (mainly in the game, fallingobject, and player classes), but it 
# is hard to pinpoint exactly where it is used because I had to go in and edit a lot of it
# or use parts of what it gave me.

import pygame
import sys
import random
from fallingobject import FallingObject
import gameconstants as gc
from glass import Glass
from water import Water
from blood import Blood
from player import Player
from fsm import FSM


class Game:
    def __init__(self):
        # Initialize Pygame.
        pygame.init()

        # Initialize screen.
        self.screen = pygame.display.set_mode((gc.WIDTH, gc.HEIGHT))
        pygame.display.set_caption("Falling Objects Game")
        self.clock = pygame.time.Clock()

        # Initialize font.
        font_path = "/System/Library/Fonts/Supplemental/GillSans.ttc"
        self.font = pygame.font.Font(font_path, 36)
    
        self.player = Player()
        self.active_objects = pygame.sprite.Group()
        self.blood_count = 0
        self.blood_count_position = (10, 10)


    def draw(self):
        # Draws the screen.
        self.screen.fill(gc.BLACK)
        self.active_objects.draw(self.screen)
        self.player.draw(self.screen, self.font)

        # Writes the blood count.
        blood_count_text = self.font.render("Blood Count: " + str(self.blood_count), True, gc.WHITE)
        self.screen.blit(blood_count_text, self.blood_count_position)

    
    def update(self):
        self.player.update(self.input)
        self.active_objects.update()

    def checkwin(self, blood_count):
        if blood_count == 10:
            return True
        return False
    
    def show_win_screen(self):
        # Display the winning screen for 3 seconds.
        #  Made by Chat GPT.
        self.screen.fill(gc.BLACK)
        win_text = self.font.render("You Win!", True, gc.WHITE)
        self.screen.blit(win_text, (gc.WIDTH // 2 - 50, gc.HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(3000) 

    # Prints instructions.
    def show_instructions_screen(self):
        self.screen.fill(gc.BLACK)
        instructions_text = [
            "Instructions:",
            "1. Avoid the falling glass.",
            "2. Collect blood to increase your score.",
            "3. You win when your blood count reaches 10.",
            "   ",
            "Press SPACE to start the game."
        ]

        y_offset = 100
        for line in instructions_text:
            text = self.font.render(line, True, gc.WHITE)
            self.screen.blit(text, (gc.WIDTH // 2 - text.get_width() // 2, y_offset))
            y_offset += 60

        pygame.display.flip()

        space_pressed = False
        while not space_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        space_pressed = True

    def run(self):
        self.show_instructions_screen()
        running = True
        while running:
            input = None
            # Handles key movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move("Left")
                    elif event.key == pygame.K_RIGHT:
                        self.player.move("Right")
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.stop_move("Left")
                    elif event.key == pygame.K_RIGHT:
                        self.player.stop_move("Right")
          
            # Checks for collisions
            collisions = pygame.sprite.spritecollide(self.player, self.active_objects, dokill=True)

            # If a collision occured, it changes the input so the FSM can change its state.
            for obj in collisions:
                if isinstance(obj, Glass):
                    input = "hit glass"
                    if self.player.fsm.current_state != self.player.IMMUNITY:
                        self.blood_count-= 1

                elif isinstance(obj, Water):
                    input = "hit water"

                elif isinstance(obj, Blood):
                    self.blood_count += 1
                    input = "hit blood"
            
            
            self.player.update(input)
            self.active_objects.update()
            self.draw()

            # Create new objects if needed.
            if len(self.active_objects) < gc.MAX_OBJECTS:
                random_object_class = random.choice([Glass, Water, Blood])
                if random_object_class == Glass:
                    obj = random_object_class(self.player)
                
                else:
                    obj = random_object_class()
                self.active_objects.add(obj)

            pygame.display.flip()
            self.clock.tick(gc.FPS)

            if self.checkwin(self.blood_count) or not running:
                running = False
                
        if self.checkwin(self.blood_count):
            self.show_win_screen()
                # pygame.quit()
                # sys.exit()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

   