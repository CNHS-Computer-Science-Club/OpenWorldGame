import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SQUARE_SIZE = 50
SQUARE_COLOR = (0, 128, 255)
BACKGROUND_COLOR = (30, 30, 30)
MOVE_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initial square position
square_x = SCREEN_WIDTH // 2 - SQUARE_SIZE // 2
square_y = SCREEN_HEIGHT // 2 - SQUARE_SIZE // 2

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys currently being pressed
    keys = pygame.key.get_pressed()

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

    # Drawing
    screen.fill(BACKGROUND_COLOR)  # Fill the background
    pygame.draw.rect(screen, SQUARE_COLOR, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))  # Draw the square

    pygame.display.flip()  # Update the display

    clock.tick(60)  # Limit the frame rate to 60 FPS
