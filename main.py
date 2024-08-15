import pygame as pg

from config import *
from functions import *
from player import Player


class Engine:
    def __init__(self):
        self.running = True
        self.display = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.player = Player()
        self.delta = 0

    def draw(self):
        pg.draw.circle(
            self.display,
            pg.Color(255, 255, 0),
            (self.player.x, self.player.y),
            self.player.radius,
        )

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.player.move(self.delta)
            self.delta = delta_time()
            self.display.fill(pg.Color("darkslategray"))

            ray_casting(self.display, self.player)

            # self.draw()

            self.clock.tick(0)
            pg.display.flip()


if __name__ == "__main__":
    app = Engine()
    app.run()
