#Cam robinson 1/26/24
file = open('/Users/camca/Downloads/mailbox.txt')
count = 0
for line in file:
    if line.startswith("From"):
        words = line.split()
        dom = words[1]
        print(dom)
        count +=1
print('There were',count,'in the file with From as the first word')