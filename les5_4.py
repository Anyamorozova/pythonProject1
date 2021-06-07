file = open("my_file_4_1.txt", "r")
file_new = open("my_file_4_2.txt", "a")

for line in file:
    content = line.split(' — ')
    if content[0] == "One":
      file_new.write(f"Один — {content[1]}")
    if content[0] == "Two":
      file_new.write(f"Два — {content[1]}")
    if content[0] == "Three":
      file_new.write(f"Три — {content[1]}")
    if content[0] == "Four":
      file_new.write(f"Четыре — {content[1]}")

file.close()
file_new.close()
