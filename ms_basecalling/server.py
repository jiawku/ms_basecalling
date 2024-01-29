import socket
import threading
import logging

from typing import List
from ms_basecalling.basecalling import Basecalling

class Server:
    def __init__(self, port: int = 9999, printN=False):
        """Server

        Args:
            port (int, optional): the port to lisense. Defaults to 9999.
            printN (bool, optional): Whether output N for undetermined base cases. Defaults to False.
        """
        self.port: int = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.threads: List[threading.Thread] = []
        self.printN = printN
        self.logger = logging.getLogger(__name__)
        

    def start_server(self) -> None:
        """
        Function to start the server.
        """
        self.socket.bind(('localhost', self.port))
        self.socket.listen(5)
        self.logger.info(f"Server started on port {self.port}")
        while True:
            client_socket, addr = self.socket.accept()
            self.logger.info(f"Connection from {addr}")
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()
            self.threads.append(thread)

    def handle_client(self, client_socket: socket) -> None:
        """
        Function to handle a client.
        Args:
            client_socket: The socket of the client.
        """
        basecalling = Basecalling(printN=self.printN)
        while True:
            data = client_socket.recv(1024)
            self.logger.debug("received:"+str(data))
            if not data:
                break
            data = list(map(float, data.decode().strip("]").strip("[").split(',')))
            self.logger.debug("parsed:"+str(data))
            basecallings = basecalling.identify_basecallings(data)
            self.logger.info("Identified:"+str(basecallings))
            client_socket.send(str(basecallings).encode())
        client_socket.close()
