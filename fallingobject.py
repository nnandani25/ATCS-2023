# import pygame
# import sys
# import random

# class FallingObject(pygame.sprite.Sprite):
#     WIDTH, HEIGHT = 800, 600
#     FPS = 60
#     WHITE = (255, 255, 255)
#     BLACK = (0, 0, 0)

#     def __init__(self, image_path, speed):
#         super().__init__()
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(FallingObject.WIDTH - self.rect.width)
#         self.rect.y = random.randrange(-100, -50)
#         self.speed = speed

#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y > FallingObject.HEIGHT:
#             self.reset_position()

#     def reset_position(self):
#         self.rect.y = random.randrange(-100, -50)
#         self.rect.x = random.randrange(FallingObject.WIDTH - self.rect.width)

# # Initialize Pygame
# pygame.init()

# # Initialize screen
# screen = pygame.display.set_mode((FallingObject.WIDTH, FallingObject.HEIGHT))
# pygame.display.set_caption("Falling Objects Game")
# clock = pygame.time.Clock()

# all_sprites = pygame.sprite.Group()

# # Create instances
# for _ in range(5):
#     obj1 = FallingObject('ATCS-2023/Images/glass.png', speed=3)
#     obj2 = FallingObject('ATCS-2023/Images/water.png', speed=4)
#     obj3 = FallingObject('ATCS-2023/Images/blood.png', speed=2)
#     all_sprites.add(obj1, obj2, obj3)

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     all_sprites.update()

#     # Draw everything
#     screen.fill(FallingObject.BLACK)
#     all_sprites.draw(screen)

#     pygame.display.flip()
#     clock.tick(FallingObject.FPS)

# pygame.quit()
# sys.exit()
import pygame
import sys
import random

class FallingObject(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (25, 36, 100)
    MAX_OBJECTS = 10

    active_objects = pygame.sprite.Group()

    OBJECT_IMAGES = [
        'ATCS-2023/Images/glass.png',
        'ATCS-2023/Images/water.png',
        'ATCS-2023/Images/blood.png'
    ]

    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(FallingObject.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -50)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > FallingObject.HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.y = random.randrange(-100, -50)
        self.rect.x = random.randrange(FallingObject.WIDTH - self.rect.width)

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((FallingObject.WIDTH, FallingObject.HEIGHT))
pygame.display.set_caption("Falling Objects Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw active objects
    FallingObject.active_objects.update()
    screen.fill(FallingObject.BLACK)
    FallingObject.active_objects.draw(screen)

    # Create new objects if needed
    if len(FallingObject.active_objects) < FallingObject.MAX_OBJECTS:
        random_image_path = random.choice(FallingObject.OBJECT_IMAGES)
        obj = FallingObject(random_image_path, speed=random.randint(2, 4))
        FallingObject.active_objects.add(obj)

    pygame.display.flip()
    clock.tick(FallingObject.FPS)

pygame.quit()
sys.exit()
