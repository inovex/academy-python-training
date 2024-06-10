import sys


def yield_multiple_statments():
    yield "This is the first statment"
    yield "This is the second statement"
    yield "This is the last statement. Don't call next again!"


example = yield_multiple_statments()
print(next(example))  # prints "This is the first statement"
print(next(example))  # prints "This is the second statement"
print(next(example))  # prints "This is the last statement. Don't call next again!"
# print(next(example)) # raises a StopIteration exception

# Let's replace the PowTwo Iterator class we created earlier
# with a generator object

# the Iterator class...


class PowTwo:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# ...can be implemented as a generator as follows


def pow_two(max: int):
    for pow in range(max + 1):
        yield 2 ** pow


powers = pow_two(2)
print(powers)  # prints <generator object powTwo at 0x7f924d3f39e0>
print(next(powers))  # prints 1 (2^0)
print(next(powers))  # prints 2 (2^1)
print(next(powers))  # prints 4 (2^2)
# print(next(powers)) # raises a StopIteration exception

print(list(pow_two(2)))  # prints [1, 2, 4]

# Generator expressions
nums_squared_list = [x*x for x in range(100)]
nums_squared_generator = (x*x for x in range(100))

# print the sizes of the objects in bytes
print(
    sys.getsizeof(nums_squared_list), 
    sys.getsizeof(nums_squared_generator)
) # 904 112
