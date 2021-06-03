file = open("my_file_5.txt", "w")

for el in range(1, 20):
  file.write(f"{str(el)} ")
file.close()

file = open("my_file_5.txt", "r")
content = file.read()
file.close()

content = content.strip().split(' ')
sum_numbers = 0

for el in content:
  sum_numbers += int(el)
  
print(f"Сумма чисел в файле равна: {sum_numbers}")
