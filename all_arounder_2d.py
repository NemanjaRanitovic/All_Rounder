import pygame as pg 
import numpy as np 
from pygame.locals import *

# Initialize the game 
pg.init()

# Initialize the screen 
screen_width = 1920
screen_height = 1080 
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('all-arounder')

# Initialize the clock 
clock = pg.time.Clock()

# Initialize the colors 
background_color = (20, 20, 20)
ball_color = (255, 0, 0)
block_color = (77, 255, 0)
text_color = (38, 38, 38)

# Blocks (left, top, width, height) - on a 1920x1080 plane
middle_blocks_left_point = screen_width/2 - 250/2
sides_blocks_top_point = screen_height/2 - 250/2

block_bottom = pg.Rect(middle_blocks_left_point, screen_height-50, 250, 50)
block_top = pg.Rect(middle_blocks_left_point, 0, 250, 50)
block_left = pg.Rect(0, sides_blocks_top_point, 50, 250)
block_right = pg.Rect(screen_width-50, sides_blocks_top_point, 50, 250)

# Game loop 
running = True
while running: 

    dt = clock.tick(60)
    screen.fill(background_color)

    # Drawing blocks
    pg.draw.rect(screen, block_color, block_bottom, 0, 30)
    pg.draw.rect(screen, block_color, block_top, 0, 30)
    pg.draw.rect(screen, block_color, block_left, 0, 30)
    pg.draw.rect(screen, block_color, block_right, 0, 30)

    # Block movement
    keys = pg.key.get_pressed()
    block_movement_speed = 1.2
    if keys[pg.K_LEFT]:
        if(middle_blocks_left_point > 50):
            middle_blocks_left_point -= block_movement_speed * dt

    if keys[pg.K_RIGHT]:
        if(middle_blocks_left_point < screen.get_width()-300):
            middle_blocks_left_point += block_movement_speed * dt 

    if keys[pg.K_UP]:
        if(sides_blocks_top_point > 50):
            sides_blocks_top_point -= block_movement_speed * dt

    if keys[pg.K_DOWN]:
        if(sides_blocks_top_point < screen.get_height()-300):
            sides_blocks_top_point += block_movement_speed * dt

    block_bottom[0] = middle_blocks_left_point
    block_top[0] = middle_blocks_left_point
    block_left[1] = sides_blocks_top_point
    block_right[1] = sides_blocks_top_point

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            running = False
            pg.quit()
    
    pg.display.update()