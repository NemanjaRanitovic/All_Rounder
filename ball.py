import config
import pygame
import math 

class ball_object:
    def __init__(self,position) -> None:
        # Inital ball properties 
        self.position = position
        self.radius = config.radius
        self.space_vertices = self.position
        self.color = config.DEFAULT_BALL_COLOR
        self.mass = 1
        self.acceleration = 1
        # Moment of intertia 
        self.inertia = (2/5)*self.mass*self.acceleration


        # Axis -> v's and a's
        self.ax = self.inertia / self.mass
        self.ay = self.ax
        self.dt = 0.025
        self.vx = 300  
        self.vy = 500

        # Angluar speed
        self.omega = math.pi / 2 
        # Rotational force
        self.torque = 100 
        # Angular acceleration 
        self.alpha = self.inertia / self.torque 
        # Angle
        self.angle = 0 

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,center = self.position,radius = self.radius)

    def ball_RK4_movement(self):
       # Izvod brzine je ubrzanje
        # K1 (X,Y) -> dt(f(y1, t1)) (dt->korak, f->izvod, y1->vx,vy, t1->pocetni trenutak)
        vx1, vy1 = self.vx, self.vy
        ax1, ay1 = self.ax, self.ay
        # K2 (X,Y) -> dt(f(y1, k1/2, t1 + dt/2)) (dt->korak, f->izvod, y1->vx,vy, t1->pocetni trenutak)
        vx2, vy2 = self.vx + 0.5*ax1*self.dt, self.vy + 0.5*ay1*self.dt
        ax2, ay2 = self.ax, self.ay
        # K3 (X,Y) -> dt(f(y1, k2/2, t1 + dt/2)) (dt->korak, f->izvod, y1->vx,vy, t1->pocetni trenutak)
        vx3, vy3 = self.vx + 0.5*ax2*self.dt, self.vy + 0.5*ay2*self.dt
        ax3, ay3 = self.ax, self.ay
        # K4 (X,Y) ->  -> dt(f(y1+k3, t1+h)) (dt->korak, f->izvod, y1->vx,vy, t1->pocetni trenutak)
        vx4, vy4 =self.vx + ax3*self.dt, self.vy + ay3*self.dt

        # Update positions
        self.position[0] = self.position[0] + (self.dt/6)*(vx1 + 2*vx2 + 2*vx3 + vx4)
        self.position[1] = self.position[1] + (self.dt/6)*(vy1 + 2*vy2 + 2*vy3 + vy4)

        self.omega += self.alpha*self.dt
        self.angle += self.omega*self.dt
        if(self.angle > 100):
            self.color = config.DEFAULT_BALL_COLOR
            self.omega = math.pi / 2
            self.dt = 0.025
        if(self.angle > 15):
            self.color = (255,255,0)

    def is_colliding_edge(self):
        if self.position[0] + self.radius >= 1920 or self.position[0] - self.radius <= 0 or self.position[1] + self.radius >= 1080 or self.position[1] - self.radius <= 0 : 
                return True
        return False

    def is_colliding_SAT(self, polygon,flag):
        for i in range(len(polygon.space_vertices)):
            v0 = polygon.space_vertices[i]
            v1 = polygon.space_vertices[(i + 1) % len(polygon.space_vertices)]
            edge_vector = [v1[0] - v0[0], v1[1] - v0[1]]
            normal = [ - edge_vector[1], edge_vector[0]]

            self_span = span_along_line_1_vertex(v0, normal, self,flag)
            polygon_span = span_along_line(v0, normal, polygon)
            if self_span[0] > polygon_span[1] or self_span[1] < polygon_span[0]:
                return False 

        
        v0 = self.space_vertices
        self_span = span_along_line_1_vertex(v0, normal, self,flag)
        polygon_span = span_along_line(v0, normal, polygon)
        if self_span[0] > polygon_span[1] or self_span[1] < polygon_span[0]:
            return False
        return True
        

def span_along_line(vertex, vector, shape):
    span = [math.inf, -math.inf]
    for v in shape.space_vertices:
        v_vector = [v[0] - vertex[0], v[1] - vertex[1]]
        d_p = dot_product(vector, v_vector)
        span[0] = min(span[0], d_p)
        span[1] = max(span[1], d_p)
    return span

def span_along_line_1_vertex(vertex, vector, shape,flag):
    span = [math.inf, -math.inf]
    v_vector = [shape.space_vertices[0] + config.radius * flag - vertex[0], shape.space_vertices[1] - config.radius * flag - vertex[1]]
    d_p = dot_product(vector, v_vector)
    span[0] =  d_p
    span[1] =  d_p
    return span

def dot_product(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1]

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

