# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:21:06 2020


"""
def sumT(t):
    """
    finds the sum of numeric values in t and returns a new tuple of 
    these numeric values

    Parameters
    ----------
    t : tuple
        tuple of mixed type values
    
    Returns
    -------
    summ : int
           sum of numeric values in t
    newT: tuple
          tuple of numeric values

    """
    newT = ()
    
    for e in t:
        if type(e) == int or type(e) == float:
            newT += (e,)
    
    return newT
        
t1 = ((3,5),5, False, 2.5, 'cs115', [1,2,3], 7.8)
print('Original tuple:')
print(t1)

t2 = sumT(t1)

print('New Tuple:')    
print(t2)
print('Sum of new tuple is', sum(t2))
    
    
