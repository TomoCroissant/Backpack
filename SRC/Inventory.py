from Item import Item

class Inventory:
  Items = [Item, Item]

  def __init__(self):
    self.Items[0] = Item
    self.Items[1] = Item
  
  def recordItemAbility(self):
    print(self.Items)
