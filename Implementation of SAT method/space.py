import config 
from block import shape_object
from triangle import triangle_object
from ball import ball_object

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
    def draw(self, surface):
        for shape in self.shapes:
            shape.draw(surface)

    def update_variables(self,hit_counter,text_counter):
        triangle_or_ball = self.shapes[0]
        for i in range(1,len(self.shapes)):
            colided_shape = self.shapes[i]
            if triangle_or_ball.is_colliding(colided_shape):
                # Left block
                if i == 1:
                    triangle_or_ball.vx *= -1
                    print("Left")
                # Right block
                elif i == 2:
                    triangle_or_ball.vx *= -1
                    print("Right")
                # Down block
                elif i == 3:
                    triangle_or_ball.vy *= -1
                    print("Down")
                # Top block
                elif i == 4:
                    triangle_or_ball.vy *= -1
                    print("top")
                else:
                    triangle_or_ball.vx*=-1
                    triangle_or_ball.vy*=-1
                    del self.shapes[5]
                print("Doslo je do kolizije")
                hit_counter+=1
                text_counter+=1
                # Mozemo da menjamo velocity ovde i smer i sve OSTALO STO JEBENO TREBA 
                # bla bla bla
        return hit_counter,text_counter