import pickle
import socket
import time
import pygame
from win32api import GetSystemMetrics
from random import randrange
import pygame.freetype

joininggame = False
disconnected = False

host = ''  # The server's hostname or IP address, probably will only use the second one
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
ww = 1000
nn = 600
DISPLAYSURF = pygame.display.set_mode((ww, nn), pygame.RESIZABLE)
keys = pygame.key.get_pressed()
alt = False
f4 = False
mainloop = True
last = False
servok = 0
click = False
stateofgame = 0
mouse = pygame.mouse.get_pos()
font = pygame.freetype.Font("font.ttf", 36)
font2 = pygame.freetype.Font("font.ttf", 90)
name = ""
serverip = ""
allowedserverchars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":", ".", "a", "b", "c", "d", "e", "f", "g"
    , "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
namet = False
serveript = False


# FPS = 60  # frames per second setting
# fpsClock = pygame.time.Clock()


def mainmenu():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse, r, g, b, r3, g3, b3, \
        w, h, click
    wn, hn = pygame.display.get_surface().get_size()
    mx, my = pygame.mouse.get_pos()
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
    DISPLAYSURF.fill((r, g, b))
    if fullscreen:
        # text on top
        text_surface, rect = font2.render("MAIN MENU", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 160), 50))
        # buttons
        button1 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(w / 2 - 160), 280, 300, 80))
        text_surface, rect = font.render("Play", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(w / 2 - 35), 300))
        if button1.collidepoint(mx, my):
            if click:
                stateofgame += 1
        button2 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(w / 2 - 160), 420, 300, 80))
        text_surface, rect = font.render("Exit", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(w / 2 - 35), 440))
        if button2.collidepoint(mx, my):
            if click:
                mainloop = False
                print("The whole game got closed")
    else:
        # text on top
        text_surface, rect = font2.render("MAIN MENU", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 160), 20))
        # buttons
        button1 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 180, 300, 80))
        text_surface, rect = font.render("Play", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 35), 200))
        if button1.collidepoint(mx, my):
            if click:
                stateofgame += 1
        button2 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 320, 300, 80))
        text_surface, rect = font.render("Exit", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 35), 340))
        if button2.collidepoint(mx, my):
            if click:
                mainloop = False
                print("The whole game got closed")
    click = False
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if fullscreen:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.FULLSCREEN)
            else:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
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
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    pygame.display.flip()
    # fpsClock.tick(FPS)


##############################################################################


def beforejoin():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse, r, g, b, r3, g3, b3, \
        w, h, click, serverip, name, serveript, namet, joininggame, host, allowedserverchars, port
    wn, hn = pygame.display.get_surface().get_size()
    mx, my = pygame.mouse.get_pos()
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
    DISPLAYSURF.fill((r, g, b))
    if fullscreen:
        # buttons
        button1 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(w / 2 - 160), 140, 300, 40))
        text_surface, rect = font.render("Server's ip:", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(w / 2 - 75), 90))
        if serveript:
            text_surface2, rect = font.render(serverip + "_", (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(w / 2 - 160), 140))
        else:
            text_surface2, rect = font.render(serverip, (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(w / 2 - 160), 140))
        if button1.collidepoint(mx, my):
            if click:
                serveript = True
                namet = False
        button2 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(w / 2 - 160), 280, 300, 40))
        text_surface, rect = font.render("Name:", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(w / 2 - 40), 230))
        if namet:
            text_surface2, rect = font.render(name + "_", (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(w / 2 - 160), 280))
        else:
            text_surface2, rect = font.render(name, (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(wn / 2 - 160), 280))
        if button2.collidepoint(mx, my):
            if click:
                namet = True
                serveript = False
        button4 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 350, 300, 40))
        text_surface, rect = font.render("Join", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 40), 355))
        if button4.collidepoint(mx, my):
            if click:
                serveript = False
                namet = False
                stateofgame += 1
        button3 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 435, 300, 40))
        text_surface, rect = font.render("Back", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 40), 440))
        if button3.collidepoint(mx, my):
            if click:
                serveript = False
                namet = False
                stateofgame -= 1
    else:
        # buttons
        button1 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 140, 300, 40))
        text_surface, rect = font.render("Server's ip:", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 75), 90))
        if serveript:
            text_surface2, rect = font.render(serverip + "_", (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(wn / 2 - 160), 140))
        else:
            text_surface2, rect = font.render(serverip, (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(wn / 2 - 160), 140))
        if button1.collidepoint(mx, my):
            if click:
                serveript = True
                namet = False
        button2 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 280, 300, 40))
        text_surface, rect = font.render("Name:", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 40), 230))
        if namet:
            text_surface2, rect = font.render(name + "_", (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(wn / 2 - 160), 280))
        else:
            text_surface2, rect = font.render(name, (0, 0, 0))
            DISPLAYSURF.blit(text_surface2, (int(wn / 2 - 160), 280))
        if button2.collidepoint(mx, my):
            if click:
                namet = True
                serveript = False
        button4 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 350, 300, 40))
        text_surface, rect = font.render("Join", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 40), 355))
        if button4.collidepoint(mx, my):
            if click:
                serveript = False
                namet = False
                stateofgame += 1
                joininggame = True
                x = serverip.split(":")
                host = x[0]
                port = x[1]
                port = int(port)
                print(host)
                print(port)
        button3 = pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (int(wn / 2 - 160), 435, 300, 40))
        text_surface, rect = font.render("Back", (0, 0, 0))
        DISPLAYSURF.blit(text_surface, (int(wn / 2 - 40), 440))
        if button3.collidepoint(mx, my):
            if click:
                serveript = False
                namet = False
                stateofgame -= 1
    click = False
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if fullscreen:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.FULLSCREEN)
            else:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if serveript:
                    serverip = serverip[:-1]
                    host = host[:-1]
                elif namet:
                    name = name[:-1]
            else:
                if serveript:
                    if event.unicode in allowedserverchars:
                        serverip += event.unicode
                        print(serverip)
                    else:
                        continue
                elif namet:
                    name += event.unicode
            # if event.key == pygame.K_l:
            # stateofgame += 1
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    pygame.display.flip()
    # fpsClock.tick(FPS)


###########################################################


def play():
    global f4, alt, fullscreen, mainloop, disconnected, DISPLAYSURF, stateofgame, mouse, r, g, b, r3, g3, b3, \
        w, h, click, last
    # wn, hn = pygame.display.get_surface().get_size()
    # mx, my = pygame.mouse.get_pos()
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
    DISPLAYSURF.fill((r, g, b))
    click = False
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if fullscreen:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.FULLSCREEN)
            else:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            print("The whole game got closed")
            mainloop = False
            last = True
            disconnected = True
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
            if event.key == pygame.K_F11:
                if fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
                    fullscreen = False
                elif not fullscreen:
                    pygame.quit()
                    DISPLAYSURF = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
                    fullscreen = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
    pygame.display.flip()
    # fpsClock.tick(FPS)


while mainloop or last:
    if mainloop:
        if stateofgame == 0:
            mainmenu()
        elif stateofgame == 1:
            beforejoin()
        elif stateofgame == 2:
            play()
        else:
            stateofgame = 0
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if joininggame or disconnected:
                try:
                    s.connect((host, port))
                except ConnectionRefusedError:
                    stateofgame = 2
                    servok = 1
            # t = time.localtime()
            # current_time = time.strftime("%H:%M:%S", t)
            time.sleep(0.02)
            data = pickle.dumps(Playervariables)
            byemessage = pickle.dumps(["bye"])
            if joininggame or disconnected:
                if not disconnected and servok == 0:
                    try:
                        stateofgame = 2
                        servok = 0
                        s.sendall(data)
                        # print("sent")
                        recv_data = s.recv(1024)
                        actualdata = pickle.loads(recv_data)
                        print(actualdata)
                    except ConnectionResetError:
                        continue
                    try:
                        float(actualdata)
                        print(actualdata)
                        port = int(actualdata)
                    except TypeError:
                        continue
                elif disconnected:
                    s.sendall(byemessage)
                    print("bye")
                    disconnected = False
                    port = 5000
                if servok == 1:
                    disconnected = False
                    servok = 0
                    joininggame = False
                    stateofgame -= 1
    last = False
    time.sleep(0.01)
    pygame.display.update()
pygame.quit()
