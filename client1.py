import pickle
import socket
import time
import pygame
from win32api import GetSystemMetrics
from random import randrange

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
r = randrange(255)
g = randrange(255)
b = randrange(255)
r3 = "a"
g3 = "a"
b3 = "a"
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
stateofgame = 0
mouse = pygame.mouse.get_pos()
# FPS = 60  # frames per second setting
# fpsClock = pygame.time.Clock()


def mainmenu():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse, r, g, b, r3, g3, b3
    # , FPS, fpsClock
    if r3 == "a":
        r2 = r - randrange(20)
        if r2 < 0:
            r2 = 0
            r3 = "b"
    else:
        r2 = r + randrange(20)
        if r2 > 255:
            r2 = 255
            r3 = "a"
    ###
    if g3 == "a":
        g2 = g - randrange(20)
        if g2 < 0:
            g2 = 0
            g3 = "b"
    else:
        g2 = g + randrange(20)
        if g2 > 255:
            g2 = 255
            g3 = "a"
    ###
    if b3 == "a":
        b2 = b - randrange(20)
        if b2 < 0:
            b2 = 0
            b3 = "b"
    else:
        b2 = b + randrange(20)
        if b2 > 255:
            b2 = 255
            b3 = "a"
    # time.sleep(0.2)
    r = r2
    g = g2
    b = b2
    print(r)
    print(g)
    print(b)
    DISPLAYSURF.fill((r, g, b))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                stateofgame += 1
            if event.key == pygame.K_F4:
                f4 = True
            if event.key == pygame.K_LALT:
                alt = True
            if alt:
                if f4:
                    print("The whole game got closed")
                    mainloop = False
                    disconnected = True
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True
    # fpsClock.tick(FPS)


def settings():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse
    DISPLAYSURF.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                stateofgame += 1
            if event.key == pygame.K_F4:
                f4 = True
            if event.key == pygame.K_LALT:
                alt = True
            if alt:
                if f4:
                    print("The whole game got closed")
                    mainloop = False
                    disconnected = True
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True


def play():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse
    DISPLAYSURF.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                stateofgame += 1
            if event.key == pygame.K_F4:
                f4 = True
            if event.key == pygame.K_LALT:
                alt = True
            if alt:
                if f4:
                    print("The whole game got closed")
                    mainloop = False
                    disconnected = True
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True


while mainloop:
    if stateofgame == 0:
        mainmenu()
    elif stateofgame == 1:
        settings()
    elif stateofgame == 2:
        play()
    else:
        stateofgame = 0
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
