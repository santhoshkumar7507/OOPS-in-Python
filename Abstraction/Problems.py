# Hide implementation, show functionality.

# Example:

# You drive a car without knowing engine details.

# prb: 1
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area")

c = Circle()
c.area()