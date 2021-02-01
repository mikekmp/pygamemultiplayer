# import time
import socket
import pickle
from threading import Thread

Serversavailable = ["nothin", "yes", "yes", "yes", "yes", "yes"]
Serverips = ["nothin", "5001", "5002", "5003", "5004"]
host = '127.0.0.1'

Gamevariables = [
    {
        "player1name": '',
        "player1health": 20,
        "player1x": 0,
        "player1y": 0
    },
    {
        "player2name": '',
        "player2health": 20,
        "player2x": 0,
        "player2y": 0
    },
    {
        "player3name": '',
        "player3health": 20,
        "player3x": 0,
        "player3y": 0
    },
    {
        "player4name": '',
        "player4health": 20,
        "player4x": 0,
        "player4y": 0
    },
    {
        "player5name": '',
        "player5health": 20,
        "player5x": 0,
        "player5y": 0
    },
    {
        "player6name": '',
        "player6health": 20,
        "player6x": 0,
        "player6y": 0
    },
    {
        "player7name": '',
        "player7health": 20,
        "player7x": 0,
        "player7y": 0
    },
    {
        "player8name": '',
        "player8health": 20,
        "player8x": 0,
        "player8y": 0
    },
    {
        "player9name": '',
        "player9health": 20,
        "player9x": 0,
        "player9y": 0
    },
    {
        "player10name": '',
        "player10health": 20,
        "player10x": 0,
        "player10y": 0
    }
]


def server0():
    while True:
        try:
            port = 5000  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    recv_data = conn.recv(1024)  # here is where the server waits for a connection
                    print(recv_data)
                    print("Someone Joined")
                    if Serversavailable[1] == "yes":
                        conn.sendall(pickle.dumps(Serverips[1]))
                    elif Serversavailable[2] == "yes":
                        conn.sendall(pickle.dumps(Serverips[2]))
                    elif Serversavailable[3] == "yes":
                        conn.sendall(pickle.dumps(Serverips[3]))
                    elif Serversavailable[4] == "yes":
                        conn.sendall(pickle.dumps(Serverips[4]))
                    # else inform players that the server is full

        except ConnectionResetError:
            print("someone left the Join server in an improper way resulting in a connection reset by windows")
            continue


def server1():
    while True:
        try:
            port = 5001  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    Serversavailable[1] = "no"
                    recv_data = conn.recv(1024)  # here is where the server waits for connection
                    data = pickle.loads(recv_data)
                    # print("someone on server1")
                    if data[0] == "bye":
                        Serversavailable[1] = "yes"
                        print("yas")
                    # print(pickle.loads(recv_data))
                    conn.sendall(pickle.dumps(Gamevariables))
        except ConnectionResetError:
            Serversavailable[1] = "yes"
            print("someone left the game on server 1 in an improper way resulting in a connection reset by windows")
            continue


def server2():
    while True:
        try:
            port = 5002  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    Serversavailable[1] = "no"
                    recv_data = conn.recv(1024)  # here is where the server waits for connection
                    data = pickle.loads(recv_data)
                    # print("someone on server2")
                    if data[0] == "bye":
                        Serversavailable[2] = "yes"
                        print("yas")
                    # print(pickle.loads(recv_data))
                    conn.sendall(pickle.dumps(Gamevariables))
        except ConnectionResetError:
            Serversavailable[2] = "yes"
            print("someone left the game on server 2 in an improper way resulting in a connection reset by windows")
            continue


def server3():
    while True:
        try:
            port = 5003  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    Serversavailable[1] = "no"
                    recv_data = conn.recv(1024)  # here is where the server waits for connection
                    data = pickle.loads(recv_data)
                    # print("someone on server3")
                    if data[0] == "bye":
                        Serversavailable[3] = "yes"
                        print("yas")
                    # print(pickle.loads(recv_data))
                    conn.sendall(pickle.dumps(Gamevariables))
        except ConnectionResetError:
            Serversavailable[3] = "yes"
            print("someone left the game on server 3 in an improper way resulting in a connection reset by windows")
            continue


def server4():
    while True:
        try:
            port = 5004  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    Serversavailable[1] = "no"
                    recv_data = conn.recv(1024)  # here is where the server waits for connection
                    data = pickle.loads(recv_data)
                    # print("someone on server4")
                    if data[0] == "bye":
                        Serversavailable[4] = "yes"
                        print("yas")
                    # print(pickle.loads(recv_data))
                    conn.sendall(pickle.dumps(Gamevariables))
        except ConnectionResetError:
            Serversavailable[4] = "yes"
            print("someone left the game on server 4 in an improper way resulting in a connection reset by windows")
            continue


def server5():
    while True:
        try:
            port = 5005  # Port to listen on (non-privileged ports are > 1023)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    Serversavailable[1] = "no"
                    recv_data = conn.recv(1024)  # here is where the server waits for connection
                    data = pickle.loads(recv_data)
                    # print("someone on server5")
                    if data[0] == "bye":
                        Serversavailable[5] = "yes"
                        print("yas")
                    # print(pickle.loads(recv_data))
                    conn.sendall(pickle.dumps(Gamevariables))
        except ConnectionResetError:
            Serversavailable[5] = "yes"
            print("someone left the game on server 5 in an improper way resulting in a connection reset by windows")
            continue


def console():
    text = input("prompt ")
    if text == "close":
        while True:
            print("a")

    else:
        print(text)


if __name__ == '__main__':
    Thread(target=server0).start()
    Thread(target=server1).start()
    Thread(target=server2).start()
    Thread(target=server3).start()
    Thread(target=server4).start()
    Thread(target=server5).start()
    Thread(target=console).start()
