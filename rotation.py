import pygame
import math
import numpy as np 

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Ball Rotation with SAT")

# Set the ball properties
radius = 25
color = (255, 0, 0)  # Red

# Set the ball initial position and angle
x = 400
y = 300
angle = 0  # In radians

# Set the ball's velocity and angular velocity
vx = 200
vy = 100
omega = math.pi / 2  # In radians/second

# Set the time step
dt = 0.01

# Set the ball's mass (in kilograms)
mass = 1

# Set the ball's moment of inertia (assume a solid sphere)
I = (2/5) * mass * radius**2

# Set the ball's torque (in Newton*meters)
torque = 100

# Set the ball's angular acceleration (in radians/second^2)
alpha = torque / I

# Set the ball's mass (in kilograms)
mass = 1

# Set the ball's radius (in meters)
radius_m = 0.025  # 25 cm

# Set the gravitational acceleration (in meters/second^2)
g = 9.81


# Set the ball's coefficient of friction (rolling resistance)
mu = 0.01

# Set the ball's rolling resistance force (in Newtons)
F_rolling_resistance = mu * mass * g

# Set the ball's air resistance force (in Newtons)
rho = 1.2  # Density of air (in kilograms/meter^3)
A = np.pi * radius_m**2  # Cross-sectional area of the ball (in square meters)
C_d = 0.47  # Drag coefficient for a smooth sphere
F_air_resistance = 0.5 * rho * A * C_d * vx**2

# Set the ball's net force (in Newtons)
F_net = F_rolling_resistance + F_air_resistance

# Set the ball's acceleration (in meters/second^2)
ax = F_net / mass
ay = -g

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the ball's angle and angular velocity
    angle += omega*dt
    omega += alpha*dt

    # Update the ball's position and velocity using the SAT method
    vx += ax*dt
    vy += ay*dt
    x += vx*dt
    y += vy*dt

    # Rotate the ball's vertices around the center of the ball
    vertices = [(x + radius*math.cos(angle), y + radius*math.sin(angle)),
                (x + radius*math.cos(angle + 2*math.pi/3), y + radius*math.sin(angle + 2*math.pi/3)),
                (x + radius*math.cos(angle + 4*math.pi/3), y + radius*math.sin(angle + 4*math.pi/3))]

    # Clear the screen
    screen.fill((255, 255, 255))  # White

    # Draw the ball
    pygame.draw.polygon(screen, color, vertices)

    # Update the display
    pygame.display.flip()

    # Delay to achieve desired frame rate
    pygame.time.delay(int(dt*1000))

# Quit pygame
pygame.quit()

