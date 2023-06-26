# -*- coding: utf-8 -*-
"""
Lab 3 v1 q2
"""
KEY = "a@bpdqi!l1mwnuo0s5t+z2A4B8E3G6WM"

def convert_text(sent):
    new_sent = ''
    for i in sent:
        if i.islower():
            code = ord(i) - 3
            char = chr(code)
        elif i.isupper():
            code = ord(i) + 3
            char = chr(code)
        elif not i.isalnum():
            char = '#'
        
        new_sent += char
        
    return new_sent

phrase = input("Enter a phrase for conversion: ")
converted_phrase = convert_text(phrase)

if phrase == "":
    print("No phrase entered.")
else:
    print("Text you entered: '" + phrase + "'")
    print("After conversion: '" + converted_phrase + "'")
    
   
    
            

