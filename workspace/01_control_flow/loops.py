houses = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]

# for house in houses:
#     print(house)

for number in range(5):
    print(number)

my_int = 42
while my_int < 45:
    print(my_int)
    my_int += 1

for house in houses:
    if house == "Slytherin":
        continue
    else:
        print(f"Congrats, you are not a Slytherin! You are in house {house}")


names = ["Harry", "Ron", "Hermione", "Luna", "Neville", "Ginny", "Draco"]
print("Harry".lower())
print("H" in "Harry")

for name in names:
    if "u" in name.lower():
        continue
    if name == "Ginny":
        print(name)
        break
    else:
        print(name)
