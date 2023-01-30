import pygame as pg

def colision_bricks(x,y,radius,screen_width,screen_height,middle_blocks_left_point,sides_blocks_top_point,e,vx,vy):
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
    
    return vx,vy
         
def colision_edge(x,y,radius,screen_height,screen_width):
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

def RK4_Movement(x,y,vx,vy,ax,ay,dt):
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

    return x,y,vx,vy,ax,ay