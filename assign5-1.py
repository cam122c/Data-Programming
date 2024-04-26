#cam Robinson due: 3/29/24
import sys

class Circle:
    radius = None
    def __init__(self,r):
        self.radius = r
    def area(self):
        circlearea = round(3.14*self.radius**2,1)
        return circlearea
    def perimeter(self):
        peri = round(2*3.14*self.radius,1)
        return peri 
radius = float(sys.argv[1])
newcircle = Circle(radius)
a=newcircle.area()
p=newcircle.perimeter()
print('Your circle with a radius',radius,'inch has a perimeter of',p,'and an area of',a)
        
        


