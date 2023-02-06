class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        print("The area of Shape is:", self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        self.area = self.length ** 2
        print("The area of Square is:", self.area)

square = Square(5)
print(square.area())