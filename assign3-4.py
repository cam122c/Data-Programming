#Cam Robinson Due: 2/21/24
import sys

length=sys.argv[1]

list1=list(length)

myTuple=tuple(list1)
print("The converted tuple is:",myTuple)

rList=[]

for itr in myTuple:
    if myTuple.count(itr)>1 and itr not in rList:
        rList.append(itr)
        print("The repeated letter",itr,"has",myTuple.count(itr),"occurance in the tuple")