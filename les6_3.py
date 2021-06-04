class Worker:

    name = None
    surname = None
    position = None
    _income = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"Полное имя: {self.surname}  {self.name}"

    def get_total_income(self):
        return f"Доход: {self._income['wage'] + self._income['bonus']}"


worker_sidorov = Position("Oleg", "Sidorov", "developer", 10000, 3000)
print(worker_sidorov.get_full_name())
print(worker_sidorov.get_total_income())
