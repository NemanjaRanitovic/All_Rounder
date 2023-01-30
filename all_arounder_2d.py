import pygame as pg 
import numpy as np 
from pygame.locals import *
import math
import funkcije as fu
import params as par

# Initialize the game 
pg.init()

screen = pg.display.set_mode((par.screen_width, par.screen_height))
pg.display.set_caption('all-arounder')

# Initialize the clock 
clock = pg.time.Clock()

block_bottom = pg.Rect(par.middle_blocks_left_point, par.screen_height-50, 250, 50)
block_top = pg.Rect(par.middle_blocks_left_point, 0, 250, 50)
block_left = pg.Rect(0, par.sides_blocks_top_point, 50, 250)
block_right = pg.Rect(par.screen_width-50, par.sides_blocks_top_point, 50, 250)

# Ball radius -> counting from center outwards
radius = 25

# Initial ball coordinates
x = par.screen_width/2
y = par.screen_height/2
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

line_image = pg.image.load('line.png')
line_image = pg.transform.scale(line_image,(50,50))
line_image = line_image.convert_alpha()

hit_counter = 0
flip = 1
positions = [[0,0],[0,0],[0,0]]
# Game loop 
running = True
while running: 

    dt = 0.005
    screen.fill(par.background_color)

    #Rotation
    angle += omega * dt
    omega += alpha *dt

    x,y,vx,vy,ax,ay = fu.RK4_Movement(x,y,vx,vy,ax,ay,dt)
    vx,vy,hit_counter = fu.colision_bricks(x,y,radius,par.screen_width,par.screen_height,par.middle_blocks_left_point,par.sides_blocks_top_point,e,vx,vy,hit_counter)
    fu.colision_edge(x,y,radius,par.screen_height,par.screen_width)

    # Drawing blocks
    pg.draw.rect(screen, par.block_color, block_bottom, 0, 30)
    pg.draw.rect(screen, par.block_color, block_top, 0, 30)
    pg.draw.rect(screen, par.block_color, block_left, 0, 30)
    pg.draw.rect(screen, par.block_color, block_right, 0, 30)

    loptica = pg.draw.circle(screen, par.ball_color, (int(x), int(y)), radius)
    fu.blitRotateCenter(screen,line_image,(x,y),-angle/dt)

    
    if(hit_counter == 6):
        positions = fu.generateTriangle(positions)
        hit_counter = 0

    
    pg.draw.polygon(screen,par.block_color,positions)

    # Block movement
    keys = pg.key.get_pressed()
    block_vertical_movement_speed = 250
    block_horiZontal_movement_speed = 250 * 1920/1080

    if keys[pg.K_LEFT]:
        if( par.middle_blocks_left_point > 50):
            par.middle_blocks_left_point -= block_horiZontal_movement_speed * dt

    if keys[pg.K_RIGHT]:
        if( par.middle_blocks_left_point < screen.get_width()-300):
            par.middle_blocks_left_point += block_horiZontal_movement_speed * dt 

    if keys[pg.K_UP]:
        if( par.sides_blocks_top_point > 50):
            par.sides_blocks_top_point -= block_vertical_movement_speed * dt

    if keys[pg.K_DOWN]:
        if( par.sides_blocks_top_point < screen.get_height()-300):
            par.sides_blocks_top_point += block_vertical_movement_speed * dt

    block_bottom[0] = par.middle_blocks_left_point
    block_top[0] =    par.middle_blocks_left_point
    block_left[1] =   par.sides_blocks_top_point
    block_right[1] =  par.sides_blocks_top_point

    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            running = False
            pg.quit()
    
    pg.display.update()