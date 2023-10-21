import socket, threading, queue

HEADER = 1024
FORMAT = 'ascii'
PORT = 9999
SERVER = '127.0.0.1'

messages = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))

def receive():
    while True:
        try: 
            message, addr = server.recvfrom(HEADER)
            messages.put((message, addr))
        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            
            message, addr = messages.get()
            print(message.decode(FORMAT))
            
            if addr not in clients:
                clients.append(addr)
            
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":")+1:]
                        server.sendto(f"{name} joined".encode(FORMAT), client)
                    else:
                        server.sendto(message, client)
                except:
                    clients.remove(client)

recv_thread = threading.Thread(target=receive)
brdcst_thread = threading.Thread(target=broadcast)

recv_thread.start()
brdcst_thread.start()

print("Server is listening...")