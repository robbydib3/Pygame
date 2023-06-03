# All credits to this work go to Tech With Tim on youtube
## https://www.youtube.com/watch?v=jO6qQDNa2UY

import pygame
import os

WIDTH, HEIGHT = 900,500 # Set width
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game") # set window name

white = (255,255,255) # set color
black = (0,0,0)
FPS = 60 # save FPS counter
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT) #in the middle of screen

#spaceships
yellow_spaceship = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship,(55,40)),90)
red_spaceship = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship,(55,40)),270)


def draw_window(red,yellow):
    WIN.fill(white) # fill background with saved color
    pygame.draw.rect(WIN,black,BORDER)
    WIN.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIN.blit(red_spaceship,((red.x,red.y)))
    pygame.display.update() # update display

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]: # left
        yellow.x -= 4
    if keys_pressed[pygame.K_d]: # right
        yellow.x += 4
    if keys_pressed[pygame.K_w]: # up
        yellow.y -= 4
    if keys_pressed[pygame.K_s]: # down
        yellow.y += 4

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]: # left
        red.x -= 4
    if keys_pressed[pygame.K_RIGHT]: # right
        red.x += 4
    if keys_pressed[pygame.K_UP]: # up
        red.y -= 4
    if keys_pressed[pygame.K_DOWN]: # down
        red.y += 4

def main():
    red = pygame.Rect(700,300,55,40)
    yellow = pygame.Rect(100,300,55,40)

    clock = pygame.time.Clock() # create clock
    run = True
    while run:
        clock.tick(FPS) # set frames per seconf to counter
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if x'd off it will quit
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red,yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
