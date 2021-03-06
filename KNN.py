import pygame
import math, random

pygame.init()

xy = 800
blueV = 0
blueCounter = 0
redV = 0
redCounter = 0
positions = []
neighbours = []
NNlist = []
firstTime = True

win = pygame.display.set_mode((xy, xy))
win.fill((255, 255, 255))


def loading():
    print('making new Point...')
    pygame.time.wait(400)
    print('_____')
    pygame.time.wait(400)
    print('|____')
    pygame.time.wait(400)
    print('||___')
    pygame.time.wait(400)
    print('|||__')
    pygame.time.wait(400)
    print('||||_')
    pygame.time.wait(400)
    print('|||||')


def yn(a, c):
    # decide if something, whether float or int is the same number
    b = a // c
    bb = a / c
    if b - bb == 0:
        return True
    else:
        return False


def drawOI(win, center, color, OI, endpos=()):
    """Draws a either a line or a point on the screen, with color being randomly 1 (RED) or 0 (BLUE) by randPos()"""
    if color == 1 and OI == 'O':
        pygame.draw.circle(win, (255, 0, 0), center, 7, 20)
    elif color == 1 and OI == 'I':
        pygame.draw.line(win, (255, 0, 0), center, endpos, width=1)
    elif color == 0 and OI == 'O':
        pygame.draw.circle(win, (0, 0, 255), center, 7, 20)
    else:
        pygame.draw.line(win, (0, 0, 255), center, endpos, width=1)


def euclidian(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)


def randPos(lis):
    for _ in range(0, 200):
        lis.append((_, [random.randrange(0, stop=xy - 15), random.randrange(0, stop=xy - 15), random.randint(0, 1), 0]))


def makeNewPoint():
    """makes a new point"""
    # loading()
    ls = [random.randint(15, xy - 15), random.randrange(15, stop=xy - 15)]
    return ls


newposition = makeNewPoint()  # newposition is just a list with coordinates and a third value added later for color


def addDistance(point):
    """this checks the distance between the new point and every other point"""
    for n in range(0, len(positions)):
        positions[n][1][3] = euclidian(point[0], point[1], positions[n][1][0], positions[n][1][1])
        # every position now receives a distance value to the new point


def redrawGameWin(neighbours):
    global firstTime

    for foo in positions:
        drawOI(win, (foo[1][0], foo[1][1]), foo[1][2], 'O')
        # draw at the given coordinates (foo[1][0], foo[1][1]) with foo[1][2] being the deciding factor for color
    pygame.draw.circle(win, (0, 0, 0), (newposition[0], newposition[1]), neighbours[-1][1][3], width=1)
    if firstTime:
        pygame.draw.circle(win, (0, 255, 0), (newposition[0], newposition[1]), 7, 20)
        for n in neighbours:
            drawOI(win, (newposition[0], newposition[1]), n[1][2], 'I', endpos=(n[1][0], n[1][1]))
        pygame.display.update()
        pygame.time.wait(6000)
    elif not firstTime:
        drawOI(win, (newposition[0], newposition[1]), newposition[2], 'O')

    pygame.display.update()
    firstTime = False


def main():
    global redV, blueV, redCounter, blueCounter
    randPos(positions)
    addDistance(newposition)
    neighbours = input("amount of nearest neighbours (2-200): ")
    positions.sort(key=lambda x: x[1][3])  # Sort the positions based on their distance to the new point
    neighbours = positions[:int(neighbours)]

    # Adds up the distance to all of the blue and red points separately
    for ne in neighbours:
        if ne[1][2] == 1:
            redV += ne[1][3]
            redCounter += 1
        else:
            blueV += ne[1][3]
            blueCounter += 1
    # The lowest of the two added up distance values is the winner of the classification
    if redV / redCounter**2 > blueV / blueCounter**2:
        newposition.append(0)
    else:
        newposition.append(1)

    print(blueV, redV)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawGameWin(neighbours)


main()
