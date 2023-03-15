from item import Item

class Inventory:
  Items = Item[10]

  def __init__(self):
    self.Items = Item[10]
  
  def recordItemAbility(self):
    print(self.Items)
