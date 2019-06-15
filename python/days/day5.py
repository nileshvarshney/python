""" create a class that has 2 methods :
1.  getString : grab string from input
2.  printStriang : Print string in upper case
"""
class Day5(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input('give me a string ...')
    def printStriang(self):
        print(self.s.upper())

x = Day5()
x.getString()
x.printStriang()