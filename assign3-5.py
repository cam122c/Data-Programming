#Cam Robinson #Due: 2/23/24

import sys

if len(sys.argv[1:])>0:
       tup = tuple(int(x) for x in sys.argv[1:])
       print("Original Tuple:", tup)

product = 1

for x in tup:
       product *= x
print("Multiplication of all the numbers of the said tuple:",product)
