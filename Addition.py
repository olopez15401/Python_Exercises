"""
A simple addition program.
Author: Oscar Lopez
Date: Jan 8, 2019.
"""

class addition():
    def __init__(self):
        self.input_numbers()
        print(self.add(self.x, self.y))

    def add(self, x, y):
        return int(x) + int(y)

    def input_numbers(self):
        print("Please enter two numbers to add together:")
        while True:
            try:
                self.x = int(input())
                self.y = int(input())
                break
            except ValueError:
                print('ERROR: Make sure you enter valid numbers!')

addition()