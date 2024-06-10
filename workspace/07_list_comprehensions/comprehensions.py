# List Comprehension

# filtering out all integers divisible by 3
# Option 1: using filter()
def divisible_by_3(num: int):
    return num % 3 == 0
divisibles_filter = list(filter(divisible_by_3, range(30)))

# This works, but we can achieve the same result using a list comprehension 
# in a more concise and readable way
divisibles_compr = [x for x in range(30) if x % 3 == 0]

print(divisibles_filter)
print(divisibles_compr)

# Multiplying all integers in a list by 3
# Option 1: using map()
def multiply_by_3(num: int):
    return num * 3
products_map = list(filter(multiply_by_3, range(30)))

# Option 2: list comprehension
products_compr = [x * 3 for x in range(30)]

print(products_map)
print(products_compr)

# Dict Comprehensions
prices_galleons = {"butter_beer": 0.5, "bertie_botts_beans": 0.75, "wand": 10.99}
galleon_to_dollar = 6.64
prices_dollar = {item: value * galleon_to_dollar for (item, value) in prices_galleons.items()}
print(prices_dollar)

# Set Comprehensions
students = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Harry Potter"]
# Filtering out duplicates
# Option 1: for loop
students_unique_loop = []
for student in students:
    if student not in students_unique_loop:
        students_unique_loop.append(student)

# Option 2: set comprehension
students_unique_compr = {student for student in students}

print(students_unique_loop)
print(list(students_unique_compr))