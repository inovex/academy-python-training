def function_name(param1, param2):
    result = ...
    return result


def say_hi(language):

    if language == "German":
        greeting = "Hallo"

    elif language == 'Spanish':
        greeting = 'Hola'

    elif language == 'English':
        greeting = 'Hi'

    elif language == 'French':
        greeting = 'Bonjour'

    return greeting


print(say_hi("Spanish"))


# Exercise: Write a function that loops through a given string
# and returns the number of vowels in the string

def count_vocals(word: str = "default"):
    total = 0
    for char in word:
        if char in ("a", "e", "i", "o", "u"):
            total += 1

    return total


count_vocals(word="hello")

print(count_vocals("hello") == 2)
print(count_vocals("nnn") == 0)
print(count_vocals("aaeeiioouu") == 10)
