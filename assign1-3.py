courses = []
profs = []

while True:
    course = input("Please enter the courses you are taking in this semester: ")
    if course == 'done':
        break

    prof = input("Please enter the professor's name for the course: ")

    courses.append(course)
    profs.append(prof)

print("The list for courses is", courses)
print("The list for professors is", profs)


print("The courses you are taking in this semester are:",end=" ")
for course in courses:
    print(course, end=" ")

print("\nThe professors for these courses are:", )
for i in range(len(profs)):
    print(f"{profs[i]} ->", end="\n")