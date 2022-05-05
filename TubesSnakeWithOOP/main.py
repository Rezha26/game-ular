# -*- coding: utf-8 -*-


import pygame
import random
from snake import snake
from apple import apple
from pygame.locals import *

        
        
    
    
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

    
grass = pygame.image.load("assets/grass.png")

class game():
    black = (100,100,0)
    red = (200, 0, 0)
    green = (0, 200, 0)
    blue = (0, 0, 200)
    white = (240, 240, 240)
    #
    def __init__(self, screenwidth, screenheight, gridsize):
        pygame.init()
        self.running = True
        self.endgame = False
        self.pregame = True
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gridsize = gridsize
        self.display = pygame.display.set_mode((self.screenwidth, self.screenheight))
        pygame.display.set_caption('Snake')
        
        self.clock = pygame.time.Clock()
        self.snakespeed = 7
        
        self.snake = snake(self.display, self.gridsize)
        self.apple = apple(self.screenwidth, self.screenheight, self.gridsize)
        
    def game_loop(self):
        while self.running == True:
            for x in range(int(width/grass.get_width()+1)):
                for y in range(int(height/grass.get_height()+1)):
                    screen.blit(grass, (x*100, y*100))
            
            
            if self.pregame == True:
                while self.pregame == True:
                    self.display.fill(self.white)
                    self.message('Welcome to Snake! Press P to Play!', self.screenwidth/2, self.screenheight/2)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                self.pregame = False 
                                
            if self.endgame == True:
                while self.endgame == True:
                    self.display.fill(self.white)
                    self.message('You lost! Press P to play again or Q to quit.', self.screenwidth/2, self.screenheight/2)
                    self.scoremessage = ('Your final score was: ') + self.printscore
                    self.message(self.scoremessage, self.screenwidth/2, (self.screenheight/2 + 64))       
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                main()
                            if event.key == pygame.K_q:
                                self.running = False
                                pygame.quit()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                   
                    if event.key == pygame.K_RIGHT:
                        self.snake.turnright()
                    if event.key == pygame.K_LEFT:
                        self.snake.turnleft()
                    if event.key == pygame.K_UP:
                        self.snake.turnup()
                    if event.key == pygame.K_DOWN:
                        self.snake.turndown()
                    
            if self.snake.move() == False:
                self.endgame = True
            
            if self.boundarycollision() == True:
                self.endgame = True
            
            if self.applecollision() == True:
                self.snake.addsegment()
                self.apple.newloc(self.snake)
                
            self.display.fill(self.black)
            
            self.printscore = str(self.score())
            self.message(self.printscore, 32, 32)
            
            self.drawapple(self.apple)
            self.drawsnake(self.snake)
            
            pygame.display.flip()
            self.clock.tick(self.snakespeed)
            
            
    def drawsnake(self, snake):
        for segment in self.snake.snakelist:
            pygame.draw.rect(self.display, self.red, (segment[0], segment[1], snake.gridsize, snake.gridsize))
    
    def drawapple(self, apple):
        pygame.draw.rect(self.display, self.green, (self.apple.x, self.apple.y, apple.gridsize, apple.gridsize))
    def boundarycollision(self):
       if self.snake.x < 0 or self.snake.y < 0 or self.snake.x > self.screenwidth - self.gridsize or self.snake.y > self.screenheight - self.gridsize:
            return True
       else:
            return False
    
    def applecollision(self):
        if self.snake.x == self.apple.x and self.snake.y == self.apple.y:
            return True
        else:
            return False
     
    def message(self, message, x, y):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(message, True, self.green)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x,y)
        self.display.blit(self.text, self.textRect)

    def score(self):
        counter = 0
        for i in range(self.snake.snakelength):
            counter += 1
        return counter


def main():
    playgame = game(800, 600, 40)
    playgame.game_loop()
    
if __name__ == '__main__':
    main()
            
            
            
            
            
            
