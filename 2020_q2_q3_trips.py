import pandas as pd

# Read in zipped trip files
trips_2020_04 = pd.read_csv('divvy_data/202004-divvy-tripdata.csv')
trips_2020_05 = pd.read_csv('divvy_data/202005-divvy-tripdata.csv')
trips_2020_06 = pd.read_csv('divvy_data/202006-divvy-tripdata.csv')
trips_2020_07 = pd.read_csv('divvy_data/202007-divvy-tripdata.csv')
trips_2020_08 = pd.read_csv('divvy_data/202008-divvy-tripdata.csv')
trips_2020_09 = pd.read_csv('divvy_data/202009-divvy-tripdata.csv')

append_list = [trips_2020_05, trips_2020_06, trips_2020_07, trips_2020_08, trips_2020_09]

# append dfs
trips_2020_q2_q3 = trips_2020_04.append(append_list, ignore_index=True)