## Made By Reid Nguyen

class NPC(object):
  isEnemy = False
  dialogue = 'Hello!'
  health = 10
  xpos = 0
  ypos = 0
  interaction = True

  def __init__(self):
    self.isEnemy = False
    self.dialogue = 'Hello!'
    self.health = 10
    self.xpos = 0
    self.ypos = 0
    self.interaction = True

  def attackType(self):
    print(self.xpos)

  def activateDialogue(self):
    print(self.dialogue)

  def quest(self):
    print(self.interaction)

  def characterType(self):
    print(self.isEnemy)

  def isDead(self):
    if(self.health == 0):
      return True
    else:
      return False
