#Task_5: Extending a Class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return F"{self.x}, {self.y}"

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __add__(self, other):
        return Vector (self.x + other.x, self.y + other.y)
    

point_1 = Point(3, 5)
point_2 = Point(2, 3)
print(point_1)
print(point_1 == point_2)
print(point_1.distance_to(point_2))

vector_1 = Vector(3, 6)
vector_2 = Vector(3, 3)
print(vector_1)
v3 = vector_1 + vector_2
print(v3)
