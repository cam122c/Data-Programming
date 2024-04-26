#Cam RObinson
import matplotlib.pyplot as plt

fh=open(r'C:\Users\camca\Downloads\DV_sample.csv','r')

for line in fh:
    if line.startswith('Date'):
        names=line.split(',')
    
    if line.startswith('2019/4/1'):
        date=line.split(',')  
        
names.remove('Date')
date.remove('2019/4/1')

percantage=date
name=names

plt.pie(percantage,labels=names,startangle=90,autopct="%1.1f%%")
plt.show()