import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from functions import get_local_ip, parse_player, ray_casting

from config import *
import socket
import pygame as pg


class Server:
    def __init__(self) -> None:
        self.HOST = get_local_ip()
        self.PORT = 8080
        self.socket_server = socket.socket()
        self.clients = []
        self.is_running = True
        self.display = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Server")

    def handle_events(self) -> None:
        """Обработка событий Pygame, таких как закрытие окна."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

    def server_program(self) -> None:
        self.socket_server.bind((self.HOST, self.PORT))
        self.socket_server.listen(5)
        print("The server is created and ready to go!")

        while self.is_running:
            conn, addr = self.socket_server.accept()
            self.clients.append((conn, addr))
            print("Connection from: " + str(addr))
            print("Type '/stop' to end the search or Enter to start. ")
            message = input("  ->  ")
            if message == "/stop":
                break

        if self.is_running:
            # Сигнал, что можно начинать игру
            [client[0].send("Start game".encode()) for client in self.clients]

            while self.is_running:
                self.handle_events()  # Обработка событий Pygame

                data = conn.recv(2048).decode()
                if not data:
                    break

                self.display.fill("purple")

                player = parse_player(data)
                if player:
                    ray_casting(self.display, player)
                    print("from connected user: " + str(player))
                else:
                    print("failed to get a player")

                pg.display.flip()
                self.clock.tick(0)

        conn.close()
        self.socket_server.close()
        pg.quit()
        print("Server stopped cleanly.")


if __name__ == "__main__":
    server_app = Server()
    server_app.server_program()
