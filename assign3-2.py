#Cam Robinson Due: 2/21/24
import sys

text=sys.argv[1]

list1=text.split()

myTuple=tuple(list1)

rList=[]

for itr in myTuple:
    if myTuple.count(itr)>1 and itr not in rList:
        rList.append(itr)
        print("The repeated word",itr,"has",myTuple.count(itr),"occurance in the tuple")