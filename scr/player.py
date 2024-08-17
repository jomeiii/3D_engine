"""
math.cos(self.player.angle): 
Косинус угла определяет горизонтальную составляющую вектора. 
Он показывает, какая доля длины луча направлена в горизонтальном
направлении.

math.sin(self.player.angle): 
Синус угла определяет вертикальную составляющую вектора. 
Он показывает, какая доля длины луча направлена в вертикальном 
направлении.
"""

from config import *

import math
import pygame.key


class Player:
    def __init__(self) -> None:
        self.x = half_width
        self.y = half_height
        self.radius = 10
        self.angle = 0
        self.ver_a = 0
        self.camera_speed = 10
        self.speed = 1000
        self.clip_y = 250

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, radius: {self.radius}, angle: {self.angle}, ver_a: {self.ver_a}, camera_speed: {self.camera_speed}, speed: {self.speed}"

    def move(self, delta: float) -> None:
        key = pygame.key.get_pressed()
        cos_a, sin_a = math.cos(self.angle), math.sin(self.angle)

        if key[pygame.K_LEFT]:
            self.angle -= 0.3 * delta * self.camera_speed
        if key[pygame.K_RIGHT]:
            self.angle += 0.3 * delta * self.camera_speed
        if key[pygame.K_UP]:
            self.ver_a -= 1500 * delta
            self.ver_a = clip(-self.clip_y, self.clip_y, self.ver_a)
        if key[pygame.K_DOWN]:
            self.ver_a += 1500 * delta
            self.ver_a = clip(-self.clip_y, self.clip_y, self.ver_a)
        if key[pygame.K_w]:
            self.x += cos_a * self.speed * delta
            self.y += sin_a * self.speed * delta
        if key[pygame.K_s]:
            self.x -= cos_a * self.speed * delta
            self.y -= sin_a * self.speed * delta
        if key[pygame.K_a]:
            self.x += sin_a * self.speed * delta
            self.y -= cos_a * self.speed * delta
        if key[pygame.K_d]:
            self.x -= sin_a * self.speed * delta
            self.y += cos_a * self.speed * delta


def clip(min_value, max_value, value):
    """Ограничивает значение value в пределах min_value и max_value."""
    return max(min_value, min(max_value, value))
