class Shape:
    def __init__(self):
        self.area = 0
        
    def area(self):
        print("The area of Shape is:", self.area)
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 20)
print(rect.area())