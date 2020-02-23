#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from dice import Die

class YahtzeeGame:
    def __init__(self, num_of_dice:int = 5):
        self.num_of_dice = num_of_dice
        self.die = Die()

    def roll(self, num:int) -> [int]:
        '''Rolls num amount of dice'''
        return [self.die.roll() for i in range(num)]
