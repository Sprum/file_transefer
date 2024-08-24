import socket
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = 'utf-8'

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"connected to {client.getpeername()}")

    # simulate data
    data = random.randbytes(41984)

    # send data
    client.send(data)
    client.send(b"close")
