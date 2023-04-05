# By Tomo Sato and Ian Turner

class Player:
  xpos = 0
  ypos = 0
  health = 10
  ammo = 100

  def __init__(self):
    self.xpos = 0
    self.ypos = 0
    self.health = 10
    self.ammo = 100

  def interactions(self):
    print(self.health)
    
  def attack(self):
    print(self.ammo)

  def movement(self):
    print(self.xpos, self.ypos)

  def isGameOver(self):
    if(self.health == 0):
      return True
    else:
      return False
