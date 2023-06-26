# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:14:18 2020

"""

class Faculty:
    def __init__(self, name, buil, room):
        self.__name = name
        self.__building = buil
        self.__room = room
        
    def getName(self):
        return self.__name
    
    def getBuilding(self):
        return self.__building
    
    def getRoom(self):
        return self.__room
    
    def setBuilding(self, buil):
        self.__building = buil
        
    def setRoom(self, room):
        self.__room = room
           
    def __str__(self):
        s = 'Faculty Name:\t' + self.__name
        s += '\tAddress:\t' + self.__building + self.__room
        return s
    
    def __repr__(self):
        s = '(Faculty)\t' + self.__name
        s += '\t' + self.__building + self.__room
        return s
    
    def __lt__(self, other):
        if self.__building != other.__building:
            return self.__building < other.__building
        else:
            return self.__room < other.__room
   
    def isMember(self, type):
        if self.__building == type:
            return 'Yes'
        else:
            return False
        
    

        
        
    
    
