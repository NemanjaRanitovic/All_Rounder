import config 
from block import shape_object
from triangle import triangle_object
from ball import ball_object
import time
import pygame

class space_object: 
    def __init__(self) -> None: 
        # Making a list of created objects 
        self.shapes = []
    
    # Function for Blocks creation 
    def add_block(self, position, vertices): 
        new_block = shape_object(position,  vertices)
        # Add to list
        self.shapes.append(new_block)
        return new_block
    
    def add_triangle(self,position,vertices):
        new_triangle = triangle_object(position,vertices)
        self.shapes.append(new_triangle)
        return new_triangle

    def add_ball(self,position):
        new_ball = ball_object(position)
        self.shapes.append(new_ball)
        return new_ball

    # Draw every block 
    def draw(self, surface,block_image_horizontal,block_image_vertical,error):
        for i in range(len(self.shapes)):
            if i == 0:
                self.shapes[i].draw(surface)
            elif(i == 1 or i == 2):
                self.shapes[i].draw(surface,block_image_vertical)
            elif(i == 3 or i == 4):
                self.shapes[i].draw(surface,block_image_horizontal)
            else:
                self.shapes[i].draw(surface,error)

    def update_variables(self,hit_counter,text_counter,hit_sound):
        triangle_or_ball = self.shapes[0]
        for i in range(1,len(self.shapes)):
            colided_shape = self.shapes[i]
            if i % 2 == 0:
                flag = 1
            else:
                flag = -1
            if triangle_or_ball.is_colliding_SAT(colided_shape,flag):
                if(triangle_or_ball.vx > 0 ):
                    flag2 = 1
                else:
                    flag2 = -1
                if(triangle_or_ball.vy > 0 ):
                    flag2 = 1
                if(abs(triangle_or_ball.vx) > 700):
                    triangle_or_ball.vx = 500
                if(abs(triangle_or_ball.vy) > 700):
                    triangle_or_ball.vy = -250
                else:
                    flag2 = -1
                # Left block
                
                if i == 1:
                    triangle_or_ball.vx *= -1
                    print("Left")
                   # triangle_or_ball.vy*=triangle_or_ball.angle * flag2
                    triangle_or_ball.vy += 10 * flag2
                    triangle_or_ball.dt *= 1.001
                # Right block
                elif i == 2:
                    triangle_or_ball.vx *= -1
                    print("Right")
                   
                    triangle_or_ball.vy += 10 * flag2
                    triangle_or_ball.dt *= 1.001
                # Down block
                elif i == 3:
                    triangle_or_ball.vy *= -1
                    print("Down")
                   
                    triangle_or_ball.vx += 10 * flag2
                    triangle_or_ball.dt *= 1.001
                # Top block
                elif i == 4:
                    triangle_or_ball.vy *= -1
                   
                    triangle_or_ball.vx += 10 * flag2
                    print(triangle_or_ball.angle)
                    triangle_or_ball.dt *= 1.001
                    print("top")
                else:
                    triangle_or_ball.vx*=-1
                    triangle_or_ball.vy*=-1
                
                    triangle_or_ball.dt += 0.001
                    del self.shapes[5]
                print("Doslo je do kolizije")
                hit_counter+=1
                text_counter+=1
                pygame.mixer.Sound.play(hit_sound)
        return hit_counter,text_counter