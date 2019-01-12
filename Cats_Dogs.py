"""
A program that displays the names of the
dogs and cats in cats.txt and dogs.txt.

Author: Oscar Lopez
Date: Jan 8,2019
"""

class Cats_Dogs():


    def __init__(self,file_1='cats.txt',file_2='dogs.txt'):
        self.cat_file = file_1
        self.dog_file = file_2
        self.print_cat_file(self.cat_file)
        self.print_dog_file(self.dog_file)

    def print_cat_file(self,cat_file):
        try:
            with open(cat_file) as catfile:
                cats = catfile.read()
                print(cats)
        except FileNotFoundError:
            print('ERROR!: Cat file not found!')

    def print_dog_file(self,dog_file):
        try:
            with open(dog_file) as dogfile:
                dogs = dogfile.read()
                print(dogs)
        except FileNotFoundError:
            print('ERROR!: Dog file not found!')


#Defaults to standard cats.txt and dogs.txt as the parameters
Cats_Dogs()

#Will return FileNotFoundError file.
Cats_Dogs('somefile.pdf','afile.txt')