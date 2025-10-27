class Animal:
    def speak(self):
        print("Animal is speaking")

class Cat(Animal):
    def speak(self):
        # super().speak()
        print("Мяу")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Гав")

class CatDog(Cat, Dog):
    def speak(self):
        super().speak()
        print("мяу гав")

kotopes = CatDog()
kotopes.speak()
print(CatDog.__mro__) # method resolution order
print(Dog.__mro__)
puppy = Dog()
puppy.speak()