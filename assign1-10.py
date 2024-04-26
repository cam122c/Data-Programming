#Cam robinson due 1/26/24
import sys

length=len(sys.argv)

num=[]

for item in range(1,length):

    inp=int(sys.argv[item])
    num.append(inp)

print("The list of scores is:",num)

print(" ")

total=len(num)
print("You have",total,"top scores.")

minV=min(num)
print("Lowest score:",minV)
    
maxV=max(num)
print("Highest score:",maxV)

avg=sum(num)/len(num)
print("Average of all scores:",round(avg,2))

print(" ")

num.sort(reverse=False)
print("Your scores in lowest to highest:",num)

num.sort(reverse=True)
print("Your scores in highest to lowest:",num)