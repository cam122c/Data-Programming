#Cam Robinson 
import matplotlib.pyplot as myplot
import sys

x_axis = [0,1,2,3,4,5]
y_axis = [0,40,80,120,160,200]

x1_axis = [0,1,2,3]
y1_axis = [200,140,80,20]

myplot.plot(x_axis,y_axis,label='john speed')
myplot.plot(x1_axis,y1_axis,label='alice speed')
myplot.legend(loc='upper left')
myplot.xlabel('X Values')
myplot.ylabel('Y Values')
myplot.show() 