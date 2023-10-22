import socket, threading, argparse, random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parses Argument")
    parser.add_argument("user_name")
    args_parser = parser.parse_args()
    user_name = args_parser.user_name

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.bind(("127.0.0.1", random.randint(4000, 9000)))

    clientSocket.sendto(f"SIGNUP_TAG: {user_name}".encode(), ("127.0.0.1", 9301))


def receive():
    while True:
        try:
            message, _ = clientSocket.recvfrom(1024)
            print(message.decode())
        except:
            pass

recv_thread = threading.Thread(target=receive)
recv_thread.start()

while True:
    message = input("")
    if message == "!q":
        clientSocket.sendto(f"[DISCONNECTING FROM SERVER]".encode(), ("127.0.0.1", 9301))
        clientSocket.close()
        break
    else:
        clientSocket.sendto(f"{user_name}: {message}".encode(), ("127.0.0.1", 9301))