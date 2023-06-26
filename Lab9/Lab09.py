# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:08:22 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

country_data = np.loadtxt('world-happiness-report_country.csv', skiprows = 1, dtype = 'str', delimiter = ',')
indicators = np.loadtxt('world-happiness-report_data.csv', skiprows = 1, delimiter = ',')

#extract the names of the country and their 2019 data
data_2019 = indicators[indicators[:,0] == 2019]
countries_2019 = country_data[np.where(indicators[:,0] == 2019)]


#create a two-dimensional array where the leftmost column stores
#the country names and the rightmost column stores the healthy
#life expectancy at birth for 2019
increased = data_2019[:,4]*1.1
file_data = np.array([countries_2019,increased])
 
#output the data to a file, 2017_data.txt
np.savetxt('increased_data.txt', file_data.T, fmt = '%s')

plt.figure(1)
plt.clf()

plt.subplot(2,1,1)
plt.plot(data_2019[0:21,8])
plt.plot(data_2019[0:21,6])
plt.legend(['Positive Affect','Generosity'])
plt.title('Relationship between Positive Affect and Generosity(2019)')

plt.subplot(2,1,2)
(vals, bounds, other) = plt.hist(data_2019[:,4],5)
plt.title('Frequency of Healthy Life Expectancy at Birth (2019)')
plt.xticks(bounds)

min_gdp_2019 = np.min(data_2019[:,2])
min_gdp_2019_pos = np.argmin(data_2019[:,2])
min_country_2019  = countries_2019[min_gdp_2019_pos]

max_gdp_2019 = np.max(data_2019[:,2])
max_gdp_2019_pos = np.argmax(data_2019[:,2])
max_country_2019  = countries_2019[max_gdp_2019_pos]

plt.figure(2)
plt.clf()
plt.title('Comparison of Lowest and Highest Log GDP(2019)')
plt.bar(min_country_2019, min_gdp_2019, color='red')
plt.bar(max_country_2019, max_gdp_2019, color = 'green')