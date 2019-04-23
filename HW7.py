#/usr/bin/python

import numpy as np 
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

print('hello pyx!')

# Get raw data from the website

constructors_field = ['constructorId','constructorRef','name','nationality','url']
drivers_field = ['driverId','driverRef','number','code','forename','surname','dob','nationality','url']
lap_times_field = ['raceId','driverId','lap','position','time','miliseconds']
pit_stops_field = ['raceId','driverId','stop','lap','time','duration','milliseconds']
races_field = ['raceId','year','round','circuitId','name','date','time','url']
results_field = ['resultId','raceId','driverId','constructorId','number','grid','position','positionText','positionOrder','points','laps','time','milliseconds','fastestLap','rank','fastestLapTime','fastestLapSpeed','statusId']

constructors = read_csv('constructors.csv', header = None, names = constructors_field)
drivers = read_csv('driver.csv', header = None, names = drivers_field)
lap_times = read_csv('lap_times.csv', header = None, names = lap_times_field)
pit_stops = read_csv('pit_stops.csv', header = None, names = pit_stops_field)
races = read_csv('races.csv', header = None, names = races_field)
results = read_csv('results.csv', header = None, names = results_field)

# Create dataset for the laptimes in the 1000th F1 Grand Prix in China

laptime_1000th_race = lap_times[lap_times.raceId == 1012].reset_index(drop = True)
laptime_1000th_race.insert(1,'RaceName',laptime_1000th_race['raceId'])
laptime_1000th_race['RaceName'].replace(races['raceId'].tolist(),races['name'].tolist(),inplace = True)
laptime_1000th_race.insert(3,'DriverName',laptime_1000th_race['driverId'])
laptime_1000th_race['DriverName'].replace(drivers['driverId'].tolist(),drivers['code'].tolist(),inplace = True)
laptime_1000th_race.to_csv('laptime_1000th_race.csv') # Export data to CSV file
test = laptime_1000th_race[['DriverName','lap','miliseconds']]
test_gp = test.pivot(index = 'lap',columns = 'DriverName',values = 'miliseconds')
# test_gp.plot()
# plt.show()

# Create dataset for Hamilton's laps in China Grand Prix

China_grand_prix = races[races.circuitId == 17].reset_index(drop = True)
laptime_ham_China = lap_times[lap_times.driverId == 1].reset_index(drop = True)
laptime_ham_China.insert(1,'RaceName',laptime_ham_China['raceId'])
laptime_ham_China.insert(1,'year',laptime_ham_China['raceId'])
laptime_ham_China['RaceName'].replace(races['raceId'].tolist(),races['name'].tolist(),inplace = True)
laptime_ham_China['year'].replace(races['raceId'].tolist(),races['year'].tolist(),inplace = True)
laptime_ham_China = laptime_ham_China[laptime_ham_China.RaceName == 'Chinese Grand Prix'].reset_index(drop = True)
laptime_ham_China.to_csv('laptime_ham_China.csv') # Export data to CSV file
test = laptime_ham_China[['year','lap','miliseconds']]
test_gp = test.pivot(index = 'lap',columns = 'year',values = 'miliseconds')
# test_gp.plot()
# plt.show()

#Create dataset for 


print(laptime_ham_China.head())
