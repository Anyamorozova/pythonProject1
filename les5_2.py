file = open("my_file.txt", "r")
content = file.read()
content = content.split("\n")
count_str, count_word = 0, 0

def count_list(list_, number):
  for el in list_:
    number += 1
  return number

count_str = count_list(content, 0)
print(f"Количество строк в файле: {count_str}")
print("Количество слов в строках соотвественно:")

for el in content:
  count_word = count_list(el.split(), 0)
  print(count_word)

file.close()
