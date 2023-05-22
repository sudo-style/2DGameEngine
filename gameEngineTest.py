import pygame
from pygame.locals import *
from itertools import count
import math

# initialize pygame
pygame.init()

# set up the screen
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("gameEngineTest")
clock = pygame.time.Clock()
FPS = 60

# colors
white = (255, 255, 255)
black = (0, 0, 30)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


playerKeys = [K_LEFT,K_RIGHT,K_UP,K_DOWN]

class Player:
    _ids = count(0)
    def __init__(self,x,y, color = red):
        self.x = x
        self.y = y
        self.pWidth = 10 # this is the size of the sprite or whatever
        self.pHeight = 10
        self.color = color
        self.player = self._ids

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.pWidth, self.pHeight)
        pygame.draw.rect(screen, self.color, rect)

    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y

    def moveLeft(self):
        self.x -= 3

    def moveRight(self):
        self.x += 3

    def moveUp(self):
        self.y -= 3

    def moveDown(self):
        self.y += 3

def clear():
    screen.fill(black)    

def draw():
    # draw
    clock.tick(FPS)
    pygame.display.flip()

class Camera:
    def __init__(self,players):     
        self.players = players

    # I want to fit all of the players inside of the box of the camera
    def getBoxSize(self):
        # it will need to get the distance of the players
        # but how would that work if I have 3 players?

        # just have it for 2 for now

        

    def getMidpoint(self):
        # this sums all of the x's and all of the y's of the players
        cordX = [player.x for player in self.players]
        cordY = [player.y for player in self.players]
        # then find the average to find the midpoint
        midpointX = sum(cordX)/len(cordX)
        midpointY = sum(cordY)/len(cordY)
        midpoint = (midpointX,midpointY)
        return midpoint

def main():
    time =  0
  
    keepGoing = True

    p1 = Player(50,50, red)
    p2 = Player(20,50, green)

    players = [p1,p2]
    c1 = Camera(players)
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == QUIT:
                keepGoing = False

        # pretty bad but just in testing phase
        keysPressed = pygame.key.get_pressed()
        if keysPressed[K_w]:    p1.moveUp()
        if keysPressed[K_s]:    p1.moveDown()
        if keysPressed[K_a]:    p1.moveLeft()
        if keysPressed[K_d]:    p1.moveRight()
        if keysPressed[K_UP]:   p2.moveUp()
        if keysPressed[K_DOWN]: p2.moveDown()
        if keysPressed[K_LEFT]: p2.moveLeft()
        if keysPressed[K_RIGHT]: p2.moveRight()                    

        clear()
        
        for player in players:
            player.draw()
        

        # draw the midpoint of the camera
        posX = c1.getMidpoint()[0] - 100
        posY = c1.getMidpoint()[1] - 100
        pygame.draw.rect(screen, blue, (posX,posY, 200,200),1)
        
        draw()
        
    pygame.quit()

if __name__ == "__main__":
    main()
