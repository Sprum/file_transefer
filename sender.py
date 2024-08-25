import os.path
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = 'utf-8'
FILE_PATH = ""

if __name__ == '__main__':
    FILE_PATH = input("Enter file path: ")
    filename = os.path.basename(FILE_PATH)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"connected to {client.getpeername()}")

    # send file name
    client.sendall(filename.encode(FORMAT))

    # read and send data
    with open(FILE_PATH, 'rb') as f:
        while chunk := f.read(SIZE):
            client.sendall(chunk)

    print("file successfully sent!")
    client.close()
