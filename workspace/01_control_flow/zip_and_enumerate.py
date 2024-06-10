names = ["Harry", "Luna", "Draco"]
houses = ["Gryffindor", "Ravenclaw", "Slytherin"]

for name, house in zip(names, houses):
    print(f"{name} is part of house {house}")


alphabet = list("abcdefghijklmnopqrstuvwxyz")
for idx, char in enumerate(alphabet):
    print(f"Character {char} is letter {idx} in the alphabet")