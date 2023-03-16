class Item:
  doesDamage = False
  fireRange = 5

  def __init__(self):
    self.doesDamage = False
    self.fireRange = 5

  def itemAbility(self):
    print(self.doesDamage)

  def collisionDetection(self):
    print(self.fireRange)