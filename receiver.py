import socket
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = 'utf-8'

if __name__ == '__main__':
    # set up server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    print(f"Listening on {ADDR}.")

    # accept connection loop
    while True:
        con, addr = server.accept()
        print(f"Accepted connection from {addr}")
        # receive data loop
        while chunk := con.recv(SIZE):
            if not chunk:
                break
            print(chunk)
        con.close()
        break

    server.close()
