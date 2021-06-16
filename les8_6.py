class My_exception(Exception):
    def __init__(self, txt):
        self.txt = txt


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
    
    
while True:
  warehouse = Warehouse()
  if input('Выход - stop, \nЛюбая клавиша - продолжить.').lower() == 'stop':
    break
    
  int_data = input('Введите, в соответствии с обозначениями, через пробел, что привезли на склад и в каком количестве. \n Обозначения: S - сканер, P - принтер, X - ксерокс \n')
  try:
    if len(int_data) < 3:
        raise My_exception("Вы ввели не все значения!")
        
    int_data = int_data.split()
    if int_data[1].isdigit() == False:
        raise My_exception("Вы ввели не число!")
  except My_exception as err:
    print(err)
  else:
    dict_ = {"S":"Scanner", "P":"Printer", "X": "Xerox"}
    for i, el in dict_.items():
      if int_data[0].upper() == i: 
        warehouse.intput_equipment(el, int_data[1])
        break
    else:
      print("Нет такого обозначения.")
    print(f" Оргтехника на складе: {warehouse.dict_equipment}")
