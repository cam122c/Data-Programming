grades = []
count = 0
avg = 0

file = open('/Users/camca/Downloads/ExamGrade.txt')

for grade in file:
    x = int(grade)
    count = count + 1
    print("Student"+str(count)+":",str(x))
    avg = avg + x
    
avg = avg/count
print('The average grade is',round(avg,2))