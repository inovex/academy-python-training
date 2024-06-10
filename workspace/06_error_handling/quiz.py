def divide_five_by(x):
    try:
        print(5 / x)
    except:
        print("An error occured!")


# divide_five_by(0)


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")
        result = 0
    return result


print(divide(a, 0))
