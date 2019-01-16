import socket
import time
import threading
import pygame
import MySQLdb

ux = 0
uy = 0
rx = 400
ry = 100
gx = 200
gy = 300
bx = 600
by = 300
bpx = 100
bpy = 100
dis = [50,100,100]
listener = 'None'
# class threl(threading.Thread):
#     def run(self):
#         while True:
#             print threading.currentThread().getName()
#             time.sleep(1)
disp_h = 800
disp_w = 600

black = (0,0,0)
dgray = (60,60,60)
white = (255,255,255)

red = (255,0,0)
lred = (200,0,0)
green= (0,255,0)
lgreen= (0,200,0)
blue = (0,0,255)
lblue = (0,0,200)

def listen():

    while True:
        listrang(konek[0],n, pd, d, 0)
        listrang(konek[1],n, pd, d, 1)
        listrang(konek[2],n, pd, d, 2)
        tril(rx, ry, dis[0], gx, gy, dis[1], bx, by, dis[2])
        time.sleep(0.1)


def listrang(con, n, pd, d, var):
    pr = int(con.recv(2))
    prw = format((10**(float(pr*-1)/10))*(10**6), '.9f')
    pdw = format((10**(float(pd*-1)/10))*(10**6), '.9f')
    # print prw + ' nW'
    d = (3 * (float(pdw))**(1/float(n))) / (float(prw))**(1/float(n))
    print str(d) + ' m'
    # print str(var)
    global dis
    d = d * 30 #20 pix/meter
    print str(d) + ' pix'
    dis[var] = d

def tril(rx, ry, rd, gx, gy, gd, bx, by, bd):
    R = rx**2 + ry**2 - rd**2
    G = gx**2 + gy**2 - gd**2
    B = bx**2 + by**2 - bd**2

    Xbg = bx - gx
    Xrb = rx - bx
    Xgr = gx - rx
    Ybg = by - gy
    Yrb = ry - by
    Ygr = gy - ry

    x = (float((R*Ybg) + (G*Yrb) + (B*Ygr))) / float((2 * ((rx*Ybg) + (gx*Yrb) +(bx*Ygr))))
    y = (float((R*Xbg) + (G*Xrb) + (B*Xgr))) / float((2 * ((ry*Xbg) + (gy*Xrb) +(by*Xgr))))

    global ux, uy
    ux, uy = x, y
    print ux, uy
    # time.sleep(1)

def list2(x, y, col, scol, list):
    mou = pygame.mouse.get_pos()
    cli = pygame.mouse.get_pressed()

    pygame.draw.circle(map_display, col, (x, y), 6)

    if x-6 < mou[0] < x+6 and y-6 < mou[1] < y+6:
        pygame.draw.circle(map_display, scol, (x, y), 6)
        if cli[0] == 1:
            global listener
            listener = list
            if list == 'Red':
                global rx
                rx = mou[0]
                global ry
                ry = mou[1]
            if list == 'Green':
                global gx
                gx = mou[0]
                global gy
                gy = mou[1]
            if list == 'Blue':
                global bx
                bx = mou[0]
                global by
                by = mou[1]

    # c = 0
    # if x-6 < mou[0] < x+6 and y-6 < mou[1] < y+6:
    #     pygame.draw.circle(map_display, scol, (x, y), 6)
    #     c = 1
    #
    # if cli[0] == 1:\
    #     d = 1
    #     global listener
    #     listener = list
    #
    # if c == 1 and d == 1:
    #     if list == 'Red':
    #         global rx
    #         rx = mou[0]
    #         global ry
    #         ry = mou[1]
    #     elif list == 'Green':
    #         global gx
    #         gx = mou[0]
    #         global gy
    #         gy = mou[1]
    #     elif list == 'Blue':
    #         global bx
    #         bx = mou[0]
    #         global by
    #         by = mou[1]
    #     elif c == 0 and d == 1:
    #         if list == 'Red':
    #             global rx
    #             rx = mou[0]
    #             global ry
    #             ry = mou[1]
    #         elif list == 'Green':
    #             global gx
    #             gx = mou[0]
    #             global gy
    #             gy = mou[1]
    #         elif list == 'Blue':
    #             global bx
    #             bx = mou[0]
    #             global by
    #             by = mou[1]

def blup(x, y, scol, list):
    mou = pygame.mouse.get_pos()
    cli = pygame.mouse.get_pressed()

    global listener, bpx, bpy
    img(mapf, bpx, bpy)
    sizm = mapf.get_size()
    # print sizm

    if x < mou[0] < x + sizm[0] and y < mou[1] < y + sizm[1]:
        # mx, my = mou[0], mou[1]
        if cli[2] == 1:
            listener = list
            bpx = mou[0] - (sizm[0]/2)
            bpy = mou[1] - (sizm[1]/2)

def texobj(text, font, color):
    texsur = font.render(text, True, color)
    return texsur, texsur.get_rect()

def disp_text(text, x, y):
    lar = pygame.font.Font('freesansbold.ttf', 12)
    texsur, texrect = texobj(text, lar, white)
    texrect = ((x, y))
    map_display.blit(texsur, texrect)

def disp_textgr(text, x, y):
    lar = pygame.font.Font('freesansbold.ttf', 12)
    texsur, texrect = texobj(text, lar, dgray)
    texrect = ((x, y))
    map_display.blit(texsur, texrect)

# def door(do1, do2, do3):
#     # cdo1 =
#     if do1 == 'd1t':
#         pygame.draw.line(map_display, white, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#         if bpx + 40 < ux < bpx + 40 and bpx + 40 < ux < bpx + 40:
#
#     elif do1 == 'd1f':
#         pygame.draw.line(map_display, black, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#
#     if do2 == 'd2t':
#         pygame.draw.line(map_display, white, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#     elif do2 == 'd2f':
#         pygame.draw.line(map_display, black, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#
#     if do3 == 'd3t':
#         pygame.draw.line(map_display, white, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#     elif do3 == 'd3f':
#         pygame.draw.line(map_display, black, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)

# def auth():
#     pygame.draw.line(map_display, red, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#     # pygame.draw.line(map_display, red, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#     # pygame.draw.line(map_display, red, (bpx + 40, bpy + 550), (bpx + 21, bpy + 31), 6)
#     if user == 'System Administrator':
#         door()
#     # elif user == 'Server Administrator':
#
#     elif user == 'Janitor':

def alp():
    s = pygame.Surface((180,80))  # the size of your rect
    s.set_alpha(75)                # alpha level
    s.fill((255,255,255))           # this fills the entire surface
    map_display.blit(s, (0,520))

    pygame.draw.circle(map_display, red, (40, 550), 6)
    pygame.draw.circle(map_display, green, (40, 570), 6)
    pygame.draw.circle(map_display, blue, (40, 590), 6)
    disp_text('Listener position: (x,y)', 20, 525)
    disp_text(str(rx), 50, 545)
    disp_text(str(disp_w-ry), 80, 545)
    disp_text(str(gx), 50, 565)
    disp_text(str(disp_w-gy), 80, 565)
    disp_text(str(bx), 50, 585)
    disp_text(str(disp_w-by), 80, 585)
    disp_text('(1 x 1)?/div', 110, 505)
    disp_textgr('x: '+str(ux), ux, uy+30)
    disp_textgr('y: '+str(disp_w-uy), ux, uy+50)
    disp_textgr(res[0][0], ux, uy+70)

def img(obj, x, y):
    map_display.blit(obj, (x,y))

class mape(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global ux, uy
        while True:
            listrang(konek[0],n, pd, d, 0)
            listrang(konek[1],n, pd, d, 1)
            listrang(konek[2],n, pd, d, 2)
            tril(rx, ry, dis[0], gx, gy, dis[1], bx, by, dis[2])
            pos = 'o' + str(ux) + 'x' + str(uy)
            cur.execute ("update user_db set user_pos=%s where username=%s", (pos,res[0][0]))

con = MySQLdb.connect('localhost', 'root', "", 'dukhaan')
con.autocommit(True)
while True:
    con.query("select username from user_db where user_pos like \"o%\"")
    k = con.store_result()
    res = k.fetch_row()
    #con.commit()
    if res:
        con.query("select cur_wpa2_pass from user_db where user_pos like \"o%\"")
        l = con.store_result()
        pas = l.fetch_row()
        con.commit()
        print res
        print pas
        break

masr = '192.168.43.174'
colokan = socket.socket()
colokan.bind((masr,4004))
colokan.listen(3)
print ('Listening on: ' + masr)
konek = {}
pengirim = {}
n, pd, d = 5, 40, 1 #path loss, measured power on d (dBm), d (meter); these value is environment-dependant
for x in range (3):
    konek[x], pengirim[x] = colokan.accept()
    # konek[x].send(res [0][0] + '//' +pas[0][0])
    konek[x].send(res[0][0])
    # print res[0][0]
    time.sleep(0.1)
    konek[x].send(pas[0][0])
    # print pas[0][0]

cur = con.cursor()

mappe = mape()
mappe.start()

pygame.init()

pygame.display.set_caption('Najm')
map_display = pygame.display.set_mode((disp_h,disp_w))
clock = pygame.time.Clock()
user = pygame.image.load('usersc.png')
mapf = pygame.image.load('baitfrres.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if listener == 'Red':
                    rx += -1
                elif listener == 'Green':
                    gx += -1
                elif listener == 'Blue':
                    bx += -1
                elif listener == 'Blueprint':
                    bpx += -1
            if event.key == pygame.K_RIGHT:
                if listener == 'Red':
                    rx += 1
                elif listener == 'Green':
                    gx += 1
                elif listener == 'Blue':
                    bx += 1
                elif listener == 'Blueprint':
                    bpx += 1
            if event.key == pygame.K_UP:
                if listener == 'Red':
                    ry += -1
                elif listener == 'Green':
                    gy += -1
                elif listener == 'Blue':
                    by += -1
                elif listener == 'Blueprint':
                    bpy += -1
            if event.key == pygame.K_DOWN:
                if listener == 'Red':
                    ry += 1
                elif listener == 'Green':
                    gy += 1
                elif listener == 'Blue':
                    by += 1
                elif listener == 'Blueprint':
                    bpy += 1

    # print listener
    map_display.fill(black)
    blup(bpx, bpy, white, 'Blueprint')
    # for x in range (40):
    #     for y in range (30):
    #         pygame.draw.line(map_display, dgray, ((disp_h/40)*x, 0), ((disp_h/40)*x, 600), 1)
    #         pygame.draw.line(map_display, dgray, (0, (disp_w/30)*y), (800, (disp_w/30)*y), 1)

    if listener == 'Red':
        pygame.draw.circle(map_display, white, (rx, ry), 8)
    if listener == 'Green':
        pygame.draw.circle(map_display, white, (gx, gy), 8)
    if listener == 'Blue':
        pygame.draw.circle(map_display, white, (bx, by), 8)

    list2(rx, ry, lred, red, "Red")
    list2(gx, gy, lgreen, green, "Green")
    list2(bx, by, lblue, blue, "Blue")

    disp_text('Ruang Server: Lantai 4', 10, 10)
    alp()
    # pygame.draw.circle(map_display, green, (ux, uy), 2)
    img(user, ux, uy)
    pygame.display.update()
    clock.tick(60)

# listen()
