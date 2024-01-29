import socket
import logging
from typing import List

class Client:
    def __init__(self, host: str = 'localhost', port: int = 9999):
        self.host: str = host
        self.port: int = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.logger = logging.getLogger(__name__)


    def connect_to_server(self) -> None:
        """
        Function to connect to the server.
        """
        self.socket.connect((self.host, self.port))
        self.logger.info(f"Connected to server at {self.host}:{self.port}")

    def send_data(self, data: List[float]) -> None:
        """
        Function to send data to the server.
        Args:
            data: List of floats.
        """
        self.socket.send(str(data).encode())

    def receive_data(self) -> None:
        """
        Function to receive data from the server.
        """
        data = self.socket.recv(1024)
        data = eval(data.decode())
        return data
        
