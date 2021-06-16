class Warehouse():
  
  dict_equipment = {}
  sub_equipment = {}
  
  def __init__(self):
    pass
     
  def intput_equipment(self, equipment, count):
    temp = self.dict_equipment.get(equipment)
    if temp == None:
      self.dict_equipment.update({equipment: count})
    else:
      self.dict_equipment.update({equipment: count + temp})
    return self.dict_equipment
    
  def output_equipment(self, subdivision, equipment, count):
    temp = self.dict_equipment.get(equipment)
    temp_sub = self.sub_equipment.get(subdivision)
    self.dict_equipment.update({equipment: temp - count})
    if temp_sub == None:
      self.sub_equipment.update({subdivision: {equipment: count}})
    else:
      if temp_sub.get(equipment) == None:
        temp_sub.update({equipment: count})
      else:
        temp_sub.update({equipment: count + temp_sub.get(equipment)})
      self.sub_equipment[subdivision] = temp_sub
    return self.sub_equipment
    
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
#print(printer.__dict__)
scanner = Scanner("HP ScanJet", 5000, False)
#print(scanner.__dict__)
xerox = Xerox("WorkCenter", 10000, "Black-white")
#print(xerox.__dict__)
warehouse = Warehouse()
warehouse.intput_equipment("Printer", 20)
warehouse.intput_equipment("Scanner", 40)
print(f"После приемки техники: {warehouse.dict_equipment}")
warehouse.output_equipment("Office", "Scanner", 20)
warehouse.output_equipment("Office", "Scanner", 20)
warehouse.output_equipment("Office", "Printer", 20)
print(f"После передачи техники: {warehouse.dict_equipment}")
