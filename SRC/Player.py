# By Tomo Sato, Ian Turner, and Reid Nguyen

class Player:
  xpos = 0
  ypos = 0
  health = 5
  ammo = 100

  def __init__(self):
    self.xpos = 0
    self.ypos = 0
    self.health = 5
    self.ammo = 100

      
## Colision Detection
  def colDet(self, NPC):
    if (NPC.xpos  >= self.xpos - 50 and NPC.xpos <= self.xpos + 50 and NPC.ypos >= self.ypos - 50 and NPC.ypos <= self.ypos + 50):
      return True
    else:
      return False