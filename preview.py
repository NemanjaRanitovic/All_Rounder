import pygame as pg
import numpy as np
from pygame.locals import *

pg.init()
screen = pg.display.set_mode((1920,1080))
pg.display.set_caption('Igrica')
clock = pg.time.Clock()

levo_dole = 835 # za gornji i donji pravougaonik da idu levo i desno 

gore_dole = 1030 # da donji pravougaonik bude na donjoj ivici ekrana

levo_levo = 425 # za levi i desni da idu gore 

#Kod za dugme-----------------------------------------------
play_button_colour = (0,0,170) 
play_button_size = (250,50)
play_rect = [screen.get_width()/2 - play_button_size[0]/2, screen.get_height()/2-play_button_size[1]/2 , (play_button_size)]


#-----------------------------------------------------------


background_color = (20,20,20)
ciglica_boja = (77,255,0)
loptica_boja = (255,0,0)

ball = pg.image.load('./pinball.png')
ball = pg.transform.scale(ball, (50,50))
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (screen.get_width()/2-ball_rect.width/2, screen.get_width()/2-ball_rect.height/2)
ball_speed=(3.0,3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

p1 = pg.Rect(levo_dole,gore_dole,250,50)
p2 = pg.Rect(levo_dole,0,250,50)
p3 = pg.Rect(0,levo_levo,50,250)
p4 = pg.Rect(1870,levo_levo,50,250)


running = True


while running:
    dt = clock.tick(60)
    screen.fill(background_color,play_button_colour,play_rect) 
    pg.draw.rect(screen,)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
    keys = pg.key.get_pressed()

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

    if(p1[0] + p1.width >= ball_rect[0] >= p1[0] and 
        ball_rect[1] + ball_rect.height >= p1[1] and
        sy > 0):
        sy *= -1
        continue
    # dodati jos 3 ova ifa za ostala 3 pravougaonika
        

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
    p4[1] = levo_levo

    pg.draw.rect(screen, ciglica_boja, p1 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p2 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p3 ,0,30)
    pg.draw.rect(screen, ciglica_boja, p4 ,0,30)

    screen.blit(ball,ball_rect)
    if(ball_served):
        ball_rect[0] += sx
        ball_rect[1] += sy
    pg.display.update()



# sirina je 1920 pola je 960 