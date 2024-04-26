
import sys

diction = {0: 10, 1:20}
count = 0
num = int(sys.argv[1])

print('The old dictionary is:',diction)


for run in range(num):
    next_key = max(diction) + 1
    next_value = diction[next_key - 1]+10
    diction[next_key] = next_value
    count +=1
    print('After the #'+str(count),'run, the new dictionary is:',diction)