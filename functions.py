from config import *
from player import Player
import pygame as pg

import math
import time

cur_time = time.time_ns()


def delta_time():
    global cur_time
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta


def ray_casting(display: pg.display, player: Player):
    in_block_pos = {
        "left": player.x - player.x // block_size * block_size,
        "top": player.y - player.y // block_size * block_size,
        "right": block_size - (player.x - player.x // block_size * block_size),
        "bottom": block_size - (player.y - player.y // block_size * block_size),
    }

    for ray in range(num_rays):
        cur_angle = player.angle - half_FOV + delta_ray * ray
        cos_a, sin_a = math.cos(cur_angle), math.sin(cur_angle)
        vd, hd = 0, 0

        # Вертикали
        for dep in range(max_depth):
            if cos_a > 0:
                vd = in_block_pos["right"] / cos_a + block_size / cos_a * dep + 1
            elif cos_a < 0:
                vd = in_block_pos["left"] / -cos_a + block_size / -cos_a * dep + 1

            x, y = vd * cos_a + player.x, vd * sin_a + player.y
            fixed_x, fixed_y = (
                x // block_size * block_size,
                y // block_size * block_size,
            )
            if (fixed_x, fixed_y) in block_map:
                break

        # Горизонтали
        for dep in range(max_depth):
            if sin_a > 0:
                hd = in_block_pos["bottom"] / sin_a + block_size / sin_a * dep + 1
            elif sin_a < 0:
                hd = in_block_pos["top"] / -sin_a + block_size / -sin_a * dep + 1

            x, y = hd * cos_a + player.x, hd * sin_a + player.y
            fixed_x, fixed_y = (
                x // block_size * block_size,
                y // block_size * block_size,
            )
            if (fixed_x, fixed_y) in block_map:
                break

        ray_size = min(vd, hd)
        ray_size *= math.cos(player.angle - cur_angle)
        height_c = coefficient / (ray_size + 0.0001)
        color = (255, 255, 255)
        pg.draw.rect(
            display, color, (ray * scale, half_height - height_c // 2, scale, height_c)
        )
