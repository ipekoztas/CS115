# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""

TUITION = 14500
SINGLE_DORM = 5000
DOUBLE_DORM = 3500
MEAL = 600
        
dorm = input("Dormitory (y/n): ")
        
fee = TUITION
        
#if enough for main
if dorm.lower() == 'y':
    roomType = input("(S)ingle Room or (D)ouble Room: ")
        	
    if roomType.upper() == 'S':
        fee +=  SINGLE_DORM
    elif roomType.upper() == 'D':
        fee +=  DOUBLE_DORM

    addMeal = input("Add meal plan? T/F): ")
        	
    if addMeal.upper() == 'T':
        fee +=  MEAL
        	
print("Total Fee Due: $",fee)