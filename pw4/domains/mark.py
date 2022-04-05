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