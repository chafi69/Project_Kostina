# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.
import math

class crug:
    def __init__(self, radius):
        self.radius = radius
    
    def diameter(self):
        return 2 * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
c = crug(5)
print(f"Радиус: {c.radius}")
print(f"Диаметр: {c.diameter()}")
print(f"Площадь: {c.area():.2f}")
print(f"Длина окружности: {c.circumference():.2f}")