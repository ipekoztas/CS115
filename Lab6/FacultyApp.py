# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:26:29 2020

"""

from Faculty import *

def read_file(fn):
    f = open(fn, 'r')
    university = []
    
    for line in f:     
        parts = line.strip().split(',')
        fac = Faculty(parts[0], parts[1], parts[2])
        university.append(fac)  
  
    f.close()
    return(university)

university = read_file('faculties.txt')

building = input("Enter building name ('A','B','C'): ")
for faculty in university:
    if faculty.isMember(building.upper()):
            print(faculty)

name = input('Enter name: ')   
found = False
i = 0
for faculty in university:
    if faculty.getName() == name:
        building = input('Enter new building: ')
        roomNo = input('Enter room no: ')
        faculty.setBuilding(building)
        faculty.setRoom(roomNo)
        found = True
        break
         
if not found:
    building = input('Enter building: ')
    roomNo = input('Enter room no: ')
    newFaculty = Faculty(name, building, roomNo)
    university.append(newFaculty)
    
university.sort()
print(university)

         


    

    
    

    

    

     

    
    
    
    
    
