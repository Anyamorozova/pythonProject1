def sum_number(arg, summa):
  flag = True
  for i in arg:
    if i.isdigit() == True:
      summa += int(i)
    elif i.upper() == 'Q':
      flag = False
      return summa, flag
  return summa, flag

summa = 0
while True:
  if input('Выход - Q, \nЛюбая клавиша - продолжить.').upper() == 'Q':
    break
  numbers = input('Введите строку чисел, разделенных пробелом: ')
  numbers = numbers.split()
  result = sum_number(numbers, summa)
  summa = result[0]
  print(f'Сумма чисел равна {summa}')
  if result[1] == False:
    break
