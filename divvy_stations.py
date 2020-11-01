import requests
import time
import pandas as pd

def get_divvy_station_data():
    # start time for time keeping
    start_time = time.time()

    # request divvy station data
    url = "https://data.cityofchicago.org/resource/bbyy-e7gq.json"
    r = requests.get(url)

    divvy_stations_json = pd.read_json(r.text)
    divvy_stations = pd.DataFrame(divvy_stations_json)

    # Fix :computed_region column names
    divvy_stations.rename(columns={':@computed_region_vrxf_vc4k':'community_area'}, inplace=True)

    # Drop stations outside of the city as there is no community area number
    divvy_stations = divvy_stations[~divvy_stations['community_area'].isna()]

    # print completed time
    print(get_divvy_station_data.__name__, " completed in ", time.time() - start_time)

    return divvy_stations
