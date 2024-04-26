#Cam Robinson
import matplotlib.pyplot as plt
import random
list1=[]
for i in range(0,500):
    num=random.randint(1,100)
    list1.append(num)
plt.hist(list1,100)
plt.show()