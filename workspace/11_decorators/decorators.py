# @decorator_function
# def my_function():
#     pass

# example: apply the input function to each element of a list
def list_decorator(function):
    def wrapper(numbers_list):
        return [function(number) for number in numbers_list]
    
    return wrapper

my_numbers = [1, 3, 5, 7]

# def add_one(number):
#     return number + 1

# decorate = list_decorator(add_one)
# print(decorate(my_numbers)) # prints [2, 4, 6, 8]

@list_decorator
def add_one(number):
    return number + 1

print(add_one(my_numbers)) # prints [2, 4, 6, 8]

# applying multiple decorators at once
def list_decorator_2(function):
    def wrapper(numbers_list):
        # print(function)
        x = function(numbers_list)
        return sum(x)
    return wrapper

# decorators are applied one after another, from bottom to top
@list_decorator_2
@list_decorator
def add_one(number):
    return number + 1

print(add_one([1,3,5,7])) # prints 20

# decorators with parameters
def repeat(num_times):
    def decorator_repeat(function):
        def wrapper(number):
            result = number
            for _ in range(num_times):
                result = function(result)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def add_one(number):
    return number + 1

print(add_one(3)) # prints 6 (= add_one was applied 3 times)