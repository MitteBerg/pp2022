import numpy as np
import curses 
from domain.student import *
from domain.course import *
from domain.mark import*

def listStudents(students):
        print("\n All student list")
    for student in inputStudentInfo.students:
        print(f"{student['id']: <10} {student['name']: <20} {student['dob']: <15}")
        
def listCourses(courses):
        print("\n All courses list")
    for course in inputCourseInfo.courses:
        print(f"{course['id']: <10} {course['name']: <20} ")
    pass