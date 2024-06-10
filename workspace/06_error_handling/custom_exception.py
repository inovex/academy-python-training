class HouseError(Exception):
    pass


for student in [("Harry Potter", "Gryffindor"), ("Draco Malfoy", "Slytherin")]:
    if student[1] != "Gryffindor":
        raise HouseError("This student is not allowed to enter the room!")
    print(f"Welcome to the Gryffindor Common Room, {student[0]}")


class HouseError(Exception):
    def __init__(self, house):
        self.house = house
        self.message = f"Students from {house} are not allowed to perform this action!"
        super().__init__(self.message)


for student in [("Harry Potter", "Gryffindor"), ("Draco Malfoy", "Slytherin")]:
    if student[1] != "Gryffindor":
        raise HouseError(student[1])
    print(f"Welcome to the Gryffindor Common Room, {student[0]}")
