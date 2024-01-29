import threading
import logging

from ms_basecalling.server import Server
from ms_basecalling.client import Client

def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Start the server
    server = Server(printN=False) # Set printN=True to print N for undetermined base cases
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()

    # Connect the client to the server
    client = Client()
    client.connect_to_server()

    while True:
        try:
            # Input data from the user and send it to the server
            data = input("Enter a list of floats, separated by commas: ")
            data = [float(item) for item in data.split(",")]

            logging.debug(data)
            client.send_data(data)

            # Receive and print data from the server
            res=client.receive_data()
            logger.info("Received:")
            print(str(res))
        except ValueError:
            print("Invalid input. Please enter a list of floats, separated by commas.")
        

if __name__ == "__main__":
    main()
