## Made By Reid Nguyen and Ian Turner

import pygame
import random


class NPC:
  xpos = 0
  ypos = 0
  canCollide = False
  frameRate = pygame.time.Clock()

## StartPoint and Movment
  def __init__(self, targetPointX, targetPointY, playerPos):
    sides = random.randint(0,3)
    if sides == 0:
      self.startPoint = [random.randint(640,1280),0]
    elif sides == 1:
      self.startPoint = [random.randint(0,1280),1280]
    elif sides == 2:
      self.startPoint = [0,random.randint(640,1280)]
    else:
      self.startPoint = [1280,random.randint(0,1280)]
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

