# -*- coding: utf-8 -*-
"""
@author: CS115
"""

import Lab04_yourname_module as md

inFileName = "input.txt"
outFileName = "output.txt"
       
choice = md.displayMenu()
choice = choice.lower()

while choice != 'd':
    domain = input("Enter domain to search: ")
    domain = domain.strip()
    
    #get email by domain			
    if choice == 'a':
        numEmail = md.getEmailByDomain(domain, inFileName)
       	if numEmail == 0 :
            print("No Users Found!" )
        else:
            print(str(numEmail) + " users exist in " + domain + " domain")
    #get user names in file
    elif choice == 'b':
       	md.displayUsersByDomain(domain)
    #get user names that include numeric value   					
    elif choice == 'c':
        md.displayUsersHavingNumeric(domain)
    else:
        print('Invalid Choice!')
       					
    choice = md.displayMenu()
        