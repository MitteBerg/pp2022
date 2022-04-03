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

def selectCourse(courses):
    listCourses(courses)
    courseid = input("Enter course id you want: ")
    return courseid

def inputMark(courseid, students):
    print(f"Enter marks of the course {courseid} for students: ")
    for student in students:
        mark = float(input(f"-Student {student['name']}:"))
        student["marks"][courseid]= mark
    

def listCourses(courses):
    print("\n All courses list")
    for course in courses:
        print(f"{course['id']: <10} {course['name']: <20} ")
    pass

def listStudents(students):
    print("\n All student list")
    for student in students:
        print(f"{student['id']: <10} {student['name']: <20} {student['dob']: <15}")

def showMark(courseid, students):
    print("\n All marks for the course {courseid}")
    for student in students:
        print(f"{student['name']: <20} {student['mark'][courseid]}")

#enter student count and information
studentCount = inputStudentCount()
students = inputStudentInfo(studentCount)
listStudents(students)

#enter course count and information
courseCount = inputCourseCount()
courses = inputCourseInfo(courseCount)
listCourses(courses)

#select course, input mark for students in the given course
courseid = selectCourse(courses)
inputMark(courseid, students)




# show marks for a given course

courseid = selectCourse(courses)
showMark(courseid, students)