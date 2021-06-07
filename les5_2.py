file = open("my_file_2.txt", "r")
content = file.read()
file.close()

content = content.split("\n")
count_str = len(content)
print(f"Количество строк в файле: {count_str}")
print("Количество слов в строках соотвественно:")

for el in content:
  count_word = len(el.split())
  print(count_word)
