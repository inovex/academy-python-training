
# Remember: functions are first-class objects
# source: https://www.datacamp.com/tutorial/decorators-python

# assigning functions to Variables
def add_one(number: int):
    return number + 1

plus_one = add_one
plus_one(5) # returns 6

# defining functions inside other functions
def adder(summand: int):
    def add_summand(number: int):
        return number + summand
    return add_summand

plus_3 = adder(3)
print(plus_3(5)) # 8

# passing functions as arguments to other functions
def add_one(number: int):
    return number + 1

def apply_to_list(function, numbers):
    return [function(x) for x in numbers]

print(apply_to_list(add_one, [1, 2, 3])) # prints [2, 3, 4]

# functions returning other functions
def add_one():
    def plus_one(number: int):
        return number + 1
    
    return plus_one

returned_add_one = add_one()
print(returned_add_one) # prints <function add_one.<locals>.plus_one at 0x7fd93d87a3a0>
print(returned_add_one(7)) # prints 8

# nested functions have access to the enclosing function's variable scope
def add_one(number: int):
    # enclosing function
    def plus_one():
        # nested function
        return number + 1
    
    return plus_one()

print(add_one(4)) # prints 5