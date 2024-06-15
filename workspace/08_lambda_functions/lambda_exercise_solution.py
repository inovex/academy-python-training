# Given the dictionary of students below

students = {
    "Harry Potter": {
        "house": "Gryffindor",
        "age": 10,
        "astronomy_mark": 80
    },
    "Ron Weasley": {
        "house": "Gryffindor",
        "age": 11,
        "astronomy_mark": 87
    },
    "Hermione Granger": {
        "house": "Gryffindor",
        "age": 11,
        "astronomy_mark": 100
    },
    "Cedric Diggory": {
        "house": "Hufflepuff",
        "age": 16,
        "astronomy_mark": 91
    },
    "Gregory Goyle": {
        "house": "Slytherin",
        "age": 12,
        "astronomy_mark": 67
    },
    "Padma Patil": {
        "house": "Ravenclaw",
        "age": 14,
        "astronomy_mark": 98
    }
}

# 1. Use a lambda function to create a list of names sorted
# by the students' age in ascending order

students_sorted_by_age = sorted(students, key=lambda x: students[x]["age"])

# 2. Use a lambda function to get only students associated with Gryffindor

gryffindor_students = list(filter(lambda x: students[x]["house"] == "Gryffindor", students))

# 3. All Gryffindor students get a bonus on their astronomy_marks! Use a
#    lambda function to add a 15% bonus to each Gryffindor student's mark.
#    Note: The final grade should not be greater than 100!

students_with_bonus = {
  name : min(100, fact["astronomy_mark"] * 1.15) if fact["house"] == "Gryffindor" else fact["astronomy_mark"]
  for name, fact in students.items()
}
