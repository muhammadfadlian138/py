from vpython import *

# Ground
ground = box(
    pos=vector(0, 0, 0),
    size=vector(20, 0.1, 20)
)

# Ball
ball = sphere(
    pos=vector(0, 1, 0),
    radius=0.3,
    color=color.red
)

# Initial velocity
velocity = vector(5, 8, 3)

# Gravity
gravity = vector(0, -9.8, 0)

# Time step
dt = 0.01

while ball.pos.y > 0:
    rate(100)

    # Physics
    velocity = velocity + gravity * dt
    ball.pos = ball.pos + velocity * dt