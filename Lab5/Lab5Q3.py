# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 08:49:44 2018

@author: user
"""

def import_cars( fileName, car_dict):
    file = open(fileName, 'r')
    for line in file:
        data = line.split(':')
        if data[0] in car_dict:
            car_dict[data[0]] += (data[1][:-1],)
        else:
            car_dict[data[0]] = (data[1][:-1],)
    file.close()

def find_by_city( city, car_dict ):
    car_list = []
    car_count = 0
    city_count = 0
    for car in car_dict:
        cars = car_dict[car]
        for c in cars:
            car_count += 1
            city_code = c[0:2]
            if city_code == city:
                city_count += 1
                if car not in car_list:
                    car_list.append(car)
    
    return (car_list,(city_count/car_count)*100)
                

c_dict = {}
import_cars('cars.txt', c_dict)
c_code = input('Enter city code to search: ')

models,percentage = find_by_city(c_code, c_dict)
print('Models with city code',c_code,models)
print('Percentage of cars from',c_code,':',percentage)
