class Car:
  
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        return "Машина поехала."
        
    def stop(self):
        return "Машина остановилась."
        
    def turn(self, direction):
        if direction == "right":
          return "Машина повернула направо."
        elif direction == "left":
          return "Машина повернула налево."
        
    def show_speed(self):
        return f"Скорость машины: {self.speed} км/ч."  
        
        
class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
          return "Превышение скорости 60 км/ч!"
        return f"Скорость машины: {self.speed} км/ч." 
        
        
class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
        
class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
          return "Превышение скорости 40 км/ч!"
        return f"Скорость машины: {self.speed} км/ч." 
        
        
class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)      

town_car = TownCar(50,"red","Volvo",False)
police_car = PoliceCar(90,"white-black","KIA",True)
work_car = WorkCar(60,"green","Mazda",False)
spirt_car = SportCar(120,"blue","Audi",False)

print(town_car.go(),town_car.show_speed(),town_car.turn("left"),town_car.stop())
print(town_car.__dict__)
print(police_car.show_speed(),police_car.turn("right"))
print(police_car.__dict__)
print(work_car.show_speed())
print(spirt_car.go(),spirt_car.show_speed())
