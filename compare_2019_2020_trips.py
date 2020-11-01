# read in data from "get" data functions
from trip_data import get_divvy_trips_2019_q2_q3, get_divvy_trips_2020_q2_q3
from chicago_community_areas import pull_community_areas_data
from divvy_stations import get_divvy_station_data

# import modules
import pandas as pd 
import numpy as np
import time

def assemble_trips_data():
    # start time for time keeping
    start_time = time.time()

    # inititate data objects
    divvy_2019 = get_divvy_trips_2019_q2_q3()
    divvy_2020 = get_divvy_trips_2020_q2_q3()
    divvy_stations = get_divvy_station_data()

    # "pull_community_areas" grabs data from Wikipedia via pd.read_html. 
    # It pulls in two tables at once, which is I assign it to two objects
    # 1st table is each individual community area
    # 2nd table is greater chicago area
    community_area, chicago_area = pull_community_areas_data()

    # Merge comunity area with divvy_stations to get area name to merge on
    divvy_stations = pd.merge(divvy_stations, community_area, how='left', left_on='community_area', right_on=['Number[8]'])
    divvy_stations['chicago_area'] = divvy_stations['Name[8]'].apply(lambda x: chicago_area_lookup(chicago_area, x))

    # Remove divvy trips from stations outside of Chicago
    divvy_stations_chi = divvy_stations['id'].to_list()

    divvy_2019 = divvy_2019[(divvy_2019['from_station_id'].isin(divvy_stations_chi)) & (divvy_2019['to_station_id'].isin(divvy_stations_chi))]
    divvy_2020 = divvy_2020[(divvy_2020['start_station_id'].isin(divvy_stations_chi)) & (divvy_2020['end_station_id'].isin(divvy_stations_chi))]

    # Bring in community area / chicago area data from divvy_stations table
    # 2019 data
    
    divvy_2019['from_community_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['community_area'].to_numpy()[0] for x in divvy_2019['from_station_id']]
    divvy_2019['from_community_name'] = [divvy_stations.loc[divvy_stations['id'] == x]['Name[8]'].to_numpy()[0] for x in divvy_2019['from_station_id']]
    divvy_2019['from_chicago_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['chicago_area'].to_numpy()[0] for x in divvy_2019['from_station_id']]

    divvy_2019['to_community_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['community_area'].to_numpy()[0] for x in divvy_2019['to_station_id']]
    divvy_2019['to_community_name'] = [divvy_stations.loc[divvy_stations['id'] == x]['Name[8]'].to_numpy()[0] for x in divvy_2019['to_station_id']]
    divvy_2019['to_chicago_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['chicago_area'].to_numpy()[0] for x in divvy_2019['to_station_id']]

    divvy_2019.to_csv('cleaned_data/divvy_2019_trips.csv', chunksize=100000)
    print("2019 done!")

    # 2020 data
    divvy_2020['from_community_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['community_area'].to_numpy()[0] for x in divvy_2020['start_station_id']]
    divvy_2020['from_community_name'] = [divvy_stations.loc[divvy_stations['id'] == x]['Name[8]'].to_numpy()[0] for x in divvy_2020['start_station_id']]
    divvy_2020['from_chicago_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['chicago_area'].to_numpy()[0] for x in divvy_2020['start_station_id']]

    divvy_2020['to_community_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['community_area'].to_numpy()[0] for x in divvy_2020['end_station_id']]
    divvy_2020['to_community_name'] = [divvy_stations.loc[divvy_stations['id'] == x]['Name[8]'].to_numpy()[0] for x in divvy_2020['end_station_id']]
    divvy_2020['to_chicago_area'] = [divvy_stations.loc[divvy_stations['id'] == x]['chicago_area'].to_numpy()[0] for x in divvy_2020['end_station_id']]

    divvy_2020.to_csv('cleaned_data/divvy_2020_trips.csv', chunksize=100000)
    print("2020 done!")

    # print completed time
    print(assemble_trips_data.__name__, " completed in ", time.time() - start_time)

def match_chicago_area_by_station_id(station_df, station_id):
    start_time = time.time()

    community_area = station_df[station_df['id']==station_id]['community_area']
    community_name = station_df[station_df['id']==station_id]['Name[8]'] 
    chicago_area = station_df[station_df['id']==station_id]['chicago_area']

    # print completed time
    print(match_chicago_area_by_station_id.__name__, " completed in ", round(time.time() - start_time, 2))

    return community_area, community_name, chicago_area

def chicago_area_lookup(df, area_name):
    start_time = time.time()

    # find index value where community name is in list of areas
    for index, row in df.iterrows():
        if area_name in df['vteCommunity areas in Chicago.1'][index]:
            return df['vteCommunity areas in Chicago'][index]
        else:
            pass

    # print completed time
    print(chicago_area_lookup.__name__, " completed in ", time.time() - start_time)
