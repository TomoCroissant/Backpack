# By Tomo Sato, Ian Turner, Reid Nguyen

import pygame, sys
from pygame.locals import QUIT
from Player import Player
from NPC import NPC
from Bullet import Bullet

player = Player()
roomNum = 1
text = False
play = True
endScreen = False
canShoot = True
boomerangHit = False
frameRate = pygame.time.Clock()
baseFPS = 60
score = 0
highScore = 0
enemyTimer = 0

spriteSize = 100
playerSprite = pygame.image.load('james2.png')
playerSprite = pygame.transform.scale(playerSprite, (spriteSize, spriteSize))

boomerang1 = pygame.image.load('boomerang1.png')
boomerang1 = pygame.transform.scale(boomerang1, (50, 50))

enemyImage = pygame.image.load('shroom.png')
enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))

room1 = pygame.image.load('room1.png')
room1 = pygame.transform.scale(room1, (1280, 1280))
room2 = pygame.image.load('subManMap.png')
room2 = pygame.transform.scale(room2, (1280, 1280))
room3 = pygame.image.load('chrisMap.png')
room3 = pygame.transform.scale(room3, (1280, 1280))
room4 = pygame.image.load('FlymanMap.png')
room4 = pygame.transform.scale(room4, (1280, 1280))
room5 = pygame.image.load('EvilJamesMap.png')
room5 = pygame.transform.scale(room5, (1280, 1280))


def makeSave():
  save = open("SaveData.txt", "w")
  save.write(str(highScore))
  save.close()

#accesses high score
save = open("SaveData.txt", "r")
contents = save.readlines()
save.close()
highScore = int(contents[0])
print("High Score:", contents[0])

def drawRoom():
  if(roomNum == 1):
    screen.blit(room1, (0, 0))
  elif(roomNum == 2):
    screen.blit(room2, (0, 0))
  elif(roomNum == 3):
    screen.blit(room3, (0, 0))
  elif(roomNum == 4):
    screen.blit(room4, (0, 0))
  elif(roomNum == 5):
    screen.blit(room5, (0, 0))
  else:
    screen.blit(room1, (0, 0))
    

pygame.init()
screen = pygame.display.set_mode((1280, 1280))
clock = pygame.time.Clock()
running = False
B1 = Bullet(-10, -10, pygame.Vector2(-10, -10))
Enemies = []


def drawPlayer(x, y):
  screen.blit(playerSprite, (x - spriteSize / 2, y - spriteSize / 2))





#main menu
while play:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False
      pygame.quit()
      sys.exit()
  
  screen.fill("blue")
  font = pygame.font.Font('FontdinerSwanky.ttf', 32)
  text = font.render('Press mouse to begin. Highscore: ' + str(highScore), True , "green", "blue")
  textRect = text.get_rect()
  textRect.center = (1280 // 2, 1280 // 2)
  screen.blit(text, textRect)
  pygame.display.update()
  if (pygame.mouse.get_pressed() == (1, 0, 0)):
    for var in Enemies:
          Enemies.remove(var)
    running = True

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
    if keys[pygame.K_s] and player_pos.y < 1279:
      player.ypos += 0.5 * (1 + frameRate.get_time())
    if keys[pygame.K_a] and player_pos.x > 1:
      player.xpos -= 0.5 * (1 + frameRate.get_time())
    if keys[pygame.K_d] and player_pos.x < 1279:
      player.xpos += 0.5 * (1 + frameRate.get_time())
  
  
  
  
    if (enemyTimer <= 0):
      Enemies.append(
        NPC((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos))
      enemyTimer = 1000
    if (pygame.mouse.get_pressed() == (1, 0, 0) and canShoot):
      # B1.xpos = player_pos.x
      # B1.ypos = player_pos.y
      # B1.targetPointX = pygame.mouse.get_pos()[0]
      # B1.targetPointY = pygame.mouse.get_pos()[1]
      # B1.playerPos = player_pos
      
      B1 = Bullet((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),player_pos)
      canShoot = False
  
    B1.move()
    B1.frameRate.tick(baseFPS)
    screen.blit(boomerang1, (B1.xpos, B1.ypos))
    if (B1.ypos >+ 1280 or B1.ypos <+ 0 or B1.xpos >+ 1280 or B1.xpos <+ 0):
      if (boomerangHit == False):
        B1.invert(player_pos)
        boomerangHit = True
      else:
        #B1 = Bullet(-10, -10, [-10,-10])
        boomerangHit = False
    for var in Enemies:
      NPC.move(var)
      var.playerPos = player_pos
      var.frameRate.tick(baseFPS)
      screen.blit(enemyImage, (var.xpos, var.ypos))
      if(player.colDet(var)):
        player.xpos = 0
        player.ypos = 0
        running = False
      if (var.colDet(B1)):
            Enemies.remove(var)
            score += 1
            if(highScore < score):
              highScore = score
            makeSave()
            if(score >= 15):
              running = False
              endScreen = True
            elif(score >= 12):
              roomNum = 5
              enemyImage = pygame.image.load('EvilJames.png')
              enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
            elif(score >= 9):
              roomNum = 4
              enemyImage = pygame.image.load('flyman.png')
              enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
            elif(score >= 6):
              roomNum = 3
              enemyImage = pygame.image.load('ChrisFullBody.png')
              enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
            elif(score >= 3):
              roomNum = 2
              enemyImage = pygame.image.load('subarine man.png')
              enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
            else:
              enemyImage = pygame.image.load('shroom.png')
              enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
              roomNum = 1
            
  
    font2 = pygame.font.Font('FontdinerSwanky.ttf', 32)
    text2 = font2.render('Score: ' + str(score), True, "green", "blue")
    textRect2 = text2.get_rect()
    textRect2.center = (1000, 28)
    screen.blit(text2, textRect2)

    # font3 = pygame.font.Font('FontdinerSwanky.ttf', 32)
    # text3 = font3.render('High Score: ' + str(highScore), True, "green", "blue")
    # textRect3 = text3.get_rect()
    # textRect3.center = (1125, 28)
    # screen.blit(text3, textRect3)
    
    pygame.display.update()
    enemyTimer -= (1 + frameRate.get_time())
  while endScreen:
    screen.fill("blue")
    font = pygame.font.Font('FontdinerSwanky.ttf', 16)
    text3 = font.render('Mushroom Man: You will never be free of me.', True, "green", "blue")
    text4 = font.render('Submarine Man: I\'ll always bring you down.', True, "green", "blue")
    text5 = font.render('Chris: Try and try, you\'ll never forget me.', True, "green", "blue")
    text6 = font.render('Flyman: The world is always bleak.', True, "green", "blue")
    text7 = font.render('Evil James: You are nothing without me.', True, "green", "blue")
    text8 = font.render('James: No. You won\'t be coming back to me.', True, "red", "blue")
    textRect3 = text3.get_rect()
    textRect3.center = (640 // 2, 100)
    screen.blit(text3, textRect3)
    textRect4 = text4.get_rect()
    textRect4.center = (640 // 2, 200)
    screen.blit(text4, textRect4)
    textRect5 = text5.get_rect()
    textRect5.center = (640 // 2, 300)
    screen.blit(text5, textRect5)
    textRect6 = text6.get_rect()
    textRect6.center = (640 // 2, 400)
    screen.blit(text6, textRect6)
    textRect7 = text7.get_rect()
    textRect7.center = (640 // 2, 500)
    screen.blit(text7, textRect7)
    textRect8 = text8.get_rect()
    textRect8.center = (640 // 2, 600)
    screen.blit(text8, textRect8)
    pygame.display.update()
    if (pygame.mouse.get_pressed() == (1, 0, 0)):
      for var in Enemies:
          Enemies.remove(var)
      enemyImage = pygame.image.load('shroom.png')
      enemyImage = pygame.transform.scale(enemyImage, (spriteSize, spriteSize))
      roomNum = 1
      score = 0
      running = True
    