# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 11:43:30 2022

"""

NUM_LIGHT = 8
passed = 0
stopped = 0
 	 
for i in range(NUM_LIGHT):
    color = input("Enter the traffic light color R, G, Y for car " + str(i+1) +':')
    if color.upper() == 'R':     	   		
        stopped += 1
    elif color.upper() == 'Y':
        print("Ready to Pass")
    elif color.upper() == 'G':
        passed += 1
    else:
        print("Invalid traffic light color!")
       	   
percentPass = passed / NUM_LIGHT
print(f"Number of cars stopped: {stopped}")
print(f"Percentage of cars passed: {percentPass*100:.1f}%")





