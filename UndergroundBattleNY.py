'''
Created on Nov 28, 2017

@author:iliketurtles
'''
import pygame
import sys, os, math
from pygame import *
from random import randint
from spriteHelper import SpriteSheet

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GAMENAME = "Underground Battle NY"
FRAMERATE = 60
BGCOLOR = (255,255,255)
#RED = (255,0,0)
#GREEN = (0,255,0)
#BLUE = (0,0,255)
#BLACK = (0,0,0)
#WHITE = (255,255,255)
#These are for quick color access


class Player:
    '''Description: Class used to identify the player'''
    ########## VARIABLES ##########
    x = 0
    y = 0
    vX = 0
    vY = 0
    collider = None
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        self.image = SpriteSheet("p2_front (1).png")
        self.image = self.image.get_image(0,0,66,92)
    ########## MAIN FUNCTION ##########
    def draw(self,surface):
        '''Draws the player sprite on the screen'''
        surface.blit(self.image,(self.x,self.y))
    
    def getCollider(self):
        '''Returns a rectangle area representing the player sprite'''
        pass

    def getCenter(self):
        rect = self.image.get_rect()
        print(rect.x,rect.y)
        return (rect.w/2,rect.h/2)
    def process(self,delta):
        self.x += self.vX*delta
        self.vY += .002*delta
        self.y += self.vY*delta + 8
        #Here X and Y cannot be used because it will cause the computer to use
        #the coordinates (0,0) on the rectangle

class Game:
    ########## VARIABLES ##########
    score = 0
    levels = []
    topScores = []
    player = None
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        self.player = Player()
    ########## MAIN FUNCTION ##########
    def main(self):
        playing = True
        centerOfScreen = self.getCenterOfScreen()
        centerOfPlayer = self.player.getCenter()
        self.player.x = centerOfScreen[0]-centerOfPlayer[0]
        self.player.y = centerOfScreen[1]-centerOfPlayer[1]
        
    ########## GAME LOOP ##########
        while playing:
            delta = self.clock.tick(FRAMERATE)
            #Forces the actions in a game to always move the same speed
            #and reach the same outcome regardless of how fast one's computer
            #is
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        #JUMP
                        self.player.vY=-1
            self.processLogic(delta)
            self.drawScreen()
            pygame.display.flip()
    def quit(self):
        pygame.quit()
        sys.exit()
               
    def processLogic(self,delta):
        self.player.process(delta)
    
    def drawScreen(self):
        self.surface.fill(BGCOLOR)
        #Constantly fills the screen with white every frame
        
        self.player.draw(self.surface)
                
    def getCenterOfScreen(self):
        return(WINDOWWIDTH/2,WINDOWHEIGHT/2)
    
if __name__=='__main__':
    game = Game()
    game.main()
    
class Levels:
    ########## VARIABLES ##########
    
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    
    ########## MAIN FUNCTION ##########
        
class Animation(NPC,Hazards,Collectables,Platforms,Interface,Buttons, \
                Destructables):
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Platforms:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Interface:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Buttons:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class NPC(Player):
    ########## VARIABLES ##########
    dead = False
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Collectables:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Hazards:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
    
class Destructables:
    ########## VARIABLES ##########
    
    ########## CONSTRUCTOR ##########
    def __init__(self):
        pass
    ########## MAIN FUNCTION ##########
