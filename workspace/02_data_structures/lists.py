houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]
print(houses[2]) # "Slytherin"
print(houses[1:3]) # ['Ravenclaw', 'Slytherin']

students = ["Harry", "Ron", ["Hermione", "Luna"], "Ginny"]
len(students) # 4
students.append("Draco") # names = ["Harry", "Ron", ["Hermione", "Luna"], "Ginny", "Draco"]
students.remove("Draco") # names = ["Harry", "Ron", ["Hermione", "Luna"], "Ginny"]
students.pop(1) # names = ['Harry', ['Hermione', 'Luna'], 'Ginny']

print(students)