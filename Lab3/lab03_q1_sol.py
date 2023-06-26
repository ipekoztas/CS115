# -*- coding: utf-8 -*-
"""
Lab 3 q1 (v1)
"""

def swap(sent1):
    """
    Returns a new sentence by swapping the first and last
    words of the given sentence
    Parameters:
        sent1: the given original sentence
    Returns:
        sent2: the new sentence
    """
   
    result = sent1
    ind1 = sent1.find(' ')
    
    if ind1 != -1:
        ind2 = sent1.rfind(' ')
        result = sent1[ind2+ 1:] 
        if ind1 != ind2:
            result += ' '
        result += sent1[ind1 + 1:ind2] + ' '
        result += sent1[:ind1]
        
    return result


sentence = input("Enter your sentence: ")
sentence = sentence.strip()

while sentence.lower() != 'exit':
    new_sent = swap(sentence) 
    print("New Sentence:", new_sent)
    sentence = input("Enter your sentence: ")
    sentence = sentence.strip()



