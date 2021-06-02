file = open("my_file.txt", 'w')

def write_to_file(file, str_):
    file.write(str_)

while True:
  if input('Чтобы выйти, нажмите "Enter". \nЛюбой символ - продолжить.') == '':
    file.close()
    break
  str_ = input('Введите любую строку: ')
  write_to_file(file, f'{str_}\n')
