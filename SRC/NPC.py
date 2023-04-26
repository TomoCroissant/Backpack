## Made By Reid Nguyen and Ian Turner

import pygame
import random


class NPC:
  xpos = 0
  ypos = 0
  canCollide = False
  frameRate = pygame.time.Clock()

  def __init__(self, targetPointX, targetPointY, playerPos):
    self.xpos = 400
    self.ypos = 400
    self.targetPoint = (targetPointX, targetPointY)
    self.playerPos = playerPos
    self.startPoint = (400, 400)
    self.canCollide = False
    self.frameRate = pygame.time.Clock()

  def move(self):
    self.xpos += (self.playerPos[0] - self.startPoint[0]) /1000 * (1 + self.frameRate.get_time())
    self.ypos += (self.playerPos[1] - self.startPoint[1]) /1000 * (1 + self.frameRate.get_time())

  def colDet(self, bullet):
    if (bullet.xpos  >= self.xpos - 50 and bullet.xpos <= self.xpos + 50 and bullet.ypos >= self.ypos - 50 and bullet.ypos <= self.ypos + 50):
      return True
    else:
      return False


  # def startPos(self):
  #   side = random.randint(1, 4)
  #     if():
  
  # def invert(self, newPos):
  #   self.targetPoint = newPos
  #   self.startPoint = (400,400)
  #   self.canCollide = True