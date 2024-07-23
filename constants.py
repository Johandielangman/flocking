# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import pygame
import os
from dotenv import load_dotenv
load_dotenv()

# =======================// GAME SETTINGS //======================= #

WINDOW_TITLE: str = os.getenv('WINDOW_TITLE', 'Flocking')
CANVAS_WIDTH: int = int(os.getenv('CANVAS_WIDTH', 1280))
CANVAS_HEIGHT: int = int(os.getenv('CANVAS_HEIGHT', 720))

SPRITE_WIDTH: int = int(os.getenv('SPRITE_WIDTH', 40))
SPRITE_HEIGHT: int = int(os.getenv('SPRITE_HEIGHT', 40))

GAME_FPS: int = int(os.getenv('GAME_FPS', 30))
DEBUG: bool = bool(os.getenv('DEBUG', False))

# =======================// STYLE //======================= #

COLOR_DARK_GREY: str = "#646250"
COLOR_LIGHT_BLUE: str = "#66d9ef"
COLOR_GREEN: tuple[int, int, int] = (0, 255, 0)
COLOR_RED: tuple[int, int, int] = (255, 0, 0)

# =======================// BOID SETTINGS //======================= #

NUM_BOIDS: int = int(os.getenv('NUM_BOIDS', 30))
SAC_WEIGHTS: tuple[float, float, float] = (
    1,  # Separation
    0.9,  # Alignment
    1.05   # Cohesion
)
PERCEPTION_RADIUS: int = int(os.getenv('PERCEPTION_RADIUS', 100))

MAX_BOID_SPEED: int = int(os.getenv('MAX_BOID_SPEED', 7))
MIN_BOID_SPEED: int = int(os.getenv('MIN_BOID_SPEED', 5))

MAX_BOID_ACCELERATION: float = float(os.getenv('MAX_BOID_ACCELERATION', 0.2))

# =======================// PATHS //======================= #

RESOURCES_FOLDER_PATH: str = os.path.join(os.path.dirname(__file__), 'resources')
BIRD_IMAGE_PATH: str = os.path.join(RESOURCES_FOLDER_PATH, 'bird.bmp')


def load_image_and_scale(
    image_path: str,
    scale: tuple[int, int] = (SPRITE_WIDTH, SPRITE_HEIGHT)
) -> pygame.Surface:
    return pygame.transform.scale(
        surface=pygame.image.load(
            image_path
        ).convert_alpha(),
        size=scale
    )
