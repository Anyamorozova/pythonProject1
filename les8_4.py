class Warehouse():
  
  def __init__(self):
    pass
     
     
class Office_equipment(Warehouse):
  
  title = None
  price = 0
  
  def __init__(self, title, price):
    self.title = title
    self.price = price

class Printer(Office_equipment):
  
  laser = None
  
  def __init__(self, title, price, laser):
    super().__init__(title, price)
    self.laser = laser


class Scanner(Office_equipment):
  
  hand_held = None
  
  def __init__(self, title, price, hand_held):
    super().__init__(title, price)
    self.hand_held = hand_held
    
    
class Xerox(Office_equipment):
  
  color = None
  
  def __init__(self, title, price, color):
    super().__init__(title, price)
    self.color = color
    
    
printer = Printer("HP LaserJet", 7000, True)
print(printer.__dict__)
scanner = Scanner("HP ScanJet", 5000, False)
print(scanner.__dict__)
xerox = Xerox("WorkCenter", 10000, "Black-white")
print(xerox.__dict__)
