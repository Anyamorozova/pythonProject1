import re
file = open("my_file.txt", "r")
subject, sum_sub, num = {}, 0, []

for line in file:
  content = line.split(': ')
  content_copy = content.copy()
  content_copy = content[1].split(' ')
  for i in range(len(content_copy)):
    if content_copy[i] != '—':
      num = re.findall(r'\d+', content_copy[i])
      print(num)
      sum_sub += int(num[0])
  subject[content[0]] = sum_sub
  sum_sub = 0
  
file.close()  
print(subject)
