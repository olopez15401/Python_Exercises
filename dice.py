from random import randint


class dice():

    """ A simple dice program. """

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(str(randint(1, self.sides)))

"""
my_die = dice()
my_die.roll_dice()
my_die.roll_dice()
"""
