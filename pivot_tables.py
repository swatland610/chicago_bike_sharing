import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

# import data
divvy_2019 = pd.read_csv('cleaned_data/divvy_2019_trips.csv')
divvy_2020 = pd.read_csv('cleaned_data/divvy_2020_trips.csv')

# Basic Chart Objects
divvy_2019_trips_by_chicago_area = divvy_2019.plot.bar(x=divvy_2019['chicago_area'], y=divvy_2019['trip_id'], color='blue')
divvy_2020_trips_by_chicago_area = divvy_2020.plot.bar(x=divvy_2020['chicago_area'], y=divvy_2020['trip_id'], color='red')

print(divvy_2019_trips_by_chicago_area, end="  ")
print(divvy_2020_trips_by_chicago_area, end="  ")

