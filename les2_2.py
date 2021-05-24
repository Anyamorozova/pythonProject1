test_list = input('Введите через запятую и без пробелов элементы списка: ')
test_list = test_list.split(',')
new_list = []

for i, elem in enumerate(test_list):
  if i % 2 == 0:
    new_list.insert(i+1,elem)
  else:
    if i != len(test_list):
      new_list.insert(i-1,elem)
    else:
      new_list.insert(i,elem)
print(new_list)
