# Implement the Concept of inheritence using python.

# Code:
from turtle import shape


class Shape:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    def area(self, x, y):
        self.x = x
        self.y = y
        a = self.x * self.y
        print("Area of a Rectangle ", a)

class Square(Shape):
    def _init_(self, x):
        self.x = x
    def area(self, x):
        self.x = x
        a = self.x * self.x
        print("Area of a Rectangle ", a)

r = Shape()
r.area(12, 34)
s = Square()
s.area(34)