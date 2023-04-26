# By Tomo Sato, Ian Turner

import pygame, sys
from pygame.locals import QUIT
from Player import Player
from NPC import NPC
from Bullet import Bullet

player = Player()
roomNum = 1
text = False
play = True
canShoot = True
boomerangHit = False
frameRate = pygame.time.Clock()
baseFPS = 60

spriteSize = 100
playerSprite = pygame.image.load('james2.png')
playerSprite = pygame.transform.scale(playerSprite, (spriteSize, spriteSize))

boomerang1 = pygame.image.load('boomerang1.png')
boomerang1 = pygame.transform.scale(boomerang1, (50, 50))

enemyImage = pygame.image.load('cat-world.png')
enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))

room1 = pygame.image.load('room1.png')
room1 = pygame.transform.scale(room1, (640, 640))


def makeSave():
  save = open("SaveData.txt", "w")
  save.write(str(player.xpos))  #playerX
  save.write("\n" + str(player.ypos))  #playerY
  save.write("\n" + str(roomNum))  #room number
  save.close()


def loadSave():  #to be coded
  save = open("SaveData.txt", "r")
  save.close()


def drawRoom():
  if (roomNum == 1):
    screen.blit(room1, (0, 0))
  else:
    screen.fill("green")


def drawNPC():
  print("drawNPC")


def drawItem():
  print("drawItem")


pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True
Bullets = []
Enemies = []


def drawPlayer(x, y):
  screen.blit(playerSprite, (x - spriteSize / 2, y - spriteSize / 2))




#main loop
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
      pygame.quit()
      sys.exit()

  frameRate.tick(baseFPS)
  drawRoom()

  player_pos = pygame.Vector2(player.xpos, player.ypos)
  
  drawPlayer(player_pos.x, player_pos.y)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] and player_pos.y > 1:
    player.ypos -= 0.5 * (1 + frameRate.get_time())
  if keys[pygame.K_s] and player_pos.y < 639:
    player.ypos += 0.5 * (1 + frameRate.get_time())
  if keys[pygame.K_a] and player_pos.x > 1:
    player.xpos -= 0.5 * (1 + frameRate.get_time())
  if keys[pygame.K_d] and player_pos.x < 639:
    player.xpos += 0.5 * (1 + frameRate.get_time())

  if (keys[pygame.K_h]):
    makeSave()

  if (pygame.mouse.get_pressed() == (1, 0, 0) and canShoot):
    Bullets.append(
      Bullet((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos))
    canShoot = False
    Enemies.append(
      NPC((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos))

  for var in Bullets:
    Bullet.move(var)
    var.frameRate.tick(baseFPS)
    # pygame.draw.image(screen, boomerang1, pygame.Vector2(var.xpos, var.ypos))
    screen.blit(boomerang1, (var.xpos, var.ypos))
    if (var.ypos > 1000 or var.ypos < -100 or var.xpos > 1000 or var.xpos < -100):
      if (boomerangHit == False):
        Bullet.invert(var, player_pos)
        boomerangHit = True
      else:
        Bullets.remove(var)
        boomerangHit = False
        canShoot = True
    for var in Enemies:
      NPC.move(var)
      var.frameRate.tick(baseFPS)
      # pygame.draw.image(screen, boomerang1, pygame.Vector2(var.xpos, var.ypos))
      screen.blit(enemyImage, (var.xpos, var.ypos))
      if (var.ypos > 640 or var.ypos < 0 or var.xpos > 640 or var.xpos < 0) or var.colDet(Bullets[0]):
          Enemies.remove(var)
  pygame.display.update()