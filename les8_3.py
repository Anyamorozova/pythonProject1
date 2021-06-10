class My_exception(Exception):
    def __init__(self, txt):
        self.txt = txt

lst_num = []
while True:
  if input('Выход - stop, \nЛюбая клавиша - продолжить.').lower() == 'stop':
    print(f"Ваш список: {lst_num}")
    break
  number = input('Введите число:')
  try:
    if number.isdigit() == False:
        raise My_exception("Вы ввели не число!")
  except My_exception as err:
    print(err)
  else:
    lst_num.append(number)
    print(f"Ваш список: {lst_num}")
