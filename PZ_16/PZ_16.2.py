# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классынаследники будут иметь свои уникальные свойства и методы.
class Transport:
    
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels
    
    def info(self):
        return f"Макс. скорость: {self.max_speed} км/ч, Кол-во колёс: {self.wheels}"
    
    def move(self):
        return "Транспорт движется"


class Car(Transport):
    
    def __init__(self, max_speed, wheels, brand, doors):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.doors = doors
    
    def beep(self):
        return "Бип-бип!"
    
    def info(self):
        return f"Автомобиль {self.brand}, {super().info()}, Дверей: {self.doors}"


class Motorcycle(Transport):
    
    def __init__(self, max_speed, wheels, has_sidecar):
        super().__init__(max_speed, wheels)
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        return "Мотоцикл едет на заднем колесе!"
    
    def info(self):
        sidecar = "есть коляска" if self.has_sidecar else "нет коляски"
        return f"Мотоцикл, {super().info()}, {sidecar}"
car = Car(220, 4, "Toyota", 4)
moto = Motorcycle(180, 2, False)

print(car.info())
print(car.beep())
print(car.move())
print()

print(moto.info())
print(moto.wheelie())
print(moto.move()) 