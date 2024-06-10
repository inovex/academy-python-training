from functools import wraps

def list_decorator(function):
    def wrapper(numbers_list):
        """This is the wrapper function"""
        return [function(number) for number in numbers_list]
    
    return wrapper

@list_decorator
def add_one(number):
    "Adds one to the input number."
    return number + 1

# The metadata of the decorated function is hidden!
print(add_one.__name__) # prints wrapper
print(add_one.__doc__) # prints This is the wrapper function

# It is good practice to use functools.wraps in order to
# copy the decorated function's metadata to the decorated closure
def list_decorator(function):
    @wraps(function)
    def wrapper(numbers_list):
        return [function(number) for number in numbers_list]
    return wrapper 

@list_decorator
def add_one(number):
    "Adds one to the input number."
    return number + 1

print(add_one.__name__) # prints 'add_one'
print(add_one.__doc__) # prints 'Adds one to the input number'