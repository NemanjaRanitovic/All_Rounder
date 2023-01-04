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

# Ball radius -> counting from center outwards
radius = 25

# Initial ball coordinates
x = screen_width/2
y = screen_height/2

# Inital ball velocity
vx = 150
vy = 100

# Ball acceleration 
g = 1 

# Ball coefficient of restitution (bounciness)
e = 1

# Ball mass
mass = 1 

# Coeff of friction 
mu = 0.1

# Set the ball's rolling resistance force (in Newtons)
F_rolling_resistance = mu * mass * g  

# Set the ball's acceleration (in meters/second^2)
ax = F_rolling_resistance / mass
ay = ax 

# Game loop 
running = True
while running: 

    dt = 0.01
    screen.fill(background_color)

    # RK4 Method for ball movement
    x1, y1, vx1, vy1 = x, y, vx, vy
    ax1, ay1 = ax, ay
    x2, y2, vx2, vy2 = x + 0.5*vx1*dt, y + 0.5*vy1*dt, vx + 0.5*ax1*dt, vy + 0.5*ay1*dt
    ax2, ay2 = ax, ay
    x3, y3, vx3, vy3 = x + 0.5*vx2*dt, y + 0.5*vy2*dt, vx + 0.5*ax2*dt, vy + 0.5*ay2*dt
    ax3, ay3 = ax, ay
    x4, y4, vx4, vy4 = x + vx3*dt, y + vy3*dt, vx + ax3*dt, vy + ay3*dt
    ax4, ay4 = ax, ay
    x = x + (dt/6)*(vx1 + 2*vx2 + 2*vx3 + vx4)
    y = y + (dt/6)*(vy1 + 2*vy2 + 2*vy3 + vy4)
    vx = vx + (dt/6)*(ax1 + 2*ax2 + 2*ax3 + ax4)
    vy = vy + (dt/6)*(ay1 + 2*ay2 + 2*ay3 + ay4)

    # TOP BLOCK
    if((x + radius >= 0 + middle_blocks_left_point and x + radius <= 0 + middle_blocks_left_point + 250) and (y - radius <= 50)):
        vx = e*vx
        vy = -e*vy

    # DOWN BLOCK
    if((x + radius >= 0 + middle_blocks_left_point and x + radius <= 0 + middle_blocks_left_point + 250) and (y + radius >= screen_height - 50)):
        vx = e*vx
        vy = -e*vy

    # LEFT BLOCK
    if((x - radius <= 50) and (y + radius >= 0 + sides_blocks_top_point and y + radius <= 0 + sides_blocks_top_point+250)): 
        vx = -e*vx
        vy = e*vy

    # RIGHT BLOCK
    if ((x + radius >= screen_width-50 ) and (y + radius >= 0 + sides_blocks_top_point and y + radius <= 0 + sides_blocks_top_point+250)):
        vx = -e*vx
        vy = e*vy
    
    # Bottom border detection
    if(y + radius >= screen_height):  
        pg.quit()

    # Top border detection
    if(y - radius <= 0):  
        pg.quit()

    # Left border detection
    if(x - radius <= 0):  
        pg.quit()
    
    # Right border detection
    if(x + radius >= screen_width):  
        pg.quit()

    # Drawing blocks
    pg.draw.rect(screen, block_color, block_bottom, 0, 30)
    pg.draw.rect(screen, block_color, block_top, 0, 30)
    pg.draw.rect(screen, block_color, block_left, 0, 30)
    pg.draw.rect(screen, block_color, block_right, 0, 30)

    # Drawing ball
    pg.draw.circle(screen, ball_color, (int(x), int(y)), radius)

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