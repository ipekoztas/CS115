# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:09:38 2022
"""

sumDeposit = 0
deposit = 0
       	  
balance = float(input("Enter the initial balance: "))
transaction = float(input("Enter the transaction amount: "))
       
while transaction != 0:
    balance += transaction
    if transaction > 0:
        deposit += 1
        sumDeposit += transaction
    transaction = float(input("Enter the transaction amount: "))
        
print(f"Balance: {balance}")
print(f"Average deposit amount: {sumDeposit/deposit:.2f}")