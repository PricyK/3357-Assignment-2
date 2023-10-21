import socket, threading, random

HEADER = 1024
FORMAT = 'ascii'
SERVER = '127.0.0.1'
PORT = random.randint(4000, 8000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((SERVER, PORT))

name = input("Nickname: ")

def receive():
    while True:
        try:
            message, _ = client.recvfrom(HEADER)
            print(message.decode(FORMAT))

        except:
            pass


t = threading.Thread(target=receive)
t.start()

client.sendto(f"NICKNAME: {name}".encode(FORMAT), (SERVER, 9999)) #sending to server so it has to be the server's port and IP

while True:
    message = input("")
    if message == "!q":
        client.sendto("[DISCONNECTING]".encode(FORMAT), (SERVER, 9999))
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(FORMAT), (SERVER, 9999))

