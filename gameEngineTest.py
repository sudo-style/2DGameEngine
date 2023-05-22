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

    '''def handleInput(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == LEFT: self.x -= 1
                if event.key == RIGHT: self.x += 1'''

def clear():
    screen.fill(black)    

def draw():
    # draw
    clock.tick(FPS)
    pygame.display.flip()


def main():
    time =  0
  
    keepGoing = True

    p1 = Player(50,50, red)
    p2 = Player(20,50, green)

    players = [p1,p2]
    #c1 = Camera(players)
    
    while keepGoing:
        for event in pygame.event.get():
            if event.type == QUIT:
                keepGoing = False

        # pretty bad but just in testing phase
        keysPressed = pygame.key.get_pressed()
        if keysPressed[K_a]:    p1.moveLeft()
        if keysPressed[K_w]:    p1.moveUp()
        if keysPressed[K_d]:    p1.moveRight()
        if keysPressed[K_s]:    p1.moveDown()
        if keysPressed[K_LEFT]: p2.moveLeft()
        if keysPressed[K_RIGHT]: p2.moveRight()
        if keysPressed[K_UP]:   p2.moveUp()
        if keysPressed[K_DOWN]: p2.moveDown()
                    
        clear()
        p1.draw()
        p2.draw()        
        draw()
        
    pygame.quit()

if __name__ == "__main__":
    main()
