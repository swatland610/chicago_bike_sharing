import requests
import pandas as pd 
import geopandas as gpd 




def pull_community_areas_data():
    # Grab 2017 community areas and population data
    url = "https://en.wikipedia.org/wiki/Community_areas_in_Chicago"
    html_tables = pd.read_html(url)

    # Grab Community Areas GeoData to access community area locations of starting and end trips
    url = "https://data.cityofchicago.org/resource/igwz-8jzy.json"
    r = requests.get(url)
    community_area_boundaries = pd.DataFrame(pd.read_json(r.text))

    # Establish DF of community areas with population
    community_area_w_pop = pd.DataFrame(html_tables[0])
    # DF of Community Area Groups
    community_area_groups = pd.DataFrame(html_tables[1])

    return community_area_w_pop, community_area_groups, community_area_boundaries



    

