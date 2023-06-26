# -*- coding: utf-8 -*-
"""
@author: CS115
"""
from Passenger import Passenger


def load_passengers( fname ):
    passengers = []
    my_file = open(fname, 'r')
    #with open(fname) as my_file:
    for line in my_file:
        data = line.split(';')
        pname = data[0]
        psurname = data[1]
        fare = float( data[2] )
        seatNo = data[3].strip()
        passenger = Passenger( pname, psurname, seatNo, fare )
        if passenger not in passengers:
            passengers.append( passenger )
        else:
            print(f'duplicate - passenger {pname} {psurname} {seatNo} not added.*.')
    my_file.close()
    return passengers

def min_index( lst, start ):
    ind = start
    for i in range(start + 1, len(lst)):
        if  lst[i].getSeatNumber() < lst[ind].getSeatNumber():
            ind = i
    return ind
        
def sort_passengers_by_seat( lst ):
    suffixStart = 0
    while suffixStart != len(lst):
        min_ind = min_index( lst, suffixStart)
        lst[suffixStart], lst[min_ind] = lst[min_ind], lst[suffixStart]
        suffixStart += 1
    
def search_passenger_by_seat( lst, search_seat ):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        if lst[mid].getSeatNumber() > search_seat:
            last = mid - 1
        elif lst[mid].getSeatNumber() < search_seat:
            first = mid + 1
        else:
            return lst[mid]
    return None

def search_passenger_by_surname( lst, surname, n ):
    if n == 0:
        return []
    else:
        matching_surnames = search_passenger_by_surname( lst, surname, n-1)
        if lst[n - 1].getPassengerSurname().lower() == surname.lower():
            matching_surnames.append( lst[n - 1] )
        return matching_surnames
    
    
    
passenger_list = load_passengers( 'passengers.txt' )
print('Original list of Passengers: ')
print( passenger_list )

#sort the list of passengers
sort_passengers_by_seat( passenger_list )
print('Passengers sorted by seat: ')
print( passenger_list )

search_seat = input('Enter seat to search: ')
passenger_in_seat =  search_passenger_by_seat( passenger_list, search_seat )
if passenger_in_seat:
    print( passenger_in_seat )
else:
    print(f'No passenger in {search_seat}')

search_surname = input('Enter surname to search: ')
matching_passengers = search_passenger_by_surname(passenger_list, search_surname, len(passenger_list))
if matching_passengers:
    print('List of matching passengers:\n',matching_passengers)
else:
    print(f'No passengers with surname {search_surname} found')
    
passenger_list.sort()
print('Passengers sorted by surname/seat number: ')
print( passenger_list )