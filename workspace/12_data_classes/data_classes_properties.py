from dataclasses import dataclass, field
import random
import timeit
from functools import partial

# Default values


@dataclass
class Magician:
    name: str
    minor: bool = True
    id: int = field(repr=False, default=random.randint(100000, 999999))


neville = Magician(name="Neville Longbottom")
print(neville)  # Magician(name='Neville Longbottom', minor=True)
print(neville.id)  # 245761 (can be different)


# init=False and __post_init__
@dataclass
class Magician:
    name: str
    age: int
    minor: bool = field(init=False)

    def __post_init__(self):
        self.minor = True if self.age < 18 else False


harry = Magician(name="Harry Potter", age=19)
print(harry.minor)  # False


# Setting order=True
# automatically adds special methods to compare instances beyond equality

@dataclass(order=True)
class Magician:
    # sort_index: int = field(init=False, repr=False)
    name: str
    age: int

    # def __post_init__(self):
    #     self.sort_index = self.age


harry = Magician(name="Harry Potter", age=17)
neville = Magician(name="Neville Longbottom", age=16)

print(harry > neville)  # False

# freezing data classes


@dataclass(frozen=True)
class Magician:
    name: str
    age: int


harry = Magician(name="Harry Potter", age=17)
print(harry)  # Magician(name='Harry Potter', age=17)
# harry.name = "Peter Crouch"  # raises a dataclasses.FrozenInstanceError exception

# optimizing data classes using slots


@dataclass
class SimpleMagician:
    name: str
    age: int
    house: str


@dataclass
class SlotMagician:
    __slots__ = ["name", "age", "house"]
    name: str
    age: int
    house: str


def get_set(magician):
    magician.name
    magician.name = "Harry Potter"


simple_harry = SimpleMagician(name="Harry Potter", age=16, house="Gryffindor")
slot_harry = SlotMagician("Harry Potter", 16, "Gryffindor")
slots = min(timeit.repeat(
    partial(get_set, slot_harry), number=100000))
no_slots = min(timeit.repeat(
    partial(get_set, simple_harry), number=100000))

print(f"% performance improvement: {(no_slots - slots) / no_slots:.2%}")
