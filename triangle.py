import config
import pygame
import math

class triangle_object:
    def __init__(self,position,vertices) -> None:
        # Initial triangle properties
        self.position = position
        self.vertices = vertices
        self.radius = config.radius
        self.color = config.DEFAULT_BALL_COLOR
        self.acceleration = 3
        self.space_vertices = list(map(lambda x: (x[0] + self.position[0], x[1] + self.position[1]), self.vertices))
        self.mass = 0.5
        self.inertia = self.mass*self.acceleration

        # Axis -> v's and a's
        self.ax = self.inertia / self.mass
        self.ay = self.ax
        self.dt = 0.02
        self.vx = 500   
        self.vy = -250

        self.angle = 0
        self.omega = math.pi / 2
        self.torque = 5
        self.alpha = self.torque / self.inertia
   
    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.space_vertices)

    def is_colliding_SAT(self, polygon,flag):
        for i in range(len(polygon.space_vertices)):
            v0 = polygon.space_vertices[i]
            v1 = polygon.space_vertices[(i + 1) % len(polygon.space_vertices)]
            edge_vector = [v1[0] - v0[0], v1[1] - v0[1]]
            normal = [ - edge_vector[1], edge_vector[0]]
            self_span = span_along_line(v0, normal, self)
            polygon_span = span_along_line(v0, normal, polygon)
            if self_span[0] > polygon_span[1] or self_span[1] < polygon_span[0]:
                return False 

        for i in range(len(self.space_vertices)):
            v0 = self.space_vertices[i]
            v1 = self.space_vertices[(i + 1) % len(self.space_vertices)]
            edge_vector = [v1[0] - v0[0], v1[1] - v0[1]]
            normal = [ - edge_vector[1], edge_vector[0]]
            self_span = span_along_line(v0, normal, self)
            polygon_span = span_along_line(v0, normal, polygon)
            if self_span[0] > polygon_span[1] or self_span[1] < polygon_span[0]:
                return False 
        return True

    def is_colliding_edge(self): 
        for i in range (len(self.space_vertices)): 
            if self.space_vertices[i][0] >= 1920 or self.space_vertices[i][0] <= 0 or self.space_vertices[i][1] >= 1080 or self.space_vertices[i][1] <= 0 : 
                return True

        return False

    def triangle_RK4_movement(self):
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
        self.position[0] = self.position[0] + (self.dt/6)*(vx1 + 2*vx2 + 2*vx3 + vx4)
        self.position[1] = self.position[1] + (self.dt/6)*(vy1 + 2*vy2 + 2*vy3 + vy4)

        #rotation movement
        self.angle +=self.omega*self.dt
        self.omega += self.alpha*self.dt
        
        self.space_vertices = [(self.position[0] + self.radius*math.cos(self.angle), self.position[1] + self.radius*math.sin(self.angle)),
                (self.position[0] + self.radius*math.cos(self.angle + 2*math.pi/3), self.position[1] + self.radius*math.sin(self.angle + 2*math.pi/3)),
                (self.position[0] + self.radius*math.cos(self.angle + 4*math.pi/3), self.position[1] + self.radius*math.sin(self.angle + 4*math.pi/3))]

def span_along_line(vertex, vector, shape):
    span = [math.inf, -math.inf]
    for v in shape.space_vertices:
        v_vector = [v[0] - vertex[0], v[1] - vertex[1]]
        d_p = dot_product(vector, v_vector)
        span[0] = min(span[0], d_p)
        span[1] = max(span[1], d_p)
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

            