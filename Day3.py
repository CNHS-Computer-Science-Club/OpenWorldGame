import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50
SQUARE_COLOR = (0, 128, 255)
BLOCK_COLOR = (255, 0, 0)
BLOCK_SIZE = 70
BACKGROUND_COLOR = (30, 30, 30)
MOVE_SPEED = 5
ENEMY_COLOR = (255, 255, 0)
ENEMY_SIZE = 40
ENEMY_SPEED = 2
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
MAX_HEALTH = 100

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initial square position
square_x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
square_y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2

# Initial block position
block_x = SCREEN_WIDTH // 4 - BLOCK_SIZE // 2
block_y = SCREEN_HEIGHT // 4 - BLOCK_SIZE // 2

# Health
health = MAX_HEALTH

# Enemy list
enemies = []

def spawn_enemy():
    enemy_x = random.choice([0, SCREEN_WIDTH - ENEMY_SIZE])
    enemy_y = random.choice([0, SCREEN_HEIGHT - ENEMY_SIZE])
    enemies.append([enemy_x, enemy_y])

# Spawn initial enemies
for _ in range(3):
    spawn_enemy()

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys currently being pressed
    keys = pygame.key.get_pressed()
    prev_x, prev_y = square_x, square_y
    
    # Update square position based on arrow keys
    if keys[pygame.K_UP]:
        square_y -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        square_y += MOVE_SPEED
    if keys[pygame.K_LEFT]:
        square_x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        square_x += MOVE_SPEED

    # Prevent the square from going off-screen
    square_x = max(0, min(SCREEN_WIDTH - SQUARE_SIZE, square_x))
    square_y = max(0, min(SCREEN_HEIGHT - SQUARE_SIZE, square_y))

    # Collision detection with the block
    square_rect = pygame.Rect(square_x, square_y, SQUARE_SIZE, SQUARE_SIZE)
    block_rect = pygame.Rect(block_x, block_y, BLOCK_SIZE, BLOCK_SIZE)

    if square_rect.colliderect(block_rect):
        square_x, square_y = prev_x, prev_y

    # Update enemies
    for enemy in enemies:
        enemy_x, enemy_y = enemy
        if enemy_x < square_x:
            enemy[0] += ENEMY_SPEED
        elif enemy_x > square_x:
            enemy[0] -= ENEMY_SPEED
        if enemy_y < square_y:
            enemy[1] += ENEMY_SPEED
        elif enemy_y > square_y:
            enemy[1] -= ENEMY_SPEED

        # Check collision with player
        enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)
        if square_rect.colliderect(enemy_rect):
            health -= 1
            if health <= 0:
                print("Game Over!")
                pygame.quit()
                sys.exit()

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, SQUARE_COLOR, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, BLOCK_COLOR, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))
    
    # Draw health bar
    pygame.draw.rect(screen, (255, 0, 0), (20, 20, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
    pygame.draw.rect(screen, (0, 255, 0), (20, 20, HEALTH_BAR_WIDTH * (health / MAX_HEALTH), HEALTH_BAR_HEIGHT))
    
    pygame.display.flip()
    clock.tick(60)
