## Made By Reid Nguyen and Ian Turner

import pygame
import random


class NPC:
  xpos = 0
  ypos = 0
  canCollide = False
  frameRate = pygame.time.Clock()


  

  def __init__(self, targetPointX, targetPointY, playerPos):
    sides = random.randint(0,3)
    if sides == 0:
      self.startPoint = [random.randint(320,640),0]
    elif sides == 1:
      self.startPoint = [random.randint(0,640),640]
    elif sides == 2:
      self.startPoint = [0,random.randint(320,640)]
    else:
      self.startPoint = [640,random.randint(0,640)]
    self.xpos = self.startPoint[0]
    self.ypos = self.startPoint[1]
    self.targetPoint = (targetPointX, targetPointY)
    self.playerPos = playerPos  
    self.canCollide = False
    self.frameRate = pygame.time.Clock()

  def move(self):
    self.xpos += (self.playerPos[0] - self.startPoint[0]) /1000 * (1 + self.frameRate.get_time())
    self.ypos += (self.playerPos[1] - self.startPoint[1]) /1000 * (1 + self.frameRate.get_time())

  def colDet(self, bullet):
    if (bullet.xpos  >= self.xpos - 65 and bullet.xpos <= self.xpos + 65 and bullet.ypos >= self.ypos - 65 and bullet.ypos <= self.ypos + 65):
      return True
    else:
      return False

