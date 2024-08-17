from config import *
from player import Player
import pygame as pg

import socket
import math
import re
import time

cur_time = time.time_ns()


def delta_time() -> float:
    global cur_time
    delta = (time.time_ns() - cur_time) / 1000000000
    cur_time = time.time_ns()
    return delta


def ray_casting(display: pg.display, player: Player) -> None:
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
            # если
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

        ray_size = min(vd, hd) * depth_coeff
        ray_size *= math.cos(player.angle - cur_angle)
        height_c = coefficient / (ray_size + 0.0001)
        c = 255 / (1 + ray_size**2 * 0.000001)
        color = (c, c, c)
        ray_x = int(ray * (width / num_rays))
        pg.draw.rect(
            display,
            color,
            (ray_x, (half_height - height_c // 2) - player.ver_a, scale, height_c),
        )


def get_local_ip() -> str:
    return socket.gethostbyname(socket.gethostname())


def parse_player(player_data: str) -> Player:
    # Обрезаем лишние пробелы в начале и конце строки
    player_data = player_data.strip()
    
    pattern = r"x:\s*([-]?[\d.]+),\s*y:\s*([-]?[\d.]+),\s*radius:\s*([\d.]+),\s*angle:\s*([-]?[\d.]+),\s*ver_a:\s*([-]?[\d.]+)"
    
    # Ищем совпадение с паттерном
    match = re.search(pattern, player_data)
    
    if match:
        try:
            x = float(match.group(1))
            y = float(match.group(2))
            radius = float(match.group(3))
            angle = float(match.group(4))
            ver_a = float(match.group(5))

            player = Player()
            player.x, player.y = x, y
            player.radius = radius
            player.angle = angle
            player.ver_a = ver_a
            return player
        except ValueError as e:
            print(f"Error converting player data to floats: {e}")
            return None
    else:
        print("Pattern did not match.")
        print(f"Expected pattern: {pattern}")
        print(f"Actual data: {player_data}")
        return None


