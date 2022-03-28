numStundent = int (input ("Number of students: "))
studentlist = []
for i in range (numStundent):
    studentid = input ("Student id: ")
    studentname = input ("Student name: ")
    studentbirth = input ("Student's date of birth: ")
    studentlist.append (( studentid, studentname, studentbirth))

coursnum = int (input ("Number of courses: "))
courselist = []
for i in range (coursnum):
    coursid = input ("Course id: ")
    coursname = input ("Course name: ")
    courselist.append ((coursid,coursname))
    
tupl = {}    
n = int (input ("Student-course marks ! "))
for i in range (n):
    while True:
        studentid = input ("Student id: ")
        coursid = input ("Course id: ")
        if studentid not in [student [0] for student in studentlist]:
            print ("Wrong student id")
            continue 
        if coursid not in [course [0] for course in courselist]:
            print ("Wrong course id")
            continue 
        break
    marks = int (input ("Marks: "))
    if coursid in tupl:
        tupl [coursid].append ((studentid, marks))
    else:
        tupl [coursid] = [(studentid, marks)]
        

for a in studentlist:
    print (f"Student id: {a[0]} Name: {a[1]} Date of birth: {a[2]}")


for b in courselist:
    print (f"Course id: {b[0]} Name: {b[1]}")
    
coursid = input ("\nEnter course! ")
if coursid in tupl:
    for tups in tupl [coursid]:
        print (f"Student {tups[0]} got {tups [1]} marks")