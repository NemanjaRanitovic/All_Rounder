import pygame 
import config 
from space import space_object 
import random
from block import get_centroid
import time
from pygame import mixer

pygame.init()
mixer.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(config.SURFACE_SIZE)
surface = pygame.Surface(config.SURFACE_SIZE)
screen = pygame.display.set_mode((1920,1080)) 
space = space_object()

miss_sound = pygame.mixer.Sound("sounds/Miss.wav")
hit_sound = pygame.mixer.Sound("sounds/Hit_snap_sound.wav")
music = pygame.mixer.music.load("sounds/Allrounder_beat_LOOP_12min.mp3")
pygame.mixer.music.play(1)

pygame.display.set_caption('All Arrounder 2D')
start_screen = config.start_screen
background_screen = config.background_screen
#background_screen = pygame.transform.scale(background_screen,config.SURFACE_SIZE)
block_image_horizontal = config.block_image_horizontal
block_image_vertical = config.block_image_vertical
def start_menu():
    run = True
    while run:
        keys = pygame.key.get_pressed()
        pygame.display.update()
        # Displays the start screen picture
        screen.blit(config.start_screen, (0, 0))

        if keys[pygame.K_SPACE]:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        clock.tick(60)

# Set game icon 
icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)
# Adding the triangle
#trougao = space.add_triangle([960,540],[[-25,-25],[25,-25],[12.5,12.5]])

# Adding the ball
lopta = space.add_ball([960,540])

# Adding the blocks 
block_left =  space.add_block([25,540],[[-25,-125],[25,-125],[25,125],[-25,125]])
block_right = space.add_block([1895,540],[[-25,-125],[25,-125],[25,125],[-25,125]])
block_down =  space.add_block([960,1055],[[-125,-25],[125,-25],[125,25],[-125,25]])
block_up =    space.add_block([960,25],[[-125,-25],[125,-25],[125,25],[-125,25]])

# Counter display
hit_counter = 0
text_counter = 0
theme_counter = 0
font = pygame.font.Font('Tanker-Regular.otf', 96)
text = font.render(str(text_counter), True, config.TEXT_COLOR)
textRect = text.get_rect()
textRect.center = (1920 // 2, 1080 // 2)
running = True 
pressed = {'down':False, 'up':False, 'left':False, 'right':False}

def generateTriangle(positions):
    #tacka 1 (x,y)
    positions[0][0] = random.randint(200,520)
    positions[0][1] = random.randint(200,300)

    #tacka 2 (x,y)
    positions[1][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    positions[1][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]

    #tacka 3(x,y)
    positions[2][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    positions[2][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]


    if(abs(positions[0][0] - positions[1][0]) < 100):
        positions[1][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    if(abs(positions[0][1] - positions[1][1]) < 100):
        positions[1][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]

    if(abs(positions[1][0] - positions[2][0]) < 100):
        positions[2][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    if(abs(positions[1][1] - positions[2][1]) < 100):
        positions[2][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]

    if(abs(positions[0][0] - positions[2][0]) < 100):
        positions[2][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    if(abs(positions[0][1] - positions[2][1]) < 100):
        positions[2][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]

    if(abs(positions[0][0] - positions[2][0]) > 500):
        positions[2][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][0]
    if(abs(positions[0][1] - positions[2][1]) > 500):
        positions[2][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[0][1]

    if(abs(positions[0][0] - positions[1][0]) > 500):
        positions[2][0] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[1][0]
    if(abs(positions[0][1] - positions[1][1]) > 500):
        positions[2][1] = random.randint(-config.CHANGE_DIR,config.CHANGE_DIR)+positions[1][1]

    return positions
  
new_vertices = [[0,0],[0,0],[0,0]]

start_menu()
while running:
    clock.tick(config.FPS)
    surface.fill(config.FILL_COLOR)
    text = font.render(str(text_counter), True, config.TEXT_COLOR)
    surface.blit(background_screen,(0,0))
    surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pressed['down'] = True
            if event.key == pygame.K_UP:
                pressed['up'] = True
            if event.key == pygame.K_LEFT:
                pressed['left'] = True
            if event.key == pygame.K_RIGHT:
                pressed['right'] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressed['down'] = False
            if event.key == pygame.K_UP:
                pressed['up'] = False
            if event.key == pygame.K_LEFT:
                pressed['left'] = False
            if event.key == pygame.K_RIGHT:
                pressed['right'] = False
        
    if pressed['up']:
        if(block_left.position[1]-152 >= 50):
            block_left.move_up_down(-config.dir_speed)
            block_right.move_up_down(-config.dir_speed)
    if pressed['down']:
        if(block_left.position[1]+152 <= 1030):
            block_left.move_up_down(config.dir_speed)
            block_right.move_up_down(config.dir_speed)
    if pressed['left']:
        if(block_down.position[0]-152 >= 50):
            block_up.move_left_right(-config.dir_speed)
            block_down.move_left_right(-config.dir_speed) 
    if pressed['right']:
        if(block_down.position[0]+152 <= 1870):
            block_up.move_left_right(config.dir_speed)
            block_down.move_left_right(config.dir_speed) 

    if(hit_counter >= config.HIT_CONSTANT and len(space.shapes) == 5):
        new_vertices = generateTriangle(new_vertices)
        hit_counter = 0
        new_position = get_centroid(new_vertices)
        space.add_block(new_position,new_vertices)
        if(theme_counter == 0):
            background_screen = config.background_screen1
            block_image_vertical = config.block_image_vertical1
            block_image_horizontal = config.block_image_horizontal1
        elif(theme_counter == 1):
            background_screen = config.background_screen2
            block_image_vertical = config.block_image_vertical2
            block_image_horizontal = config.block_image_horizontal2
        elif(theme_counter == 2):
            background_screen = config.background_screen3
            block_image_vertical = config.block_image_vertical3
            block_image_horizontal = config.block_image_horizontal3
        elif(theme_counter == 3):
            background_screen = config.background_screen4
            block_image_vertical = config.block_image_vertical4
            block_image_horizontal = config.block_image_horizontal4
        elif(theme_counter == 4):
            background_screen = config.background_screen5
            block_image_vertical = config.block_image_vertical5
            block_image_horizontal = config.block_image_horizontal5
        elif(theme_counter == 5):
            background_screen = config.background_screen6
            block_image_vertical = config.block_image_vertical6
            block_image_horizontal = config.block_image_horizontal6
        elif(theme_counter == 6):
            background_screen = config.background_screen7
            block_image_vertical = config.block_image_vertical7
            block_image_horizontal = config.block_image_horizontal7
        elif(theme_counter == 7):
            background_screen = config.background_screen8
            block_image_vertical = config.block_image_vertical8
            block_image_horizontal = config.block_image_horizontal8
        elif(theme_counter == 8):
            background_screen = config.background_screen9
            block_image_vertical = config.block_image_vertical9
            block_image_horizontal = config.block_image_horizontal9
        if(theme_counter == 8):
            theme_counter = 0
        else:
            theme_counter+=1


    # Movement through RK4 method 
    #trougao.triangle_RK4_movement()
    lopta.ball_RK4_movement()
                 
    # Edge detection -> Game quit
    '''if trougao.is_colliding_edge():
        pygame.mixer.Sound.play(miss_sound)
        time.sleep(0.5) 
        pygame.quit()'''

    if lopta.is_colliding_edge():
        pygame.mixer.Sound.play(miss_sound)
        time.sleep(0.5)
        pygame.quit()
        
    hit_counter,text_counter = space.update_variables(hit_counter,text_counter,hit_sound)
    space.draw(surface,block_image_horizontal,block_image_vertical,config.error)
    window.blit(background_screen,(0,0))
    window.blit(surface,(0,0))
    pygame.display.update()
