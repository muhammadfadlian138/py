import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.pensize(3)
t.color("darkgray", "lightgray")

# Start filling the gear shape
t.begin_fill()

# Draw the main outer circle base
t.circle(80)
t.end_fill()

# Draw the gear teeth
num_teeth = 12
tooth_length = 20
tooth_width = 15

t.penup()
t.goto(0, 80)  # Move to the edge of the circle radius (80)
t.setheading(0)
t.pendown()

for _ in range(num_teeth):
  t.forward(tooth_width / 2)
  t.left(90)
  t.forward(tooth_length)
  t.right(90)
  t.forward(tooth_width)
  t.right(90)
  t.forward(tooth_length)
  t.left(90)
  t.forward(tooth_width / 2)
  t.left(360 / num_teeth)

# Draw the inner center hole of the gear
t.penup()
t.goto(0, 25)
t.setheading(0)
t.pendown()
t.color("darkgray", "white")
t.begin_fill()
t.circle(25)
t.end_fill()

# Hide turtle and finish
t.hideturtle()
turtle.done()
