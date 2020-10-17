import requests
import pandas as pd 




def pull_community_areas_data():
    # Grab 2017 community areas and population data
    url = "https://en.wikipedia.org/wiki/Community_areas_in_Chicago"
    html_tables = pd.read_html(url)

    # Establish DF of community areas with population
    community_area_w_pop = pd.DataFrame(html_tables[0])
    # DF of Community Area Groups
    community_area_groups = pd.DataFrame(html_tables[1])

    return community_area_w_pop, community_area_groups



    

