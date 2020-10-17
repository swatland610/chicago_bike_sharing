import pandas as pd 
from datetime import datetime, date

def get_divvy_trips_2019_q2_q3():
    # Read in csv trip files
    trips_2019_q2 = pd.read_csv('divvy_data/Divvy_Trips_2019_Q2.csv')
    trips_2019_q3 = pd.read_csv('divvy_data/Divvy_Trips_2019_Q3.csv')

    # Column Labels are different between data sets. 
    # Align Column Names
    columns = {}
    position = 0

    # loop to match key-value pairs for rename
    for i in trips_2019_q2.columns:
        # find value for key-value pair
        matching_col = trips_2019_q3.columns[position]
        # create key-value pair
        columns[i] = matching_col
        # update position for next column
        position = position + 1

    # update column names in trips_2019_q2
    trips_2019_q2.rename(columns=columns, inplace=True)
    # append dfs
    data = trips_2019_q2.append(trips_2019_q3, ignore_index=True)

    # convert datetime strings to dates
    data['start_time'] = data['start_time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())
    data['end_time'] = data['end_time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())

    return data

def get_divvy_trips_2020_q2_q3():
    # Read in csv trip files
    trips_2020_04 = pd.read_csv('divvy_data/202004-divvy-tripdata.csv')
    trips_2020_05 = pd.read_csv('divvy_data/202005-divvy-tripdata.csv')
    trips_2020_06 = pd.read_csv('divvy_data/202006-divvy-tripdata.csv')
    trips_2020_07 = pd.read_csv('divvy_data/202007-divvy-tripdata.csv')
    trips_2020_08 = pd.read_csv('divvy_data/202008-divvy-tripdata.csv')
    trips_2020_09 = pd.read_csv('divvy_data/202009-divvy-tripdata.csv')

    append_list = [trips_2020_05, trips_2020_06, trips_2020_07, trips_2020_08, trips_2020_09]

    # append dfs
    data = trips_2020_04.append(append_list, ignore_index=True)

    # Fix datetime strings to dates
    data['started_at'] = data['started_at'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())
    data['ended_at'] = data['ended_at'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())
    
    return data
