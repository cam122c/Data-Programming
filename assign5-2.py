#cam Robinson due: 3/29/24
import sys

class Circle:
    radius = None
    def __init__(self,r):
        self.radius = r
    def area(self):
        circlearea = round(3.14*self.radius**2,1)
        return circlearea
class Cylinder(Circle):
    height = 0
    def __init__(self,r,h):
        self.radius = r
        self.height = h
    def area(self):
        areacyc = round(2*3.14*self.radius*self.height+2*3.14*self.radius**2,2)
        return areacyc
radius = int(sys.argv[1])
height = int(sys.argv[2])

NewCylinder = Cylinder(radius,height)
r = NewCylinder.area()
print('You are asking to create a cylinder with a radius of',radius,'and height of',height,'inches')
print('Area of the cylinder is',r)

