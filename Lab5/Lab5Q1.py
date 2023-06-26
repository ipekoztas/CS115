# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:54:54 2022

"""

import random 


def fill_list(n):
    """
    creates a list of n integers between 2 and 50
    
    Parameters:
        n: int
           number of random integers
    Returns:
        l1: list
            list of integers between 2 and 50
    """
    
    l1 = []
    for i in range(n):
        l1.append(random.randint(2,51))
                  
    return l1

def eliminate_values(list1):
    """
    removes the repeated copies of the elements in the list
    
    Parameters:
        list1: list
            list of integers between 2 and 50
    
    """
    i = 0
    while i < len(list1):
        if list1[i] in list1[:i]:
            list1.pop(i)
        else:
            i += 1

n = int(input('Enter the number of elements:'))            
my_list = fill_list(n)
print('Original list:')
print(my_list)
eliminate_values(my_list)
print('List with multiples removed:\n',my_list)