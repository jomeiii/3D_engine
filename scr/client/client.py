import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from functions import get_local_ip
from player import Player

import socket


class Client:
    def __init__(self) -> None:
        """Инициализация клиента и создание сокета."""
        self.HOST = get_local_ip()
        self.PORT = 8080
        self.client_socket = socket.socket()
        self.client_socket.connect((self.HOST, self.PORT))

    def client_program(self, player: Player) -> None:
        self.client_socket.send(
            f"x: {player.x}, y: {player.y}, radius: {player.radius}, angle: {player.angle}, ver_a: {player.ver_a}".encode()
        )

    def start_client(self) -> None:
        data = self.client_socket.recv(1024).decode()
        print(data)
