#cam robinson 2/9/23
import sys

length = len(sys.argv)
num = {}
count = 1  
for i in range(1,length):
    if sys.argv[i] == 'done':
        break
    else:
        num[count] = int(sys.argv[i])
        count +=1# prints {1:5,2:6, 3:7, 4: 4,5:3}
print('The dictionary is',num)
sortedvalues = sorted(num.values())
print("The two largest numbers are:",sortedvalues[-1],',',sortedvalues[-2])