# read in data from "get" data functions
from trip_data import get_divvy_trips_2019_q2_q3, get_divvy_trips_2020_q2_q3

# import modules
import pandas as pd 
import numpy as np

# get data
divvy_2019 = get_divvy_trips_2019_q2_q3()
divvy_2020 = get_divvy_trips_2020_q2_q3()

