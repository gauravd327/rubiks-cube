import json
import pygame
from cube import Cube

pygame.init() 

screen_width = 750
screen_height = 550
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rubik's cube")


# Colors
RED = (255, 0, 0, 50)
GREEN = (0, 255, 0, 50)
BLUE = (0, 0, 255, 50)
YELLOW = (255, 255, 0, 50)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255, 50)
BLACK = (0, 0, 0, 50)


cube = Cube(3)
f = open("algorithms/pll.json")
data = json.load(f)
cube.rotate("R B2 U2 B2 D F2 L2 R2 D B2 D2 L' U' R U' R B2 F' D' B'")

def convertCol(con):
    if con == "green":
        return GREEN
    
    elif con == "white":
        return WHITE
    
    elif con == "blue":
        return BLUE

    elif con == "yellow":
        return YELLOW

    elif con == "orange":
        return ORANGE

    elif con == "red":
        return RED

def drawBoard(startX, startY):
    offset = 160
    for i in range(4):
        drawFace(startX + (offset * i), startY, cube.getCube()[i])

    drawFace(startX + offset, startY + offset, cube.getCube()[4])
    drawFace(startX + offset, startY - offset, cube.getCube()[5])


def drawFace(startX, startY, face):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(win, convertCol(face[i][j].getColor()), (startX + (i * 50), startY + (j * 50), 40, 40))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cube.rotate(data['ua'])
            


    drawBoard(50, 200)
    pygame.display.update()
   
pygame.quit()
