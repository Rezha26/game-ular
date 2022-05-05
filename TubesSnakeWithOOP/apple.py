import pygame
import random

class apple():
    #return a (x,y)
    def __init__(self, screenwidth, screenheight, gridsize):
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gridsize = gridsize
        self.x = round(random.randrange(0, self.screenwidth - self.gridsize)/self.gridsize)*self.gridsize
        self.y = round(random.randrange(0, self.screenheight - self.gridsize)/self.gridsize)*self.gridsize
    
    def newloc(self, snake):
        badspawn = True
        while badspawn == True:
            self.x = round(random.randrange(0, self.screenwidth - self.gridsize)/self.gridsize)*self.gridsize
            self.y = round(random.randrange(0, self.screenheight - self.gridsize)/self.gridsize)*self.gridsize
            badspawn = False
            for position in snake.snakelist:
                if position[0] == self.x and position[1] == self.y:
                    badspawn = True
                    break
                else:
                    badspawn = False