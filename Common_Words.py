"""
A small program that determines the number
of functions in a python file.

Author: Oscar Lopez
Date: Jan 10, 2019
"""

class Common_Words():
    
    def __init__(self,filename):
        self.functions = 0
        self.readFile(filename)
        self.countFunctions()
        print(self.functions)

    def readFile(self,file):
        self.filename = file
        with open(self.filename) as file_object:
            self.contents = file_object.read()
    
    def countFunctions(self):
        self.functions = self.contents.count('def')
