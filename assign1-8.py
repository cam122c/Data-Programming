f = open(r'C:\Users\camca\Downloads\romeo.txt')

gword = []

for line in f:
    words = line.split()
    
    for word in words:
        if word not in gword:
            gword.append(word)
gword.sort()
print(gword)