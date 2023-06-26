# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:40:23 2022

@author: can
"""
phrase = input("Enter a phrase (or 'exit'): ")

while phrase.upper() != 'EXIT':
    space = 0
    while len(phrase) > 0:
        print(space * ' ' + phrase)
        phrase = phrase[1:-1]
        space += 1
    print()
    phrase = input("Enter another phrase (or 'exit'): ")
    
print("End of program.")








