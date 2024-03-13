import math

class Circle:
    def __init__(self, r):
        print("init")
        self.radius = r

    def circle_area_cal(self):
        print("asdfsf")
        return math.pi * self.radius**2
    
    def circle_perimeter_cal(self):
        return math.pi * self.radius * 2
    
r = float(input("Input r: "))

circle = Circle(r)
print("123432")

area = circle.circle_area_cal()
print(area)

perimeter = circle.circle_perimeter_cal()
print(perimeter)

