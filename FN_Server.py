import socket, threading, queue

messages = queue.Queue()
users = []

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket
serverSocket.bind(("127.0.0.1", 9301))

def receive():
    while True:
        try:
            msg, addr = serverSocket.recvfrom(1024)
            messages.put((msg, addr))
        
        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            msg, addr = messages.get()
            print(msg.decode())
            if addr not in users:
                users.append(addr)
            
            for client in users:
                try:
                    if msg.decode().startswith("SIGNUP_TAB:"):
                        name = msg.decode()[msg.decode().index(":")+1:]
                        serverSocket.sendto(f"{name} joined!", client)
                    else:
                        serverSocket.sendto(msg, client)

                except:
                    users.remove(client)

recv_thread = threading.Thread(target=receive)
bdct_thread = threading.Thread(target=broadcast)

recv_thread.start()
bdct_thread.start()

print(f"CHATROOM\n\nThis is the server side.\
          \nI am ready to receive connections on port 9301\n")