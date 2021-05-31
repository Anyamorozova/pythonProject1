def division(num1, num2):
  try:
    return num1/num2
  except:
    return 'Деление на ноль недопустимо!'

numbers = input('Введите два числа через пробел: ').split()
print('Результат деления: ',division(int(numbers[0]), int(numbers[1])))
