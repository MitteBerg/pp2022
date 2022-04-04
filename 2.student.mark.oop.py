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
    # inout infoL  id , name , dob
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
    
class Course:
    def __init__(self):
        self.course_name =input('enter course name:')
        self.course_id = input('enter course id:')
        self.coursenum = input('enter number of course:')
    def CourseCount(self):
        
        return self.coursenum

    def inputCourseInfo(self):
      courses = []
    # inout infoL  id , name , dob
      for i in range(0, courseCount):
        id = self.course_id
        name = self.course_name
        
        course = {
            "id": id,
            "name": name
            
        }
        courses.append(course)
        return courses

    

class Mark(Student,Course):
    def __init__(self,student,course):
        self.__mark = input("enter mark")
        
    def showmark():
        pass
    
    def GPA():
        pass
    
    

#enter student count and information
studentCount = Student()
students = Student(studentCount)
students.inputStudentCount

#enter course count and information
courseCount = Course()
courses = Course(courseCount)
courses.inputCourseCount

#select course, input mark for students in the given course
#courseid = selectCourse(courses)
#inputMark(courseid, students)




# show marks for a given course

#courseid = selectCourse(courses)
#showMark(courseid, students)