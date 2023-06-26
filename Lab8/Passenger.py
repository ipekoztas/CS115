# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class Passenger:
    __airportTax = 0.03
    __fareLimit = 1000
    
    def __init__( self, pname, psurname, seatNo, fare ):
        self.__passengerName = pname
        self.__passengerSurname = psurname
        self.setSeatNumber( seatNo )
        self.__fare = fare
    
    def getPassengerName( self ):
        return self.__passengerName
    
    def getPassengerSurname( self ):
        return self.__passengerSurname
    
    def getSeatNumber( self ):
        return self.__seatNumber
  
    def setSeatNumber( self, seatNumber ):
        if len( seatNumber ) < 3:
            self.__seatNumber = 'unassigned'
        elif seatNumber[0:2].isdigit() and seatNumber[2].isalpha():
            self.__seatNumber = seatNumber[0:2] + seatNumber[2].upper()
        else:
            self.__seatNumber = 'unassigned'
    
    def calculate_fare( self ):
        if self.__fare < Passenger.__fareLimit:
            return self.__fare * (1 + Passenger.__airportTax )
        return self.__fare
    
    def __repr__( self ):
           rep = f'{self.__passengerSurname}, {self.__passengerName[0]}. '
           rep += f'({self.__seatNumber}) Fare: {self.calculate_fare():.2f}TL\n'
           return rep
           