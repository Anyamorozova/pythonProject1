str_input = input('Введите строку из нескольких слов, разделённых пробелами: ')
list_input = str_input.split(' ')

for i, elem in enumerate(list_input):
  if len(elem) <= 10:
    print(i, elem)
  else:
    print(i, elem[:10])
