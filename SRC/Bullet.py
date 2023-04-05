# By Ian Turner

import pygame


class Bullet:
  xpos = 0
  ypos = 0
  canCollide = False
  frameRate = pygame.time.Clock()

  def __init__(self, targetPointX, targetPointY, playerPos):
    self.xpos = playerPos.x
    self.ypos = playerPos.y
    self.targetPoint = (targetPointX, targetPointY)
    self.playerPos = playerPos
    self.startPoint = (playerPos.x, playerPos.y)
    self.canCollide = False
    self.frameRate = pygame.time.Clock()

  def move(self):
    self.xpos += (self.targetPoint[0] - self.startPoint[0]) /500 * (1 + self.frameRate.get_time())
    self.ypos += (self.targetPoint[1] - self.startPoint[1]) /500 * (1 + self.frameRate.get_time())

  def invert(self, newPos):
    self.targetPoint = newPos
    self.startPoint = (self.xpos, self.ypos)
    self.canCollide = True