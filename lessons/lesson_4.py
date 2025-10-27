from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self, sound):
        pass


class Dog(Animal):
    def make_sound(self, sound):
        print("Гав гав")

    def walk(self):
        print("<UNK> <UNK>")

class Cat(Animal):
    def make_sound(self, sound):
        print("мяяяяяяяу")

puppy = Dog()
puppy.make_sound("")