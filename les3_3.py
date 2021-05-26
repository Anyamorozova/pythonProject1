def my_func (num1, num2, num3):
  numbers = [num1, num2, num3]
  max_1 = (max(numbers))
  numbers.remove(max_1)
  max_2 = (max(numbers))
  
  return max_1 + max_2
  
print(my_func(1, 2, 1))
