import pygame as pg 
import numpy as np 
from pygame.locals import *
import math
import funkcije as fu

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

# Ball radius -> counting from center outwards
radius = 25

# Initial ball coordinates
x = screen_width/2
y = screen_height/2
angle = 0

# Inital ball velocity
vx = 150
vy = 100
omega = math.pi / 2

# Ball acceleration 
g = 1 

# Ball coefficient of restitution (bounciness)
e = 1

# Ball mass
mass = 1 

# Coeff of friction 
mu = 0.01

# Set the ball's rolling resistance force (in Newtons)
F_rolling_resistance = mu * mass * g  

#Ball's moment of intertia
I = (2/5) * mass * radius**2

torque = 100

#Angular acceleration 
alpha = torque / I 


# Set the ball's acceleration (in meters/second^2)
ax = F_rolling_resistance / mass
ay = ax 

slika = pg.image.load('line.png')
slika = pg.transform.scale(slika,(50,50))
slika = slika.convert_alpha()

# Game loop 
running = True
while running: 

    dt = 0.01
    screen.fill(background_color)

    #Rotation
    angle += omega * dt
    omega += alpha *dt


    x,y,vx,vy,ax,ay = fu.RK4_Movement(x,y,vx,vy,ax,ay,dt)
    
    vx,vy = fu.colision_bricks(x,y,radius,screen_width,screen_height,middle_blocks_left_point,sides_blocks_top_point,e,vx,vy)
    fu.colision_edge(x,y,radius,screen_height,screen_width)


    # Drawing blocks
    pg.draw.rect(screen, block_color, block_bottom, 0, 30)
    pg.draw.rect(screen, block_color, block_top, 0, 30)
    pg.draw.rect(screen, block_color, block_left, 0, 30)
    pg.draw.rect(screen, block_color, block_right, 0, 30)

    # Drawing ball kada ovo zakomentarisem vidi se polygon koji se rotira cilj je napraviti lopticu
    loptica = pg.draw.circle(screen, ball_color, (int(x), int(y)), radius)
    screen.blit(slika,loptica)
    
    # Block movement
    keys = pg.key.get_pressed()
    block_vertical_movement_speed = 250
    block_horiZontal_movement_speed = 250 * 1920/1080

    if keys[pg.K_LEFT]:
        if(middle_blocks_left_point > 50):
            middle_blocks_left_point -= block_horiZontal_movement_speed * dt

    if keys[pg.K_RIGHT]:
        if(middle_blocks_left_point < screen.get_width()-300):
            middle_blocks_left_point += block_horiZontal_movement_speed * dt 

    if keys[pg.K_UP]:
        if(sides_blocks_top_point > 50):
            sides_blocks_top_point -= block_vertical_movement_speed * dt

    if keys[pg.K_DOWN]:
        if(sides_blocks_top_point < screen.get_height()-300):
            sides_blocks_top_point += block_vertical_movement_speed * dt

    block_bottom[0] = middle_blocks_left_point
    block_top[0] = middle_blocks_left_point
    block_left[1] = sides_blocks_top_point
    block_right[1] = sides_blocks_top_point

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            running = False
            pg.quit()
    
    pg.display.update()