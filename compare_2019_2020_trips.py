# read in data from "get" data functions
from trip_data import get_divvy_trips_2019_q2_q3, get_divvy_trips_2020_q2_q3
from chicago_community_areas import pull_community_areas_data
from divvy_stations import get_divvy_station_data

# import modules
import pandas as pd 
import numpy as np
import geopandas as gpd 
from shapely.geometry import Polygon, Point


def enrich_trips_with_community_areas_data():
    # inititate data objects
    divvy_2019 = get_divvy_trips_2019_q2_q3()
    divvy_2020 = get_divvy_trips_2020_q2_q3()
    community_area_w_pop, community_area_groups, community_area_boundaries = pull_community_areas_data()

    # Convert trips and community area boundaries to GeoDataFrames to find points within Polygons
    divvy_2019_gpd = gpd.GeoDataFrame(community_area_boundaries, 
                    geometry=gpd.points_from_xy())

# I want to look look into trip data by what community area they start and end in.
# Defining Community Area look up function for analysis at the community area level

def community_area_lookup(point):
    # To be used with pandas.apply()

