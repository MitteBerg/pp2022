import math
import numpy as np
import curses 
from domain.student import *
from domain.course import *
from domain.mark import*




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
    
class Course:
    def __init__(self):
        self.course_name =input('enter course name:')
        self.course_id = input('enter course id:')
        self.coursenum = input('enter number of course:')
    def CourseCount(self):
        
        return self.coursenum

    def inputCourseInfo(self):
      courses = []
    
      for i in range(0, courseCount):
        id = self.course_id
        name = self.course_name
        
        course = {
            "id": id,
            "name": name
            
        }
        courses.append(course)
        return courses
    
    def listCourses(courses):
        print("\n All courses list")
    for course in inputCourseInfo.courses:
        print(f"{course['id']: <10} {course['name']: <20} ")
    pass

    

class Marks:
    def __init__(self,sid,course_id,mark,Gpa=0):
        self.studentid = sid
        self.course_id = course_id
        self.mark = mark
        self.Gpa=Gpa
    
    def calculate_average():
        creditssum = 0
        markssum = 0
        for course_id, marks in marklist:
          for course in courselist:
            if course_id == courses[0]:
                sum_credits += int(courses[2])
                sum_marks += marks * int(courses[2])
        average = sum_marks / sum_credits
        average = np.round(average, 1)
        return average