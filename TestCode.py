## Install and setup
import pygame

pygame.init()

# Set the width and height of the screen (window)
screen_width = 800
screen_height = 600

# Create the screen (window)
screen = pygame.display.set_mode((screen_width, screen_height))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen (window)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
