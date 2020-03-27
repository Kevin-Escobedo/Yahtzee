#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import random

class Die:
    def __init__(self, sides:int = 6):
        self.sides = sides
        self.rolls = []

    def roll(self):
        '''Rolls the die'''
        roll = random.randrange(1, self.sides + 1)
        self.rolls.append(roll)
        return roll
