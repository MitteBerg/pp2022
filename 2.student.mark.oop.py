class Student:
    def __init__(self, name , id , dob ):
        self.name = name
        self.id = id
        self.dob = dob
        
    def infor(self):
        print("Student's name : {}".format(self.name))
        print("Student's  id : {}".format(self.id))
        print("Student's day of birth : {}".format(self.dob))
        
    
class Course:
    def __init__(self, course_name,course_id):
        self.course_name = course_name
        self.course_id = course_id
        
    def infor(self):
        print("Course id:{}".format(self.course_name))
        print("Course_id:{}".format(self.course_id))
    
#Polymorphism
stlist= [Student(),Course()]
for i in stlist:
    i.infor()

a1 = Student()
a1.student_infor()    
    
