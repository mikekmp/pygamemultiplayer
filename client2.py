import pickle
import socket
import time
import pygame
from win32api import GetSystemMetrics

joininggame = False
disconnected = False

host = '127.0.0.1'  # The server's hostname or IP address, probably will only use the second one
Playervariables = [
    {
        "playername": 'mikekmp1',
        "playerx": 0,
        "playery": 0
    }
]

port = 5000  # The port used by the server. Changes when joining, will also be needed to be configurable
# on main menu by user

pygame.init()
fullscreen = False
infoObject = pygame.display.Info()
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
keys = pygame.key.get_pressed()
alt = False
f4 = False
mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4:
                f4 = True
            if event.key == pygame.K_LALT:
                alt = True
            if alt:
                if f4:
                    print("The whole game got closed")
                    mainloop = False
                    disconnected = True
            if event.key == pygame.K_F1:
                if joininggame:
                    joininggame = False
                    disconnected = True
                elif not joininggame:
                    joininggame = True
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True
    if mainloop:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if joininggame or disconnected:
                s.connect((host, port))
            # t = time.localtime()
            # current_time = time.strftime("%H:%M:%S", t)
            time.sleep(0.02)
            data = pickle.dumps(Playervariables)
            byemessage = pickle.dumps(["bye"])
            if joininggame or disconnected:
                try:
                    if not disconnected:
                        s.sendall(data)
                        print("sent")
                    elif disconnected:
                        s.sendall(byemessage)
                        print("bye")
                        disconnected = False
                        port = 5000
                except ConnectionResetError:
                    print("connection reset for some reason")
                    continue
                recv_data = s.recv(1024)
                actualdata = pickle.loads(recv_data)
                try:
                    float(actualdata)
                    print(actualdata)
                    port = int(actualdata)
                except TypeError:
                    continue
    pygame.display.update()
pygame.quit()
