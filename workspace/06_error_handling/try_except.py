# 1. try / except
#   The try clause is executed first. If an Exception occurs, the except clause is executed.
#   Else, the except clause is skipped.

def calculate_mean(nums: list):
    try:
        mean = sum(nums) / len(nums)
        print(mean)
    except:
        print("Cannot calculate the mean for the given input.")


calculate_mean([2, 5, 6, 6, 9, 3])  # works fine
calculate_mean(["one", "two", "three"])  # throws an Exception

# Let's be a bit more specific


def calculate_mean(nums):
    try:
        mean = sum(nums) / len(nums)
        print(mean)
    except TypeError:
        print("The input must be a list of numbers.")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")


calculate_mean(["one", "two", "three"])  # The input must be a list of numbers.
calculate_mean([])  # ZeroDivisionError: division by zero
# calculate_mean(x) # throws a NameError, since the variable 'x' is not defined

# 2. finally
#   The finally clause is always executed after the try and except clauses


def calculate_mean(nums):
    try:
        mean = sum(nums) / len(nums)
        print(mean)
    except:
        print("Cannot calculate the mean for the given input.")
    finally:
        # in real world apps, 'finally' is useful for releasing external resources
        print(f"Executed calculate_mean for input: {nums}")


calculate_mean([2, 5, 6, 6, 9, 3])
calculate_mean(["one", "two", "three"])

# 3. else


def calculate_mean(nums):
    try:
        mean = sum(nums) / len(nums)
    except:
        print("Cannot calculate the mean for the given input.")
    else:
        print(mean)

# 4. raising an exception


def buy_butter_beer(age: int):
    if age < 18:
        raise ValueError("You must be at least 18 to buy Butter Beer.")
    print("Enjoy your Butter Beer!")


buy_butter_beer(16)  # throws a ValueError
