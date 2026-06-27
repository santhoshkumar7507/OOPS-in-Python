# Program 1
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("santhosh")

# s1.display()
# Explanation
# Variable → name
# Method → display()

# prb 2

class Car:
    def __init__(self, color):
        self.color = color

    def show(self):
        print(self.color)

c1 = Car("Red")

c1.show()