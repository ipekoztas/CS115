# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""

DISCOUNT = 0.2
TAX = 0.15
pAmount = float(input("Enter purchase amount(in dollars): "))
dAmount = pAmount * DISCOUNT
discounted = pAmount - dAmount
taxAmount = discounted * TAX
paid = discounted + taxAmount 
		
print("Amount discount: $",dAmount)
print("Price after discount: $",discounted)
print("Sales Tax: $",taxAmount)
print("Amount due: $",paid)