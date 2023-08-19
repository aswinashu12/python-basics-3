import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area_of_c(self):
        area=math.pi*self.radius**2
        return area
    def perimeter_of_c(self):

        perimeter=2*math.pi*self.radius
        return perimeter
radius=float(input("enter the radius"))
p1=circle(radius)
print(p1.area_of_c())
print(p1.perimeter_of_c())