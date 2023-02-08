import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point: ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    def dist(self, other):
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2
        return math.sqrt(x_diff + y_diff)
        
p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show() # Point: (1, 2)
p2.show() # Point: (4, 6)

p1.move(3, 4)
p1.show() # Point: (4, 6)

distance = p1.dist(p2)
print(distance) # 3.605551275463989