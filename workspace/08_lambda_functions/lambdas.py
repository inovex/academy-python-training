# sources: https://docs.python.org/3/reference/expressions.html
# https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8

# Lambda expression = anonymous function
# The expression 'lambda parameters: expression' yields a function object which behaves like:
# def <lambda>(parameters):
#   return expression

# example:
# regular Python function:
def double(x: int):
    return x * 2

# lambda function:
lambda x: x * 2

# PROS:
# - good for simple logical operations
# - makes code more readable
# - good if used only once

# CONS:
# - not suited for more sophisticated expressions that have multiple independent operations
# - bad for long operations, e.g., with nested conditional statements
# - it is not possible to add docstrings explaining the function's usage/parameters/output


# using a lambda function with map() to transform the students' names to lowercase
students_upper = ["HARRY POTTER", "DRACO MALFOY", "HERMIONE GRANGER", "RONALD WEASLEY"]
students_lower = list(map(lambda x: x.lower(), students_upper)) 


# using a lambda function with filter() to get students who scored more than 80 points and passed the exam
astronomy_marks = [
    ("Harry Potter", 80),
    ("Hermione Granger", 100),
    ("Draco Malfoy", 77),
    ("Ron Weasley", 82)
]
astronomy_passed = list(filter(lambda student: student[1] > 80, astronomy_marks))
# --> [('Hermione Granger', 100), ('Ron Weasley', 82)]

# using a lambda function to sort the students by their marks in descending order
marks_sorted_no_key = sorted(astronomy_marks) # sorts the students by their names in alphabetical order
# [('Draco Malfoy', 77), ('Harry Potter', 80), ('Hermione Granger', 100), ('Ron Weasley', 82)]
marks_sorted = sorted(astronomy_marks, key=lambda student: -student[1])
# [('Hermione Granger', 100), ('Ron Weasley', 82), ('Harry Potter', 80), ('Draco Malfoy', 77)]

# lambda with conditional
items_prices = [("butter_beer", 0.5), ("bertie_botts_beans", 0.75), ("wand", 10.99), ("invisibility_cloak", 299)]

# apply a 10% discount to items that cost more than 10 galleons
items_discount = list(
    map(
        lambda item: (item[0] ,item[1] / 1.10) if item[1] > 10 else item, 
        items_prices
    )
)
print(items_discount)