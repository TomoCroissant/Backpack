class Room:
  sizeX = 10
  sizeY = 10
  roomNum = 1

  def __init__(self):
    self.sizeX = 10
    self.sizeY = 10
    self.roomNum = 1

  def roomBorder(self):
    print(self.sizeX, self.sizeY)

  def collisionDetection(self):
    print(self.roomNum)
