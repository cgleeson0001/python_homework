# Task 5: Extending a Class

import math

#Create class Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #equality
    def _eq_(self, other):
        return self.x == other.x and self.y == other.y
    #string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    #euclidean distance
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 +
                         (self.y - other.y) ** 2)

    
#Create class Vector
class Vector(Point):

    #override string rep
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    #override + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

#main program
if __name__ == "__main__":
    p1=Point(3,4)
    p2=Point(6,8)

    print(p1)
    print(p2)
    print("Equal:", p1 == p2)
    print("Distance:", p1.distance_to(p2))

    #Create vectors
    v1=Vector(1,2)
    v2=Vector(3,4)

    print(v1)
    print(v2)

    v3=v1+v2
    print("Vector addition:", v3)
