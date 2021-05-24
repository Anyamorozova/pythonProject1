test_list = ['a', ['b'], 3]
for i in test_list:
  print('Элемент списка под номером '+ str(test_list.index(i)) +' имеет тип - '+ str(type(i)))
