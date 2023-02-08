import config
import pygame
import math

class shape_object: 
    # Constructor of the block 
    def __init__(self, position, vertices) -> None: 
        # Block is positioned, and vertices are relative to that pos
        self.vertices = vertices
        self.position = position
        self.color = config.DEFAULT_BLOCK_COLOR
        # Positional vectors for every vertex 
        self.space_vertices = list(map(lambda x: (x[0] + self.position[0], x[1] + self.position[1]), self.vertices))
        self.centralize_polygon_position()
        self.velocity = 0

    def centralize_polygon_position(self):
        self.position = get_centroid(self.space_vertices)
        self.vertices = []
        for vertex in self.space_vertices:
            self.vertices.append(calc_vector(self.position, vertex))

    def move_up_down(self,direction):
        self.position[1] += config.MOVEMENT_MULTIPLIER * direction
        self.velocity = config.MOVEMENT_MULTIPLIER
        self.update_space_vertices()

    def move_left_right(self,direction):
        self.position[0] += config.MOVEMENT_MULTIPLIER * direction
        self.velocity = config.MOVEMENT_MULTIPLIER * direction
        self.update_space_vertices()

    def update_space_vertices(self):
            self.space_vertices = list(map(lambda x: (x[0] + self.position[0], x[1] + self.position[1]), self.vertices))

    def draw(self,surface,block_image_horizontal):
        pygame.draw.polygon(surface, self.color, self.space_vertices)
        surface.blit(block_image_horizontal,self.space_vertices[0])
        
def calc_vector(p1, p2):
    # Calculating vector
    return [p2[0] - p1[0], p2[1] - p1[1]]

def get_centroid(vertices):
        x = y = 0
        area = 0
        n = len(vertices)
        for i in range(n):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % n]
            tmp = p1[0] * p2[1] - p2[0] * p1[1]
            area += tmp
            x += (p1[0] + p2[0]) * tmp
            y += (p1[1] + p2[1]) * tmp
        
        return [x / (3*area), y / (3*area)] 

    