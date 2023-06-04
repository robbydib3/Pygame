# All credits to this work go to Tech With Tim on youtube
## https://www.youtube.com/watch?v=jO6qQDNa2UY

import pygame
import os
pygame.font.init()
pygame.mixer.init()
from pygame import mixer

WIDTH, HEIGHT = 900,500 # Set width
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game") # set window name

HEALTH_FONT = pygame.font.SysFont('comicsans',30)
WINNER_FONT = pygame.font.SysFont('comicsans',30)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

mixer.music.load(os.path.join('Assets','Maintheme.mp3'))
mixer.music.play(-1)
mixer.music.set_volume(0.25)

white = (255,255,255) # set color
black = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 # save FPS counter
BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT) #in the middle of screen
BULLET_VEL = 5
max_bullets = 3 

YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT + 2

#spaceships
yellow_spaceship = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship,(55,40)),90)
red_spaceship = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship,(55,40)),270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.jpg')),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,i):
    WIN.fill((0,0,0))
    WIN.blit(SPACE,(i,0)) # fill background with saved color
    WIN.blit(SPACE, (WIDTH + i,0))

    if i == 0:
        WIN.blit(SPACE,(WIDTH + i,0))

    pygame.draw.rect(WIN,black,BORDER)

    red_health_text = HEALTH_FONT.render('Health: ' + str(red_health),1,white)
    yellow_health_text = HEALTH_FONT.render('Health: ' + str(yellow_health),1,white)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text, (10,10))


    WIN.blit(yellow_spaceship,(yellow.x,yellow.y))
    WIN.blit(red_spaceship,((red.x,red.y)))

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    


    pygame.display.update() # update display

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and  yellow.x - 4 > 0: # left
        yellow.x -= 4
    if keys_pressed[pygame.K_d] and  yellow.x + 4 + yellow.width < BORDER.x: # right
        yellow.x += 4
    if keys_pressed[pygame.K_w] and  yellow.y - 4 > 0: # up
        yellow.y -= 4
    if keys_pressed[pygame.K_s] and  yellow.y + 4 + yellow.height < HEIGHT -20: # down
        yellow.y += 4

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - 4  > BORDER.x + BORDER.width: # left
        red.x -= 4
    if keys_pressed[pygame.K_RIGHT] and red.x + 4 + red.width < WIDTH:# right
        red.x += 4
    if keys_pressed[pygame.K_UP] and red.y - 4 > 0: # up
        red.y -= 4
    if keys_pressed[pygame.K_DOWN] and  red.y + 4 + red.height < HEIGHT -20: # down
        red.y += 4

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,white)
    WIN.blit(draw_text,(WIDTH//2 - draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(700,300,55,40)
    yellow = pygame.Rect(100,300,55,40)

    yellow_bullets = []
    red_bullets = []

    yellow_health = 5
    red_health = 5
    i = 0

    clock = pygame.time.Clock() # create clock
    run = True
    while run:
        clock.tick(FPS) # set frames per seconf to counter
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if x'd off it will quit
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.height//2 + 7,10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x ,red.y + red.height//2 + 7,10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        WIN.blit(SPACE,(0,0)) # fill background with saved color
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets,red_bullets,yellow,red)

        draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health,i)
        i -= 1

        if i == -WIDTH:
            i = 0

    main()

if __name__ == "__main__":
    main()
