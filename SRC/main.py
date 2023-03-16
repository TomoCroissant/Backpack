import pygame, sys
from pygame.locals import QUIT
from Inventory import Inventory
from Item import Item
from Room import Room
from Player import Player
from NPC import NPC

text = False
play = True

def makeSave():
  print("makeSave")

def loadSave():
  print("loadSave")

def drawRoom():
  print("drawRoom")

def drawPlayer():
  print("drawPlayer")

def drawNPC():
  print("drawNPC")

def drawItem():
  print("drawItem")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
  