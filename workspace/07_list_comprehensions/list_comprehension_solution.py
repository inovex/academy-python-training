students = ["Harry Potter", "Hermione Granger", "Ron Wasley", "Draco Malfoy"]

# Use a list comprehension to create a list of the students' last names
students_last_names = [ name.split(" ")[-1] for name in students ]
print('students_last_names:', students_last_names)

# Use a list comprehension to create a list of students whose last name's first character
# appears in the first half of the alphabet
alphabet_part_a = "ABCDEFGHIJKLM"
students_group_a = [ name for name in students_last_names if name[0] in alphabet_part_a ]
print('students_group_a', students_group_a)