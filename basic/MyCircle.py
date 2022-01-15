import math

class Circle:
    r = 0
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2*self.r*math.pi

    def area(self):
        return self.r*self.r*math.pi