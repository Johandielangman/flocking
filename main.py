# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~


from pygame.math import Vector2
import pygame
import random

from modules.boid import Boid
from constants import (
    CANVAS_WIDTH,
    WINDOW_TITLE,
    CANVAS_HEIGHT,
    COLOR_LIGHT_BLUE,
    GAME_FPS,
    NUM_BOIDS
)


def main_loop():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        size=(CANVAS_WIDTH, CANVAS_HEIGHT)
    )
    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption(WINDOW_TITLE)

    running: bool = True
    boids: list[Boid] = []
    for _ in range(NUM_BOIDS):
        pos_x = random.randint(0, CANVAS_WIDTH)
        pos_y = random.randint(0, CANVAS_HEIGHT)
        v_x = random.uniform(-2, 2)
        v_y = random.uniform(-2, 2)
        boid = Boid(
            position=Vector2(x=pos_x, y=pos_y),
            velocity=Vector2(x=v_x, y=v_y)
        )
        boids.append(boid)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(COLOR_LIGHT_BLUE)

        # =======================// DRAWING //======================= #

        for boid in boids:
            boid.flock(boids)
            boid.update()
            boid.draw(screen)

        # =========================================================== #
        pygame.display.flip()
        clock.tick(GAME_FPS)


if __name__ == "__main__":
    main_loop()
    pygame.quit()
