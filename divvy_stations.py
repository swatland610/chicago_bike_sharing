import requests
import time
import pandas as pd
import rtree
import geopandas as gpd
from shapely.geometry import Point, Polygon
from shapely import wkt

def get_divvy_station_data():
    # start time for time keeping
    start_time = time.time()

    # request divvy station data
    url = "https://data.cityofchicago.org/resource/bbyy-e7gq.json"
    r = requests.get(url)

    divvy_stations_json = pd.read_json(r.text)
    divvy_stations = pd.DataFrame(divvy_stations_json)
    # Convert to GeoDataFrame to correct community areas
    divvy_stations = gpd.GeoDataFrame(divvy_stations, geometry=gpd.points_from_xy(divvy_stations.longitude, divvy_stations.latitude))

    # Fix :computed_region column names
    divvy_stations.rename(columns={':@computed_region_vrxf_vc4k':'old_community_area'}, inplace=True)

    # Drop stations outside of the city as there is no community area number
    divvy_stations = divvy_stations[~divvy_stations['old_community_area'].isna()]

    # Bring in Chicago Shapefiles for Community Area Comparison
    chicago = grab_community_area_shapefiles()

    # Fix Community Area
    divvy_stations['community_area'] = divvy_stations['geometry'].apply(lambda x: find_polygon(chicago, x))

    # print completed time
    print(get_divvy_station_data.__name__, " completed in ", time.time() - start_time)

    return divvy_stations

def grab_community_area_shapefiles():
    chicago = gpd.read_file("divvy_data/Boundaries - Community Areas", crs = {'init': 'epsg:4326'})
    return chicago

def find_polygon(gdf, coordinate):
    dex = gdf[gdf['geometry'].contains(coordinate)].index.values[0]
    return gdf['area_num_1'][dex]
