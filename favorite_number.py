"""
Simple program that prompts a user's favorite number, stores it, and prints it out.

Author: Oscar Lopez
Date: Jan 11, 2019
"""
import json


class favorite_number():
    
    def __init__(self):
        self.prompt_user()
        self.save_number()
        print(self.read_number())
    
    def prompt_user(self):
        while True:
            try:
                self.number = int(input("What is your favorite number?\n"))
                break
            except ValueError:
                print("ERROR: Please enter a valid number!")
    
    def save_number(self, filename = 'favorite_number.json'):
        with open(filename,'w') as f_obj:
            json.dump(str(self.number),f_obj)
    
    def read_number(self,filename = 'favorite_number.json'):
        try:
            with open(filename) as f_obj:
                return json.load(f_obj)
        except FileNotFoundError:
            print("ERROR! File " + filename + " cannot be read!")


favorite_number()