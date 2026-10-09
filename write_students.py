# Task 1: Student Records File
f = open("students.txt", "w")
print("Name: Mary Wanjiru, Reg: CS/001/2026, Course: Computer Science, Mark: 78", file=f)
print("Name: John Kamau, Reg: CS/002/2026, Course: IT, Mark: 65", file=f)
print("Name: Aisha Omar, Reg: CS/003/2026, Course: Software Eng, Mark: 82", file=f)
f.close()

# If students.txt already exists, opening it with 'w' ERASES (overwrites)
# its existing contents. If it does not exist, it is created.
print("Records saved. Note: mode 'w' overwrites any existing content.")
