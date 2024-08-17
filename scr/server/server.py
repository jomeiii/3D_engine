import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from functions import get_local_ip, parse_player_pos

import socket


class Server:
    def __init__(self) -> None:
        self.HOST = get_local_ip()
        self.PORT = 8080
        self.socket_server = socket.socket()
        self.clients = []
        self.is_running = True

    def server_program(self) -> None:
        self.socket_server = socket.socket()
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
                self.is_running = False

        # Сигнал, что можно начинать игру
        [client[0].send("Start game".encode()) for client in self.clients]

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))

        conn.close()


if __name__ == "__main__":
    server_app = Server()
    server_app.server_program()
