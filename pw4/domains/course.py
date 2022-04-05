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