import pygame
from pygame.locals import *
from itertools import count
import math

# initialize pygame
pygame.init()

# set up the screen
width = 1000
height = 1000
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
    def pos(self):
        return pygame.Vector2(self.x,self.y)

def clear():
    screen.fill(black)    

def draw():
    clock.tick(FPS)
    pygame.display.flip()

class Camera:
    def __init__(self,players):     
        self.players = players

    # I want to fit all of the players inside of the box of the camera
    def getBoxSize(self):
        # TODO: n players
        # I think to do n players I would need to calculate the max and min values from the midpoint
        # for both the x and y direction

        
        # for now just get the difference between p1 and p2
        players = self.players
        pos1 = players[0].pos()
        pos2 = players[1].pos()
        distance = pos1.distance_to(pos2)
        return max(distance, 200)

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

    p1 = Player(width/2 +  0,height/2, red)
    p2 = Player(width/2 + 50,height/2, green)

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
        
        padding = 100
        boxSize = c1.getBoxSize() + padding
        
        # draw the midpoint of the camera
        posX = c1.getMidpoint()[0] - boxSize/2
        posY = c1.getMidpoint()[1] - boxSize/2
        pygame.draw.rect(screen, blue, (posX,posY, boxSize, boxSize),1)
        
        draw()
        
    pygame.quit()

if __name__ == "__main__":
    main()
