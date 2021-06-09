class Cell:
  
    count_cell = None
    
    def __init__(self, count_cell):
      self.count_cell = count_cell
      
    def __str__(self):
      return str(self.count_cell)
    
    def __add__(self, other):
      return Cell(self.count_cell + other.count_cell)
      
    def __sub__(self, other):
      if self.count_cell > other.count_cell:
        return Cell(self.count_cell - other.count_cell)
      else:
        return "Ошибка, вычитание невозможно."
        
    def __mul__(self, other):
      return Cell(self.count_cell * other.count_cell)
      
    def __floordiv__(self, other):
      return Cell(self.count_cell // other.count_cell)
      
    def make_order(self, number_cell_row):
      str_, i, arg = "", self.count_cell // number_cell_row, self.count_cell % number_cell_row
      while(i>0):
        for _ in range(number_cell_row):
          str_ += "*"
        str_ += r"\n"
        i -= 1
      if arg != 0:
        for _ in range(arg):
          str_ += "*"
      else:
        str_ = str_[:-2]
      return str_ 
      
cell_1 = Cell(3)
cell_2 = Cell(12)
print(cell_2.make_order(5), cell_1 + cell_2, cell_2 // cell_1, cell_1 * cell_2, cell_1 - cell_2)
