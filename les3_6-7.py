def int_func(text):
  return text.capitalize()
  
"""Первый вариант, вывод 'красивый' """
str_ = 'qwe asd zxc'.split()
list_new = ''
for i in str_:
  list_new += '{} '.format(int_func(i))
print(list_new)

"""Второй вариант"""
print(list(map(int_func,str_)))
