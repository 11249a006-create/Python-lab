class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def area(self, b, h):
        return 0.5 * b * h

class Circle(Shape):
    def area(self, r):
        return 3.14159 * r * r

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

print("Triangle Area:", Triangle().area(10, 5))
print("Circle Area:", Circle().area(7))
print("Rectangle Area:", Rectangle().area(10, 4))
