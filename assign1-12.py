#Cam robinson 1/26/24
import sys

length=len(sys.argv)

lame1=[]
lame2=[]

for item in range(1,length):

    inp=int(sys.argv[item])
    lame1.append(inp)
    if inp not in lame2:
        lame2.append(inp)
    
print(lame2)