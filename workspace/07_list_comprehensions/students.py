# sources: 
# https://docs.python.org/3/tutorial/datastructures.html
# https://towardsdatascience.com/pythons-map-filter-and-reduce-functions-explained-2b3817a94639

students = [
    ("Harry Potter", "Gryffindor"),
    ("Hermione Granger", "Gryffindor"),
    ("Ron Weasley", "Gryffindor"),
    ("Draco Malfoy", "Slytherin"), 
    ("Cedric Diggory", "Hufflepuff")    
]

# TO DO: Add explanations/context
# TO DO: Add exercise
# TO DO: Add dict and set comprehensions
# we only want the students' last names -> map()
def get_last_name(student: tuple):
    return (student[0].split(" ")[1], student[1])

students_last_names = list(map(get_last_name, students))
print(students_last_names)

# we are only interested in students from Gryffindor
# -> filter()
def in_gryffindor(student: str):
    return student[1] == 'Gryffindor'

students_gryffindor = list(filter(in_gryffindor, students_last_names))
print(students_gryffindor)

# There is a more Pythonic way! Let's implement the above in only one line of code
# -> list comprehension
# get the students last names
students_last_names = [(student[0].split(" ")[1], student[1]) for student in students]
print(students_last_names)

# again, let's include only students from Gryffindor. This time, we are only interested in their names, though.
students_slytherin = [student[0] for student in students_last_names if student[1] == "Gryffindor"]
print(students_slytherin)