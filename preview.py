import pygame as pg
import numpy as np
from pygame.locals import *

# Initialize the game 
pg.init()

# Initialize the screen
screen = pg.display.set_mode((1920,1080))
pg.display.set_caption('all-arounder')

# Setting Clock
clock = pg.time.Clock()

# Rectangle coordinates 
levo_dole = 835 # za gornji i donji pravougaonik da idu levo i desno 
gore_dole = 1030 # da donji pravougaonik bude na donjoj ivici ekrana
levo_levo = 425 # za levi i desni da idu gore 

# Initialize colors 
background_color = (20,20,20)
ciglica_boja = (77,255,0)
loptica_boja = (255,0,0)
tekst_boja = (38, 38, 38)

# Screen-cover solutions
start_screen = pg.image.load("start-cover.png")

# Start menu returns true until we click the Start button
def start_menu():
    
    run = True
    while run:
        keys = pg.key.get_pressed()
        pg.display.update()
        # Displays the start screen picture
        screen.blit(start_screen, (0, 0))

        if keys[pg.K_SPACE]:
            run = False


        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        pg.display.update()
        clock.tick(60)

# Ball settings 
ball = pg.image.load('pinball-red')
ball = pg.transform.scale(ball, (50,50))
ball = ball.convert_alpha() #  convert to a Pygame format 
ball_rect = ball.get_rect() # 
ball_start = (screen.get_width()/2-ball_rect.width/2, screen.get_width()/2-ball_rect.height/2) # starting coordinates
ball_speed = (3.0,3.0) 
ball_served = False         # freeze when started 
sx, sy = ball_speed
ball_rect.topleft = ball_start

# Rounder rec's coordinates 
p1 = pg.Rect(levo_dole,gore_dole,250,50) # most down rectangle 
p2 = pg.Rect(levo_dole,0,250,50) # most top rectangle 
p3 = pg.Rect(0,levo_levo,50,250) # most left rectangle 
p4 = pg.Rect(1870,levo_levo,50,250) # most right rectangle 

# Counter display 
text_couter = 0 
font = pg.font.Font('Tanker-Regular.otf', 96)
text = font.render(str(text_couter), True, tekst_boja)
textRect = text.get_rect()
textRect.center = (1920 // 2, 1080 // 2)
running = True                 

# Set icon 
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

# Start menu 
start_menu()

# This one measures rate of change of speed per colision
speedChange = 1.05

# Game 
while running:

    dt = clock.tick(60)
    text = font.render(str(text_couter), True, tekst_boja)
    screen.fill(background_color)
    screen.blit(text, textRect)

    # Game loop 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

    keys = pg.key.get_pressed()

    # Key detections 
    if keys[pg.K_LEFT]:
        if(levo_dole > 50):
            levo_dole -= 0.5 * dt

    if keys[pg.K_RIGHT]:
        if(levo_dole < screen.get_width()-300):
            levo_dole += 0.5 * dt 

    if keys[pg.K_UP]:
        if(levo_levo > 50):
            levo_levo -= 0.25 * dt
            levo_levo -= 0.25 * dt 

    if keys[pg.K_DOWN]:
        if(levo_levo < screen.get_height()-300):
            levo_levo += 0.25 * dt 
            levo_levo += 0.25 * dt 

    if keys[pg.K_SPACE]:
        ball_served = True

    # Colision DOWN rectangle 
    if(p1[0] + p1.width >= ball_rect[0] >= p1[0] and 
        ball_rect[1] + ball_rect.height >= p1[1] and
        sy > 0):
        sy *= -1 * speedChange # every time it hits the rec, change direction - and  speed x 1.1 
        text_couter += 1
        continue
    
    # Colision RIGHT rectangle
    if(p4[1] + p4.height >= ball_rect[1] >= p4[1] and 
        ball_rect[0] + ball_rect.width >= p4[0] and
        sx > 0):
        sx *= -1 * speedChange # every time it hits the rec, change direction - and speed x 1.1 
        text_couter += 1
        continue 

    # Colision TOP rectangle
    if(p2[0] + p2.width >= ball_rect[0] >= p2[0] and 
        ball_rect[1] <= p2[1] + ball_rect.height and
        sy < 0):
        sy *= -1 * speedChange # every time it hits the rec, change direction - and  speed x 1
        text_couter += 1
        continue
    
    # Colision LEFT rectangle 
    if(p3[1] + p3.height >= ball_rect[1] >= p3[1] and 
        ball_rect[0]  <=  p3[0]+ p3.width  and 
        sx < 0):
        sx *= -1 * speedChange # every time it hits the rec, change direction - and speed x 1.1
        text_couter += 1 
        continue 
    

    if(ball_rect[0] <= 0 ):
        ball_rect[0] = 0
        sx *= -1
        

    if(ball_rect[0] >= screen.get_width() - ball.get_width()):
        ball_rect[0] = screen.get_width() - ball.get_width()
        sx *=-1

    if(ball_rect[1] <= 0 ):
        ball_rect[1] = 0
        sy *= -1

    if(ball_rect[1] >= screen.get_height() - ball.get_height()):
        ball_rect[1] = screen.get_height() - ball.get_height()
        sy *= -1

    
    p1[0] = levo_dole
    p2[0] = levo_dole
    p3[1] = levo_levo
    p4[1] = levo_levo # tako smo nazvali jebiga

    # Drawing rectangles

    pg.draw.rect(screen, ciglica_boja, p1 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p2 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p3 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p4 ,0,30)

    screen.blit(ball,ball_rect)
    if(ball_served):
        ball_rect[0] += sx 
        ball_rect[1] += sy

    pg.display.update()

