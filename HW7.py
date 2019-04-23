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
test = laptime_1000th_race[['DriverName','lap','miliseconds']]
test_gp = test.pivot(index = 'lap',columns = 'DriverName',values = 'miliseconds')
test_gp.plot()
plt.show()

print(laptime_1000th_race.head())
print(test.head())