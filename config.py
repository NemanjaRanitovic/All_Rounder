import pygame
SURFACE_SIZE = (1920, 1080)
FILL_COLOR = (0, 0, 0)
FPS  = 60
DEFAULT_BLOCK_COLOR = (250, 226, 158)
DEFAULT_BALL_COLOR = (250, 226, 158)
POLYGON_FILL_ALPHA = 120    
MOVEMENT_MULTIPLIER = 10
HIT_CONSTANT = 6
CHANGE_DIR = 450
TEXT_COLOR = (250, 226, 158)
dir_speed = 3
radius = 15

start_screen = pygame.image.load("Images/start-cover.png")
background_screen = pygame.image.load("Images/Background_Design.jpg")
background_screen = pygame.transform.scale(background_screen,SURFACE_SIZE)
block_image_horizontal = pygame.image.load("Images/Horizontal_Block_Design.jpg")
block_image_vertical = pygame.image.load("Images/Vertical_Block_Design.jpg")

#Pescana tematika
background_screen1 = pygame.image.load("Images/Background_Design.jpg")
background_screen1 = pygame.transform.scale(background_screen1,SURFACE_SIZE)
block_image_horizontal1 = pygame.image.load("Images/Horizontal_Block_Design.jpg")
block_image_vertical1 = pygame.image.load("Images/Vertical_Block_Design.jpg")

#Vatrena tematika
background_screen2 = pygame.image.load("Images/Fire_Block_Design.jpg")
background_screen2 = pygame.transform.scale(background_screen2,SURFACE_SIZE)
block_image_horizontal2 = pygame.image.load("Images/Fire_Horizontal_Block_Design.jpg")
block_image_vertical2 = pygame.image.load("Images/Fire_Vertical_Block_Design.jpg")

#Ledena tematika
background_screen3 = pygame.image.load("Images/Ice_Background_Design.jpg")
#background_screen3 = pygame.transform.scale(background_screen3,SURFACE_SIZE)
block_image_horizontal3 = pygame.image.load("Images/Ice_Horizontal_Block_Design.jpg")
block_image_vertical3 = pygame.image.load("Images/Ice_Vertical_Block_Design.jpg")

#Atina
background_screen4 = pygame.image.load("Images/Athens_Background.jpg")
#background_screen4 = pygame.transform.scale(background_screen4,SURFACE_SIZE)
block_image_horizontal4 = pygame.image.load("Images/Athens_Horizontal_Block_Design.png")
block_image_vertical4 = pygame.image.load("Images/Athens_Vertical_Block_Design.png")

#Paris
background_screen5 = pygame.image.load("Images/Paris_Background.jpg")
#background_screen5 = pygame.transform.scale(background_screen5,SURFACE_SIZE)
block_image_horizontal5 = pygame.image.load("Images/Paris_Horizontal_Block_Design.png")
block_image_vertical5 = pygame.image.load("Images/Paris_Vertical_Block_Design.png")
 
#Stonegendge
background_screen6 = pygame.image.load("Images/Stonegendge_Background_Design.jpg")
#background_screen6 = pygame.transform.scale(background_screen6,SURFACE_SIZE)
block_image_horizontal6 = pygame.image.load("Images/Stonegendge_Horizontal_Block_Design.png")
block_image_vertical6 = pygame.image.load("Images/Stonegendge_Vertical_Block_Design.png")

#England
background_screen7 = pygame.image.load("Images/England_Background_Design.jpg")
#background_screen7 = pygame.transform.scale(background_screen7,SURFACE_SIZE)
block_image_horizontal7 = pygame.image.load("Images/England_Horizontal_Block_Design.png")
block_image_vertical7 = pygame.image.load("Images/England_Vertical_Block_Design.png")


#Italia
background_screen8 = pygame.image.load("Images/Italia_Background_Design.jpg")
#background_screen8 = pygame.transform.scale(background_screen8,SURFACE_SIZE)
block_image_horizontal8 = pygame.image.load("Images/Italia_Horizontal_Block_Design.png")
block_image_vertical8 = pygame.image.load("Images/Italia_Vertical_Block_Design.png")


#Rusia
background_screen9 = pygame.image.load("Images/Russia_Background_Design.jpg")
#background_screen9 = pygame.transform.scale(background_screen9,SURFACE_SIZE)
block_image_horizontal9 = pygame.image.load("Images/Russia_Horizontal_Block_Design.png")
block_image_vertical9 = pygame.image.load("Images/Russia_Vertical_Block_Design.png")

error = pygame.image.load("Images/Vertical_block_design.jpg")
error = pygame.transform.scale(error,(1,1))

