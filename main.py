import sys
import pygame as pg
from pygame import gfxdraw
from pygame.locals import QUIT
from const import *
from Hexagon import *   

def drawRect(pos, height, boardSize):
    x, y = pos
    pg.draw.polygon(screen, RED, [(x,y), (x, y+height), (x+height-height/boardSize, y+height/2), (x+height-height/boardSize ,y+height/2+height)])
    pg.draw.polygon(screen, BLUE, [(x,y), (x+height-height/boardSize, y+height/2), (x, y+height), (x+height-height/boardSize, y+height/2+height)])


pg.init()
pg.display.set_caption('Draw')
screen = pg.display.set_mode((W, H))
screen.fill(WHITE)
x, y = STARTPOS
coordinate = [[0 for i in range(TILES)] for j in range(TILES)]
for i in range(TILES):
    distance = 0
    for j in range(TILES):
        coordinate[i][j] = Hexagon(HEXRADIUS, (x, y+distance))
        distance += coordinate[i][j].minimalRadius * 2
    x, y = coordinate[i][0].findNextPoint()
x, y = STARTPOS
drawRect((x-2*coordinate[0][0].minimalRadius, y - 4 * coordinate[0][0].minimalRadius), coordinate[0][0].minimalRadius * (TILES+2) * 2, TILES)


while True:

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()    
    for col in range(TILES):
        for row in range(TILES):
            if coordinate[col][row].state == 0:
                coordinate[col][row].fillHexagon(screen, WHITE)
                coordinate[col][row].render(screen)
                if coordinate[col][row].inHexagon(pg.mouse.get_pos()):
                    if PLAYER == 1:
                        coordinate[col][row].fillHexagon(screen, RED)
                        coordinate[col][row].render(screen)
                    else:
                        coordinate[col][row].fillHexagon(screen, BLUE)
                        coordinate[col][row].render(screen)

    if event.type == pg.MOUSEBUTTONDOWN:
        for col in range(TILES):
            for row in range(TILES):
                if coordinate[col][row].inHexagon(pg.mouse.get_pos())\
                    and coordinate[col][row].state == 0:
                        if PLAYER == 1:
                            coordinate[col][row].fillHexagon(screen, RED)
                            coordinate[col][row].render(screen)
                            coordinate[col][row].captured(PLAYER)
                            print("Red capture ("+str(col)+","+str(row)+")")
                        else:
                            coordinate[col][row].fillHexagon(screen, BLUE)
                            coordinate[col][row].render(screen)
                            coordinate[col][row].captured(PLAYER)
                            print("Blue capture ("+str(col)+","+str(row)+")")
                        PLAYER = 3 - PLAYER

    pg.display.update()