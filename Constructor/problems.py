# . Constructor (init)
# Constructor runs automatically when object is created.
# Think:
# When you buy a phone, setup happens automatically.

# prb:1
class Student:
    def __init__(self):
        print("Student Created")

s1 = Student()

# prb: 2

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Vignesh")

print(s1.name)