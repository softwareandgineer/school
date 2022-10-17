# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
sunx = 75
suny = 75
sunr = 50
moonx = 0 - WIDTH
sky_color_r = 25
sky_color_g = 25
sky_color_b = 112
leaves_color = 100
grass_color = 75
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    sunx += 2
    moonx += 2
    if sunx > WIDTH + 100:
        sunx = (WIDTH * -1) - 50
    if moonx > WIDTH + 100:
        moonx = (WIDTH * -1) - 50
    if WIDTH / 2 <= sunx <= WIDTH and sky_color_r > 2:
        sky_color_r -= 1
        sky_color_g -= 1
        sky_color_b -= 1
        leaves_color -= 1
        grass_color -= 1
    if 0 <= sunx <= WIDTH / 2:
        sky_color_r += 1
        sky_color_g += 1
        sky_color_b += 1
        leaves_color += 1
        grass_color += 1


    # DRAWING
    screen.fill((sky_color_r, sky_color_g, sky_color_b))  # always the first drawing command

    # grass
    pygame.draw.rect(screen, (0, grass_color, 0), (0, 400, WIDTH, 100))

    # sun
    pygame.draw.circle(screen, (255, 200, 0), (sunx, suny), sunr + 5)
    pygame.draw.circle(screen, (255, 255, 0), (sunx, suny), sunr)
    pygame.draw.circle(screen, (0, 0, 0), (sunx - 15, suny - 10), sunr - 45)
    pygame.draw.circle(screen, (0, 0, 0), (sunx + 15, suny - 10), sunr - 45)
    pygame.draw.circle(screen, (0, 0, 0), (sunx, suny + 15), sunr - 35)
    pygame.draw.rect(screen, (255, 255, 0), (sunx - 15, suny, sunr - 20, sunr - 35))

    # moon
    pygame.draw.circle(screen, (255, 255, 255), (moonx, suny), sunr - 15)
    pygame.draw.circle(screen, (0, 0, 0), (moonx - 15, suny - 10), sunr - 45)
    pygame.draw.circle(screen, (0, 0, 0), (moonx + 15, suny - 10), sunr - 45)
    pygame.draw.circle(screen, (0, 0, 0), (moonx, suny + 15), sunr - 35)
    pygame.draw.rect(screen, (255, 255, 255), (moonx - 15, suny + 15, sunr - 20, sunr - 35))

    # tree
    pygame.draw.rect(screen, (100, 75, 50), (WIDTH / 2 - 35, 250, 70, 200))
    pygame.draw.circle(screen, (0, leaves_color, 0), (WIDTH / 2, suny + 100), 70)
    pygame.draw.circle(screen, (0, leaves_color, 0), ((WIDTH / 2) - 50, suny + 175), 70)
    pygame.draw.circle(screen, (0, leaves_color, 0), ((WIDTH / 2) + 50, suny + 175), 70)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
