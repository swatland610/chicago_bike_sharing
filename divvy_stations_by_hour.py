import requests
import json
import pandas as pd 

def divvy_stations_by_hour_pull():
    # bring in data from 2020-04-01 and onward
    # # there is missing data for half of 2019, so we will not bring it in
    url = "https://data.cityofchicago.org/resource/eq45-8inv.json?$limit=10000000&$where=timestamp > '2020-03-31T23:59:59.000'"
    r = requests.get(url)

    hourly_json = pd.read_json(r.text)
    divvy_stations_by_hour = pd.DataFrame(hourly_json)

    divvy_stations_by_hour.to_csv('divvy_data/divvy_stations_by_hour.csv')
