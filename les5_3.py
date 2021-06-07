file = open("my_file_3.txt", "r")
content = file.read()
file.close()

content = content.split("\n")
list_worker, sum_wage = [], 0
count_worker = len(content)

for el in content:
  list_worker.append(el.split())
  
print("Сотрудники, имеющие оклад менее 20 тысяч рублей:")

for el in list_worker:
  if int(el[1]) < 20000:
    print(el[0])
  sum_wage += int(el[1])
  
average_wage = sum_wage/count_worker

print(f"Средняя величина дохода сотрудников: {average_wage}")
