import pygame as pg

from config import *
from functions import *
from player import Player
from client.client import Client


class Engine:
    def __init__(self) -> None:
        self.running = True
        self.display = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.delta = 0
        self.player = Player()
        self.client = Client()

    def draw(self) -> None:
        pg.draw.circle(
            self.display,
            pg.Color(255, 255, 0),
            (self.player.x, self.player.y),
            self.player.radius,
        )

    def run(self) -> None:
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.player.move(self.delta)
            self.client.client_program((self.player.x, self.player.y))
            self.delta = delta_time()
            self.display.fill(pg.Color("darkslategray"))
            pg.display.set_caption("FPS: " + str(int(self.clock.get_fps())))

            ray_casting(self.display, self.player)

            self.clock.tick(0)
            pg.display.flip()


if __name__ == "__main__":
    app = Engine()
    app.client.start_client()
    app.run()
