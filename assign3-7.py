#Cam Robinson Due:2/23/24
#nums=((10,5,10,12),(1,2))
num = ((10,10,10,12),(30,45,56),(81,80,39,32,90),(1,2,3,4,0))

print("Original Tuple:",num)

summary=0
newList=[]

for item in num:
    summary=0
    for itr in item:
        summary=summary+itr
    result=summary/len(item)
    newList.append(result)

newTuple=tuple(newList)

print(newTuple)