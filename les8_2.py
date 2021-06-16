class My_exception(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_num_1 = int(input("Введите делимое: "))
inp_num_2 = int(input("Введите делитель: "))

try:
    if inp_num_2 == 0:
        raise My_exception("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except My_exception as err:
    print(err)
else:
    print(f"Все хорошо. Ваш результат деления: {inp_num_1/inp_num_2}")
