import socket


def main():
    host = socket.gethostname()
    port = 3000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter message: ")

    while message.lower().strip() != "quit":
        client_socket.send(message.encode())
        messag = client_socket.recv(1024).decode()
        print(f"Received message {messag}")
        message = input("Enter message: ")

    client_socket.close()


if __name__ == "__main__":
    main()
