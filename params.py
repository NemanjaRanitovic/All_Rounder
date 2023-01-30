import pygame as pg
import math

# Initialize the screen 
screen_width = 1920
screen_height = 1080 

# Initialize the colors
background_color = (20, 20, 20)
ball_color = (255, 0, 0)
block_color = (77, 255, 0)
text_color = (38, 38, 38)

# Blocks (left, top, width, height) - on a 1920x1080 plane
middle_blocks_left_point = screen_width/2 - 250/2
sides_blocks_top_point = screen_height/2 - 250/2