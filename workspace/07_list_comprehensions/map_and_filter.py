students = ["Harry Potter", "Hermione Granger", "Ron Wasley", "Draco Malfoy"]

# what if we want only the students' last names?
# Two Options
# Option 1: using a for-loop (the object-oriented way)
students_last_names_OOP = []
for student in students:
    last_name = student.split(" ")[1]
    students_last_names_OOP.append(last_name)

# Option 2: using map() (the functional programming way)
def get_last_name(student):
    return student.split(" ")[1]
students_last_names_FP = map(get_last_name, students)

#print(students_lastNames_OOP)
print(students_last_names_FP) # prints a map object
print(list(students_last_names_FP)) # prints a list of each element in the map object

# Now, let's assume we want only those students whose last names' first letters
# appear in the first half of the alphabet.
# Again, we have two options:
# Option 1: using a for-loop (the object-oriented way)
students_group_a_OOP = []
for student in students_last_names_OOP:
    if student[0] in "ABCDEFGHIJKLM":
        students_group_a_OOP.append(student)
print(students_group_a_OOP)

# Option 2: using filter() -> the functional programming way
def isin_group_a(student):
    return student[0] in "ABCDEFGHIJKLM"
students_group_a_FP = filter(isin_group_a, students_last_names_OOP)
print(students_group_a_FP)
print(list(students_group_a_FP))