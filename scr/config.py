import math

# screen
width = 800
height = 500
half_width = width / 2
half_height = height / 2

# map
block_size = 100
text_map = [
    "WWWWWWWWWWW",
    "W..W...W..W",
    "W..W...W..W",
    "W..W...W..W",
    "W.........W",
    "W.........W",
    "W.........W",
    "WWWWWWWWWWW",
]

block_map = set()
y_block_pos = 0
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column == "W":
            block_map.add((x_block_pos, y_block_pos))
        x_block_pos += block_size
    y_block_pos += block_size

# ray casting
FOV = math.pi / 2
half_FOV = FOV / 2
max_depth = width // block_size
num_rays = width
delta_ray = FOV / (num_rays - 1)
dist = num_rays / (2 * math.tan(half_FOV))
coefficient = dist * block_size * 2
scale = 1
depth_coeff = 2
