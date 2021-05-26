season = ['зима', 'весна', 'лето', 'осень']
month_all = {1 : 'январь', 2 : 'февраль', 3 : 'март', 4 : 'апрель', 5 : 'май', 6 : 'июнь', 7 : 'июль', 8 : 'август', 9 : 'сентябрь', 10 : 'октябрь', 11 : 'ноябрь', 12 : 'декабрь'}
month_input = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))

for i in month_all:
  if i == month_input:
    month_ = month_all[i]
if month_input == 12 or month_input == 1 or month_input == 2:
  print(f'Время года, к которому относится месяц {month_} - {season[0]}')
elif month_input == 3 or month_input == 4 or month_input == 5:
  print(f'Время года, к которому относится месяц {month_} - {season[1]}')
elif month_input == 6 or month_input == 7 or month_input == 8:
  print(f'Время года, к которому относится месяц {month_} - {season[2]}')
elif month_input == 9 or month_input == 10 or month_input == 11:
  print(f'Время года, к которому относится месяц {month_} - {season[3]}')
