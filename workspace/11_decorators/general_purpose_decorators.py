def debugging_decorator(function):
    def wrapper(*args, **kwargs):
        print(
            f"Calling function {function.__name__} with arguments: {args} {kwargs}"
        )
        result = function(*args, **kwargs)
        print(f"{function.__name__} returned: {result}")
        return result
    return wrapper


@debugging_decorator
def add(a, b):
    return a + b


add(1, 2)  # Calling function add with arguments: (1, 2) {} add returned: 3
# Calling function add with arguments: () {'a': 1, 'b': 2} add returned: 3
add(a=1, b=2)
