# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""
MAIN = 15
STARTER = 10
DESSERT = 8

budget = int(input("Enter budget: "))
totalMeal = 0
        
#if enough for main
if budget >= MAIN:
    totalMeal = MAIN
    print("Main dish added.")
    budget = budget - totalMeal
    if budget >= STARTER:
        totalMeal += STARTER
        print("Starter added.")
        budget -= STARTER
    else:
        print("Budget not sufficient for starter...")
    if budget >= DESSERT:
        totalMeal += DESSERT
        print("Dessert added.")
        budget -= DESSERT
    else:
        print("Budget not sufficient for dessert...")

    print(f"Total Meal Cost: {totalMeal:} Remaining Budget: {budget:}" )

else:
    print("More money needed")
