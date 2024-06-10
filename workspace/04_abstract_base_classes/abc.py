# Option 1: Using the metaclass ABCMeta
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass

# Option 2: Using the helper class ABC to define your own
# ABC through inheritance
from abc import ABC, abstractmethod

class MyABC(ABC):
    @abstractmethod
    def my_method(self):
        pass


class Parent:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Child(Parent):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return "bar() called"

parent = Parent() # doesn't throw an error
child = Child() # doesn't throw an error
child.bar() # raises NotImplementedError