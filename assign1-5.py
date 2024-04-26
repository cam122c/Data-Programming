import sys


def fib(num):
# 1 1 2 3 5 8
    n1 = 0
    n2 = 1
    seq = ""
    
    for itr in range(num):
        n3 = n1+n2
        seq = seq+str(n2)+" "
        n1 = n2
        n2 = n3
    
    return seq

num = int(sys.argv[1])
seq = fib(num)
total = sum(seq)
avg = total/num

print("the fib sequence is:",seq)
print('The sum of all numbers is:',total)
print('The average of all numbers:',avg)

