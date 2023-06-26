# -*- coding: utf-8 -*-
"""
@author: CS115
"""

def displayMenu():
    """
    display a menu and returns the choice entered by the user

    Returns
    -------
    choice
        string 
        choice entered by the user

    """
    print("Menu: ")
    print("(a) Find email by domain ")
    print("(b) Display users by domain")
    print("(c) Display numeric userNames by domain")
    print("(d) EXIT ");
    choice = input('Enter choice: ')

    while (choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd'){
        print("Menu: ")
        print("(a) Find email by domain ")
        print("(b) Display users by domain")
        print("(c) Display numeric userNames by domain")
        print("(d) EXIT ");
        choice = input('Enter choice: ')
    }
	
    return choice
    
def getEmailByDomain(sDomain, inFileName):
    """
    writes the email addresses in the given domain to a file

    Parameters
    ----------
    sDomain : str
        given domain
    inFileName : file handle
        input file

    Returns
    -------
    count : int
        number of emaill addreses in the given domain

    """
    count = 0
    outFileName = sDomain+".txt"
    
    #open input and output files
    inFile = open(inFileName, 'r')
    outFile = open(outFileName, 'w')
    	
    #read file
    for email in inFile:
        atSymbol = email.find("@")
        dotSymbol = email.find(".", atSymbol);
    		
        #get the domain
        domain = email[atSymbol+1:dotSymbol]
        if domain.lower() == sDomain:
            userName = email[0: atSymbol]
            outFile.write(userName + '\n')
            count += 1
            
    inFile.close()
    outFile.close()
    return count
    
def displayUsersByDomain(sDomain): 
    """
    displays the user names in the file

    Parameters
    ----------
    sDomain : str
        domain name

    Returns
    -------
    None.

    """
   
    inFileName = sDomain+".txt"
    
    try:
        inFile = open(inFileName, 'r') 	
        #read file
        for user in inFile:
            print(user.strip())
        inFile.close()
    except:
        print('File Not Found!')      
   
def displayUsersHavingNumeric(sDomain):
    """
    displays the user names that contain numeric values

    Parameters
    ----------
    sDomain : int
        given domain

    Returns
    -------
    None.

    """
    inFileName = sDomain + ".txt"
    
    try:
        inFile = open(inFileName, 'r')
        	
        #read file
        for user in inFile:
            containsNum = False
            for ch in user:
                if ch.isdigit():
                    containsNum= True
                    break
                
            if containsNum:
                print(user.strip())
        inFile.close()
                
    except:
        print('File Not Found')  
            
	    		
    
    	