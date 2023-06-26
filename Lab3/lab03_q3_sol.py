# -*- coding: utf-8 -*-
"""
Lab 3 v1 q3
"""
import random 

def throwUntil(summ):
    """ Assumes sum is an int and 2 <= sum <= 12
    Simulates throwing a pair of dice until getting desired sum
    Displays the die values whose die total is equal to sum
    Returns the number of rolls to get the desired sum
    
    Parameters:
         summ = sum of the two dice
    Returns:
        how many times the dice are rolled to have the summ value
    """
    count = 1
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    while die1 + die2 != summ:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        count = count + 1

    print('Die1', die1, 'Die2', die2)
    return count

desiredSum = int(input('Enter sum of dice: '))
while desiredSum < 2 or desiredSum > 12:
    print('Sum must be between 2 and 12 inclusive')
    desiredSum = int(input('Enter sum of dice: '))
    
numRolls = throwUntil(desiredSum)
print('Dice are rolled', numRolls, 'times to get the sum', desiredSum)