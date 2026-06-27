# Child gets properties from Parent.

# Example:

# Dog is an Animal.

# prb 1

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()

d.sound()