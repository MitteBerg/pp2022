class Student:
    def __init__(self):  
        self.sname = input('enter student name:')
        self.sid = input('enter student rollno:')
        self.dob = input('enter student dob:')
        self.count=input('enter number of student:')
    def inputStudentCount():
        count = int(input("Number of students:"))
        return count

    def inputStudentInfo(studentCount):
    #returns a list students , with info from keyboard
        students = []
    # inout infoL  id , name , dob
        for i in range(0, studentCount):
            id = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Student DoB: ")
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
    def inputCourseCount():
        count = int(input("Number of courses:"))
        return count

    def inputCourseInfo(courseCount):
      courses = []
    # inout infoL  id , name , dob
      for i in range(0, courseCount):
        id = input("course ID: ")
        name = input("course name: ")
        
        course = {
            "id": id,
            "name": name
            
        }
        courses.append(course)
        return courses

    

class Mark(Student,Course):
    def __init__(self,student,course):
        self.__mark = input("enter mark")
    
    

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