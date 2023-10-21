# Assignment: UDP Simple Chat Room - UDP Client Code Implementation
import socket, threading, random, argparse


HEADER = 1024
FORMAT = 'ascii'
SERVER = '127.0.0.1'
PORT = random.randint(8000, 9000)


def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode(FORMAT))
        except:
            pass



def run(clientSocket, clientname, serverAddr, serverPort):
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    client.sendto(f"SIGNUP_TAG: {clientname}".encode(FORMAT), (SERVER, 9999))

    while True:
        message = input(f"{clientname}: ")
        msg = message[message.index(":")+2:]
        if msg == "!q":
            client.sendto(f"[{clientname} DISCONNECTING]".encode(FORMAT), (SERVER, 9999))
            exit()
        else:
            client.sendto(f"{clientname}: {msg}".encode(FORMAT), (SERVER, 9999))


# **Main Code**:  
if __name__ == "__main__":
    
    # Arguments: name address
    parser = argparse.ArgumentParser(description='argument parser')
    parser.add_argument('name')  # to use: python udp_client.py username
    args = parser.parse_args()
    nickname = args.name
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    client.bind((SERVER, PORT))

    run(client, nickname, SERVER, 9999)  # Calling the function to start the client.
