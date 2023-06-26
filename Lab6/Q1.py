# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:56:27 2022

@author: user
"""

def valuesBefore(m, n):
    """
    finds how many values are before n in each column of m
    Parameters
    ----------
    m: matrix
       of integer values
    
    n : int
        given value

    Returns
    -------
    res: list
         int list keeping the number of values that are present 
         before n for each column of m

    """
    count = 0
    res = []
    found = False
    
    for col in range(len(m[0])):
        for row in range (len(m)):
            if mat[row][col] == n:
                res.append(count)
                found = True
                break
            else:
                count += 1
    			
    	#if search value does not exist, store -1
        if not found:
            res.append(-1)
     		
     	#reset found and count before next column
        found = False;
        count = 0
        
    return res

mat = [[2,4,8,6],[6,2,2,5],[8,7,7,9],[4,6,2,3],[8,9,3,8]]
n = int(input('Enter the number to search: '))
result = valuesBefore(mat, n)

for i in range (len(result)):
    if result[i] != -1:
        print(f'There are {result[i]} values before {n} in column {i}')
    else:
        print(f'There is no {n} in column {i}')
                