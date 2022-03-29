class Student:
    def __init__(self):  
        self.sname = input('enter student name:')
        self.sid = input('enter student rollno:')
        self.dob = input('enter student dob:')
        self.count=input('enter number of student:')
    def name(self):  
        return self.sname
        
    def id(self):  
        return self.id
    
    def birthday(self):  
        return self.dob
    def number(self): 
        return self.count
        
    
class Course:
    def __init__(self):
        self.course_name =input('enter course name:')
        self.course_id = input('enter course id:')
        self.coursenum = input('enter number of course:')
    def coursename(self):  
        return self.course_name
    def courseid(self):  
        return self.course_id
    def numcourse(self):
        return self.coursenum
    

class Mark:
    def __init__(self):
        self.__mark = input("enter mark")
    

numStudents = Student()
numStudents.number()
Studentlist = []
for i in range (numStudents):
    studentname, studentid, dob = Student()
    studentname.name()
    studentid.id()
    dob.birthday()
    Studentlist.append ((studentname, studentid, dob))






numCourse = Course()
numCourse.numcourse()
Courselist = []
for i in range (numCourse):
    courseid, coursename= Course()
    courseid.courseid()
    coursename.coursename()
    
    Courselist.append ((courseid,coursename))


st1=Student()

    

