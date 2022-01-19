# Maximo Antigua
#Dice Roll Simulator
 
from random import randrange
"""
This is a basic program that will take an integer and compare it with the result of two others.
These numbers are from 1 to 6, just like a dice. Every iteration these two numbers change.

"""

def diceRoll(num):

    if num > 6:
        print('Please input a number between 1 and 6.')
    elif num <= 6:
        print('Tossing dice...')
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)
        print('... and we got a {dice1} and a {dice2}!!'.format(dice1=dice1, dice2=dice2))
        if dice1 == num or dice2 == num:
            print('You matched with one of the numbers!')
        else:
            print('Your number did not match with the dice :(' )

diceRoll(6)
