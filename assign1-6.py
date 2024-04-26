import sys

def isPal(w):
    fIdx=0
    lIdx=len(w)-1
    while fIdx<=lIdx:
        if w[fIdx]==w[lIdx]:
            fIdx=fIdx+1
            lIdx=lIdx-1
        else:
            return False
    return True

word=sys.argv[1]
result=isPal(word)
if result==True:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")