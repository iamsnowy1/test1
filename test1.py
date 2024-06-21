Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from abc import ABC, abstractmethod
... 
... # Базовий клас Shape
... class Shape(ABC):
...     @abstractmethod
...     def calculate_area(self):
...         pass
... 
... # Клас Circle, який успадковує Shape
... class Circle(Shape):
...     def __init__(self, radius):
...         self.radius = radius
...     
...     def calculate_area(self):
...         return 3.14 * self.radius * self.radius
...     
...     def draw(self):
...         print(f"Drawing a circle with radius {self.radius}")
... 
... # Клас Square, який успадковує Shape
... class Square(Shape):
...     def __init__(self, side):
...         self.side = side
...     
...     def calculate_area(self):
...         return self.side * self.side
...     
...     def draw(self):
...         print(f"Drawing a square with side {self.side}")
... 
... # Клас Triangle, який успадковує Shape
... class Triangle(Shape):
...     def __init__(self, base, height):
...         self.base = base
...         self.height = height
...     
...     def calculate_area(self):
...         return 0.5 * self.base * self.height
...     
...     def draw(self):
...         print(f"Drawing a triangle with base {self.base} and height {self.height}")
... 
... # Інтерфейс IDrawable
... class IDrawable(ABC):
...     @abstractmethod
...     def draw(self):
...         pass
... 
... # Демонстрація використання поліморфізму
... shapes = [
...     Circle(5),
...     Square(4),
...     Triangle(3, 6)
... ]
... 
... for shape in shapes:
...     area = shape.calculate_area()
...     shape.draw()
...     print(f"Area: {area}")
    print()  # Роздільна лінія для кращої читабельності
