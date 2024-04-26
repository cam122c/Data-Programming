#Cam Robinson Due:2/23/24
#nums = (6,5,1,2,0,4)
num = (1,2,3)
total = 0
length = len(num)
for i in range(length):
    total = total +num[i]*pow(10,length-(i+1))
print(total)
