#Cam Robinson Due: 2/21/24
import sys

num = int(sys.argv[1])

list1 = []
list2 = []
list3 = []

count = 1
for itr in range (1,num+1):
    num1 = 2**count
    list1.append(num1)
    list2.append(num1)

    num3 = 3**count

    list3.append(num1)
    list3.append(num3)
    count = count+1

list2.append(2*list2[-1])

myTuple1 = tuple(list1)    
myTuple2 = tuple(list2)    
myTuple3 = tuple(list3)    
print("The first tuple is:",myTuple1) 
print("The second tuple is:",myTuple2)   
print("The third tuple is:",myTuple3)
