# Assignment: UDP Simple Chat Room - UDP Server Code Implementation
import socket, threading, queue


HEADER = 1024
FORMAT = 'ascii'
PORT = 9999

messages = queue.Queue()
clients = []


def receive(server):
    while True:
        try:
            message, addr = server.recvfrom(HEADER)
            messages.put((message, addr))
        except:
            pass

def broadcast(server):
    while True:
        while not messages.empty():

            message, addr = messages.get()
            print(message.decode(FORMAT))

            if addr not in clients:
                clients.append(addr)

            for client in clients:
                try:
                    if message.decode().startswith("NICKNAME:"):
                        nickname = message.decode(FORMAT)[message.decode().index(":")+1:]
                        server.sendto(f"{nickname} has joined the chat!")
                    else:
                        server.sendto(message, client)

                except:
                    clients.remove(client)


def run(serverSocket, serverPort):
    print("Server is listening...")

    recv_thread = threading.Thread(target=receive, args=(serverSocket,))
    brdcst_thread = threading.Thread(target=broadcast, args=(serverSocket,))

    recv_thread.start()
    brdcst_thread.start()

# **Main Code**:  
if __name__ == "__main__":
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating a UDP socket.
    server.bind(("127.0.0.1", PORT))

    
    run(server, PORT)  # Calling the function to start the server.
