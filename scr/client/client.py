import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from functions import get_local_ip

import socket


class Client:
    def __init__(self) -> None:
        """Инициализация клиента и создание сокета."""
        self.HOST = get_local_ip()
        self.PORT = 8080
        self.client_socket = socket.socket()
        self.client_socket.connect((self.HOST, self.PORT))
        

    def client_program(self, player_pos: tuple) -> None:
        self.client_socket.send(f"x: {player_pos[0]}, y: {player_pos[1]}".encode())

    def start_client(self) -> None:
        data = self.client_socket.recv(1024).decode()
        print(data)
