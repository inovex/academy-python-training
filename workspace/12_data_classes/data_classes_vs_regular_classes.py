from dataclasses import dataclass

# Data class vs. regular class


@dataclass
class Point:
    x: int
    y: int


p1 = Point(1, 2)
p2 = Point(1, 3)

print(p1)  # prints Point(x=1, y=2)
print(Point(1, 2) == Point(1, 2))  # prints True


class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(MyPoint(1, 2))  # <__main__.MyPoint object at 0x7f652c9ca550>
print(MyPoint(1, 2) == MyPoint(1, 2))  # False

# adding __repr__ and __eq__ to MyPoint


class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyPoint(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, MyPoint):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented


p1 = MyPoint(1, 2)
p2 = MyPoint(1, 2)

print(p1)  # MyPoint(x=1, y=2)
print(p1 == p2)  # True
