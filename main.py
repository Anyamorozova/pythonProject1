# print("Введите число: ")
# number = input()
# print(number)
# print("Введите произвольное слово: ")
# word = input()
# print(word)
# ____________________________

# print("Введите время в секундах: ")
# seconds = int(input())
# minutes = seconds//60
# hour = minutes//60
# minutes = minutes % 60
# seconds = seconds - hour * 3600 - minutes * 60
# if hour < 10:
#     hour = "0" + str(hour)
# if minutes < 10:
#     minutes = "0" + str(minutes)
# if seconds < 10:
#     seconds = "0" + str(seconds)
# print("{}:{}:{}".format(hour, minutes, seconds))
# ______________________________

# print("Введите число не больше 10: ")
# number_one = input()
# number_two = number_one + number_one
# number_three = number_two + number_one
# sum = int(number_one) + int(number_two) + int(number_three)
# print(sum)
# ______________________________

# print("Введите целое положительное число: ")
# number = input()
# len_num = len(number)
# big_number = 0
# while len_num != 0:
#     if int(number) % 10 > big_number:
#         big_number = int(number) % 10
#     len_num = len_num - 1
#     number = number[:-1]
# print(big_number)
# ______________________________

# print("Введите значение выручки фирмы: ")
# proceeds = int(input())
# print("Введите значение издержек фирмы: ")
# costs = int(input())
# if costs > proceeds:
#     print("К сожалению у вашей фирмы убыток.")
# else:
#     print("Поздравляем, у вашей фирмы прибыль!")
#     profit = proceeds - costs
#     ren_proceeds = profit/proceeds
#     print("Рентабельность выручки: {}".format(ren_proceeds))
#     print("Укажите количество сотрудников: ")
#     staff = int(input())
#     profit_staff = profit//staff
#     print("Прибыль фирмы в расчете на одного сотрудника: {}".format(profit_staff))
# ______________________
