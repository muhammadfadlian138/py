import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))

x = 200
y = 50
speed = 0
gravity = 0.01

running = True

while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left click")
                # Reset the ball
                y = 50
                speed = 0

            elif event.button == 3:
                print("Right click")
                pygame.quit()

    speed = speed + gravity
    y = y + speed

    pygame.draw.circle(screen, "red", (x, y), 30)

    pygame.display.flip()

pygame.quit()