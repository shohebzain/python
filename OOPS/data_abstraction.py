"""class square:
    def __init__(self,side):
        self.side = side

class circle:
    def __init__(self,radius):
        self.radius = radius

obj = circle()
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animal types."""

    @abstractmethod
    def make_sound(self):
        """Make the animal produce a sound."""
        pass
class Dog(Animal):
    def make_sound(self):
        print("Dog says woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat says meow!")

if __name__ == "__main__":
    animals = [Dog(), Cat()]
    for animal in animals:
        animal.make_sound() 