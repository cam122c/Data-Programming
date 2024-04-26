#cam Robinson due: 3/29/24
class Student:
    students = None
    
    def __init__(self,list1):
        self.students = list1
    def mate(self):
        for i in self.students:
            print(i)
students =  [{"name": "Jon Snow", "student id": 721440392, "currentGPA": 3.70, "course1" : "A", "course2" : "A", "course3" : "B", "course4" : "A"}, {"name": "Samwell Tarly", "student id": 193323016, "currentGPA": 2.38, "course1" : "b","course2" : "d", "course3" : "C", "course4" : "b"}, {"name": "Tyrion Lannister", "student id": 779530062, "currentGPA": 0.10, "course1" : "f","course2" : "c", "course3" : "B", "course4" : "c"}, {"name": "Daenerys Targaryen", "student id": 127831563, "currentGPA": 1.15, "course1" : "b","course2" : "A", "course3" : "a", "course4" : "b"}, {"name": "Sansa Stark", "student id": 958823778, "currentGPA": 3.25, "course1" : "C","course2" : "A", "course3" : "D", "course4" : "c"}]

studentlist1 = Student(students)
print(studentlist1.mate())