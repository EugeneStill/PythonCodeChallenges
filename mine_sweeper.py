import random
kMine = 9
class Matrix():
  def __init__(self, T):
    self.elem_type = T
  def resize(self, rows, cols):
    self.data = [self.elem_type() for _ in range(rows * cols)]
    self.rows, self.cols = rows, cols
  def at(self, row, col):
    return self.data[row * self.cols + col]
  def rows(self):
    return self.rows
  def cols(self):
    return self.cols
class MineField():
  class Spot():
    def __init__(self):
      self.value = 0
      self.visible = False
  def _spot(self):
    return self.Spot()
  def __init__(self, rows, cols, num_mines):
    self.matrix = Matrix(self._spot)
    self.matrix.resize(rows, cols)
    self.rows, self.cols = rows, cols
    if num_mines > rows * cols:
      print("Too many mines")
    mine_list = [i < num_mines for i in range(rows * cols)]
    random.shuffle(mine_list)
    print(mine_list)
    for index, is_mine in enumerate(mine_list):
      if not is_mine:
        continue
      row, col = index // cols, index % cols
      self.matrix.at(row, col).value = kMine
      for i in range(-1, 2):
        for j in range(-1, 2):
          if row + i < 0 or row + i >= rows or col + j < 0 or col + j >= cols:
            continue
          if self.matrix.at(row + i, col + j).value == kMine:
            continue
          self.matrix.at(row + i, col + j).value += 1
  def OnClick(self, row, col):
    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
      return False
    spot = self.matrix.at(row, col)
    if spot.visible:
      return False
    spot.visible = True
    if spot.value == kMine:
      print("Boom!!!!")
      return True
    if spot.value != 0:
      return False
    self.OnClick(row - 1, col)
    self.OnClick(row, col - 1)
    self.OnClick(row + 1, col)
    self.OnClick(row, col + 1)
    return False
  def Print(self, show_hidden=False):
    for i in range(self.rows):
      for j in range(self.cols):
        ch = '.'
        if self.matrix.at(i, j).visible or show_hidden:
          ch = self.matrix.at(i, j).value
        print(ch, end=' ')
      print() # row end character
    print("\n\n") # breaks between matrices

if __name__ == '__main__':
  mine_field = MineField(12, 10, 7)
  mine_field.Print(True)
  mine_field.OnClick(5, 2)
  mine_field.Print()
  mine_field.OnClick(2, 6)
  mine_field.Print()
  mine_field.OnClick(9, 3)
  mine_field.Print()
  mine_field.OnClick(0, 0)
  mine_field.Print()
  mine_field.OnClick(3, 5)
  mine_field.Print()