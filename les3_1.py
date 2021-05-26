def division(num1, num2):
  if num2 != 0:
    return num1/num2
  else:
    return 'Деление на ноль недопустимо!'

numbers = input('Введите два числа через пробел: ')
numbers = numbers.split()

print('Результат деления: ',division(int(numbers[0]), int(numbers[1])))
