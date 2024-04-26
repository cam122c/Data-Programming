#Cam Robinson Due: 2/21/24
course = []
instr = []

while True:
    courses = input("Please enter the courses you are taking in this semester: ")
    if courses == 'done':
        break

    professors = input("Please enter the professor's name for the course: ")
    print(" ")
    course.append(str(courses))
    instr.append(str(professors))
    
print(" ")
    
myTuple1=tuple(course)
print("The courses tuple is",myTuple1)

myTuple2=tuple(instr)
print("The professor's tuple is",myTuple2)

myTuple3=zip(myTuple1,myTuple2)

list3=[]

for itr in myTuple3:
    list3.append(itr[0])
    list3.append(itr[1])
print(tuple(list3))