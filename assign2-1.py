
import sys

length = len(sys.argv)

weekdays = {}

for itr in range (1,length,2):
    day = sys.argv[itr]
    num = sys.argv[itr+1]
    weekdays[day] = num
print(weekdays)

sortvalue = sorted(weekdays.values())
sortdict = {}
#print(sortvalue) # prints ['1','2','3','4','5','6','7']

for i in sortvalue:
    for k in weekdays.keys():
        if weekdays[k] == i :
            sortdict[k] = weekdays[k]
            break
print(sortdict)

reversesortvalue = sorted(weekdays.values(), reverse=True)
reversedict = {}

for i in reversesortvalue:
    for k in weekdays.keys():
        if weekdays[k] == i :
            reversedict[k] = weekdays[k]
            break
    
print('\nOutput in descending order:')
for key,values in reversedict.items():
    print(key,"=>",values)

print('\nOutput in ascending order:')
for key,values in sortdict.items():
    print(key,"=>",values)  
  