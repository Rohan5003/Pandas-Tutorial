class Circle:
    def area(self):
        return "Area = π * r^2"

class Square:
    def area(self):
        return "Area = side * side"

shapes = [Circle(), Square()]

for shape in shapes:
    print(shape.area())
