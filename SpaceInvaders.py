import os
import signal
import time
import random
import sys
from board import *
from spaceship import *
from missile import *
from block import *
from alien import *
from getch import *

g = board(17, 17)
g.inv_board()
g.initial()
os.system("clear")
g.inv_print(0)
k = getch()
g.update()

spc = Spaceship(15, 1, 1, u'\U0001f6e6')
mis = []
flag = 0
t1 = 1
score = 0
al = []

os.system("clear")
g.inv_print(score)

with raw(sys.stdin):
    with nonblocking(sys.stdin):
        while True:
            try:
                key = sys.stdin.read(1)

                if time.time() - t1 >= 10:
                    al.append(
                        alien(
                            random.randrange(
                                1, 4, 2), random.randint(
                                1, 15), "A"))
                    g.updatealien(al[0].xPos, al[0].yPos, al[0].sym)
                    al[len(al) - 1].start_tym = time.time()
                    al[len(al) - 1].end_tym = al[len(al) - 1].start_tym + 8
                    t1 = time.time()

                for i in range(len(al)):
                    if time.time() >= al[i].end_tym:
                        g.updatealien(al[i].xPos, al[i].yPos, ' ')
                        al.pop(0)

                if(key == 'q'):
                    sys.exit(0)

                if(key == 'a'):
                    oldyPos = spc.yPos
                    spc.yPos = spc.moveleft(spc.yPos)
                    g.updatespaceship(
                        spc.xPos, oldyPos, spc.xPos, spc.yPos, spc.sym)

                if(key == 'd'):
                    oldyPos = spc.yPos
                    spc.yPos = spc.moveright(spc.yPos)
                    g.updatespaceship(
                        spc.xPos, oldyPos, spc.xPos, spc.yPos, spc.sym)

                if(key == ' '):
                    mis.append(Mis1())
                    mis[flag].pos(spc.xPos, spc.yPos)
                    # print mis[flag]
                    flag += 1

                if(key == 's'):
                    mis.append(Mis2())
                    mis[flag].pos(spc.xPos, spc.yPos)
                    # print mis[flag]
                    flag += 1

                if flag >= 0:
                    for i in range(flag):
                        oldX = mis[i].x
                        mis[i].x = mis[i].moveup(mis[i].x)
                        for j in range(len(al)):
                            var = mis[i].checkcollision(
                                mis[i].x, mis[i].y, al[j].xPos, al[j].yPos)
                            if var == 1 and mis[i].typ == 1:
                                mis[i].x = 0
                                score += 1
                                al[j].sym = ' '
                            if var == 1 and mis[i].typ == 2:
                                mis[i].x = 0
                                al[j].sym = '@'
                                al[j].end_tym = time.time() + 5
                            g.updatealien(al[j].xPos, al[j].yPos, al[j].sym)
                            if var == 1 and mis[i].typ == 1:
                                al.pop(j)
                        g.updatemissile(
                            oldX, mis[i].y, mis[i].x, mis[i].y,
                            mis[i].sym, spc.sym)
            except IOError:
                if time.time() - t1 >= 10:
                    al.append(
                        alien(
                            random.randrange(
                                1, 4, 2), random.randint(
                                1, 15), "A"))
                    g.updatealien(al[0].xPos, al[0].yPos, al[0].sym)
                    al[len(al) - 1].start_tym = time.time()
                    al[len(al) - 1].end_tym = al[len(al) - 1].start_tym + 8
                    t1 = time.time()

                for i in range(len(al)):
                    if time.time() >= al[i].end_tym:
                        g.updatealien(al[i].xPos, al[i].yPos, ' ')
                        al.pop(0)

                if flag >= 0:
                    for i in range(flag):
                        oldX = mis[i].x
                        mis[i].x = mis[i].moveup(mis[i].x)
                        for j in range(len(al)):
                            var = mis[i].checkcollision(
                                mis[i].x, mis[i].y, al[j].xPos, al[j].yPos)
                            if var == 1 and mis[i].typ == 1:
                                mis[i].x = 0
                                score += 1
                                al[j].sym = ' '
                            if var == 1 and mis[i].typ == 2:
                                mis[i].x = 0
                                al[j].sym = '@'
                                al[j].end_tym = time.time() + 5
                            g.updatealien(al[j].xPos, al[j].yPos, al[j].sym)
                            if var == 1 and mis[i].typ == 1:
                                al.pop(j)
                        g.updatemissile(
                            oldX, mis[i].y, mis[i].x, mis[i].y,
                            mis[i].sym, spc.sym)
            time.sleep(0.2)
            os.system("clear")
            g.inv_print(score)
