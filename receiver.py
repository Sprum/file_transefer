import socket
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (IP, PORT)
SIZE = 4096
FORMAT = 'utf-8'
OUTPUT_DIR = "received/"

if __name__ == '__main__':
    # set up server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    print(f"Listening on {ADDR}.")

    con, addr = server.accept()
    with con:
        print(f'connected to {addr}')

        filename = con.recv(SIZE).decode(FORMAT).strip()
        print(f'receiving file: {filename}')

        with open(OUTPUT_DIR+filename, 'wb') as f:
            # receiving loop
            while True:
                data = con.recv(SIZE)
                if not data:
                    break
                f.write(data)

    print("file successfully received")
