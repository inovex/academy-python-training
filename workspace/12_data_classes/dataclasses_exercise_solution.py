# # Data classes exercise
# 1. Create a Magician data class
#       - attributes: name, age, patronus
#       - create an instance of the class for Harry Potter and print his name and patronus
#
# 2. Create a Student data class that inherits from Magician
#       - add the attributes house and year
#       - create at least 4 instances of Student, store them in a list
#       - write a function that takes the list as input and returns a new list with the
#         Student instances sorted by their last names in alphabetical order
#       - You may use actual characters from Harry Potter, or invent your own characters

# Solution Exercise 1
from dataclasses import dataclass

@dataclass
class Magician:
    name: str
    age: int
    patronus: str

harry_potter = Magician("Harry Potter", 17, "Stag")
print(f"Magician: {harry_potter.name}, Patronus: {harry_potter.patronus}")

# Solution Exercise 2
@dataclass
class Student(Magician):
    house: str
    year: int

students = [
    Student("Harry Potter", 15, "Stag", "Gryffindor", 4),
    Student("Hermione Granger", 16, "Otter", "Gryffindor", 4),
    Student("Cedric Diggory", 18, "Unknown", "Hufflepuff", 7),
    Student("Luna Lovegood", 15, "Hare", "Ravenclaw", 4)
]

students_sorted = sorted(students, key=lambda student: student.name.split(" ")[1])
print(students_sorted)