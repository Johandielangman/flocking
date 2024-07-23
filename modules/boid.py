# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
#      /\_/\
#     ( o.o )
#      > ^ <
#
# Author: Johan Hanekom
# Date: July 2024
# ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~

import math
import pygame
from pygame.math import Vector2
from constants import (
    MAX_BOID_ACCELERATION,
    PERCEPTION_RADIUS,
    BIRD_IMAGE_PATH,
    MAX_BOID_SPEED,
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    COLOR_GREEN,
    SAC_WEIGHTS,
    COLOR_RED,
    DEBUG,
    load_image_and_scale
)


class Boid:
    def __init__(
        self,
        position: Vector2,
        velocity: Vector2,
        perception: int = PERCEPTION_RADIUS,
        sac_weights: tuple[float, float, float] = SAC_WEIGHTS,
        max_acceleration: float = MAX_BOID_ACCELERATION,
        max_speed: int = MAX_BOID_SPEED,
        enable_edge_collision: bool = False,
        show_hitbox: bool = DEBUG,
        show_vectors: bool = DEBUG
    ):
        self.position: Vector2 = position
        self.velocity: Vector2 = velocity
        self.acceleration: Vector2 = Vector2(0, 0)
        self.max_acceleration: float = max_acceleration
        self.max_speed: int = max_speed
        self.enable_edge_collision: bool = enable_edge_collision
        self.show_hitbox: bool = show_hitbox
        self.show_vectors: bool = show_vectors
        self.angle: float = 0
        self.w_s, self.w_a, self.w_c = sac_weights
        self.perception: int = perception

        self.original_image: pygame.Surface = load_image_and_scale(BIRD_IMAGE_PATH)
        self.image: pygame.Surface = self.original_image.copy()
        self.rect: pygame.Rect = self.image.get_rect(center=self.position)
        self.update_rect_and_rotation()

    def visible(self, other_boid: 'Boid') -> bool:
        distance_to_other_boid: float = self.position.distance_to(other_boid.position)
        return (
            other_boid != self and
            distance_to_other_boid < self.perception
        )

    def align(
        self,
        boids: list['Boid']
    ) -> Vector2:
        steer: Vector2 = Vector2(0, 0)
        total: int = 0
        for other_boid in boids:
            if self.visible(other_boid):
                steer += other_boid.velocity
                total += 1
        if total > 0:
            steer /= total
            steer.scale_to_length(self.max_speed)
            steer -= self.velocity
            if steer.length() > self.max_acceleration:
                steer.scale_to_length(self.max_acceleration)
        return steer

    def cohere(
        self,
        boids: list['Boid']
    ) -> Vector2:
        steer: Vector2 = Vector2(0, 0)
        total: int = 0
        for other_boid in boids:
            if self.visible(other_boid):
                steer += other_boid.position
                total += 1
        if total > 0:
            steer /= total
            steer -= self.position
            steer.scale_to_length(self.max_speed)
            steer -= self.velocity
            if steer.length() > self.max_acceleration:
                steer.scale_to_length(self.max_acceleration)
        return steer

    def separate(
        self,
        boids: list['Boid']
    ) -> Vector2:
        steer: Vector2 = Vector2(0, 0)
        total: int = 0
        for other_boid in boids:
            if self.visible(other_boid):
                distance: float = self.position.distance_to(other_boid.position)
                if distance < 0.1:
                    distance = 0.1
                diff: Vector2 = self.position - other_boid.position
                diff /= distance
                steer += diff
                total += 1
        if total > 0:
            steer /= total
            steer.scale_to_length(self.max_speed)
            steer -= self.velocity
            if steer.length() > self.max_acceleration:
                steer.scale_to_length(self.max_acceleration)
        return steer

    def flock(
        self,
        boids: list['Boid']
    ) -> None:
        alignment: Vector2 = self.align(boids)
        cohesion: Vector2 = self.cohere(boids)
        separation: Vector2 = self.separate(boids)

        self.acceleration += alignment * self.w_a
        self.acceleration += cohesion * self.w_c
        self.acceleration += separation * self.w_s

    def update_rect_and_rotation(self):
        new_angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x)) - 90
        if new_angle != self.angle:
            self.angle = new_angle
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0
        if self.velocity.length() > 0:
            self.velocity.scale_to_length(min(self.velocity.length(), self.max_speed))
        if self.enable_edge_collision:
            self.edge_collision()
        else:
            self.edges()
        self.update_rect_and_rotation()

    def edge_collision(self) -> None:
        min_x: int = self.rect.width // 2
        min_y: int = self.rect.height // 2
        max_x: int = CANVAS_WIDTH - min_x
        max_y: int = CANVAS_HEIGHT - min_y

        if (
            self.position.x < min_x or
            self.position.x > max_x
        ):
            self.velocity.x *= -1
        if (
            self.position.y < min_y or
            self.position.y > max_y
        ):
            self.velocity.y *= -1

        self.position.x = max(0, min(self.position.x, CANVAS_WIDTH))
        self.position.y = max(0, min(self.position.y, CANVAS_HEIGHT))

    def edges(self) -> None:
        if self.position.x > CANVAS_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = CANVAS_WIDTH

        if self.position.y > CANVAS_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = CANVAS_HEIGHT

    def draw(
        self,
        screen: pygame.Surface
    ) -> None:
        screen.blit(self.image, self.rect)
        if self.show_hitbox:
            pygame.draw.rect(screen, COLOR_GREEN, self.rect, 2)
        if self.show_vectors:
            self.draw_vector(screen, self.velocity, COLOR_GREEN)
            self.draw_vector(screen, self.acceleration, COLOR_RED)

    def draw_vector(self, screen: pygame.Surface, vector: Vector2, color: tuple) -> None:
        if vector.length() > 0:
            start_pos = self.position
            end_pos = self.position + vector * 20  # Scale the vector for visibility
            pygame.draw.line(screen, color, start_pos, end_pos, 2)
