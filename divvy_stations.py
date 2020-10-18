import requests
import pandas as pd

def get_divvy_station_data():   
    # request divvy station data
    url = "https://data.cityofchicago.org/resource/bk89-9dk7.json"
    r = requests.get(url)

    divvy_stations_json = pd.read_json(r.text)
    divvy_stations = pd.DataFrame(divvy_stations_json)

    return divvy_stations