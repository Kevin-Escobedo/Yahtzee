#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import random

class Die:
    def __init__(self, sides:int = 6):
        self.sides = sides

    def roll(self):
        '''Rolls the die'''
        return random.randrange(1, sides + 1)
