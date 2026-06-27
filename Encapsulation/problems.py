# Hiding data from direct access.

# Example:

# ATM hides internal bank details.

# prb 1

class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

b = Bank()

b.show_balance()

# prb: 2

class Student:
    def __init__(self):
        self.__marks = 90

    def show(self):
        print(self.__marks)

s = Student()

s.show()