def my_func_1 (x, y):
  return x**y
  
def my_func_2 (x, y):
  y = abs(y)
  while y != 0:
    x *= x
    y -= y
  return 1/x
  
print(my_func_2(2.2, -2))
print(my_func_1(2.2, -2))
