# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class Passenger:
    airportTax = 0.03
    fareLimit = 1000
    fuelSurcharge = 150
    
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
  
    def getFare( self ):
        return self.__fare
                   
    def __repr__( self ):
           rep = f'{self.__passengerSurname}, {self.__passengerName[0]}. '
           rep += f'({self.__seatNumber}) Fare: {self.calculate_fare():.2f}TL\n'
           return rep
       