class Student:
    def __init__(self):  
        self.sname = input('enter student name:')
        self.sid = input('enter student id:')
        self.dob = input('enter student dob:')
        self.count=input('enter number of student:')
    def StudentCount(self):
        return self.count

    def inputStudentInfo(self,studentCount):
    #returns a list students , with info from keyboard
        students = []
    
        for i in range(0, studentCount):
            id = self.sid
            name = self.sname
            dob = self.dob
            student = {
            "id": id,
            "name": name,
            "dob":dob,
            "marks":{}
        }
        students.append(student)
        return students
    
    def listStudents(students):
        print("\n All student list")
    for student in inputStudentInfo.students:
        print(f"{student['id']: <10} {student['name']: <20} {student['dob']: <15}")
    