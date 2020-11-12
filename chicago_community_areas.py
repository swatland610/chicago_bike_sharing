import requests
import pandas as pd 
import time
pd.set_option('display.max_rows',100)

def pull_community_areas_data():
    # start time for time keeping
    start_time = time.time()

    # Grab 2017 community areas and population data
    url = "https://en.wikipedia.org/wiki/Community_areas_in_Chicago"
    html_tables = pd.read_html(url)

    # Establish DF of community areas with population
    community_area_w_pop = pd.DataFrame(html_tables[0])[:-1]

    # DF of Community Area Groups
    community_area_groups = pd.DataFrame(html_tables[1])

    # fix formatting of community area number
    community_area_w_pop['Number[8]'] = community_area_w_pop['Number[8]'].apply(lambda x: int(x))

    # Fix formatting of "(The) Loop[11]"
    community_area_w_pop['Name[8]'][31] = "Loop"

    # print completed time
    print(pull_community_areas_data.__name__, " completed in ", time.time() - start_time)

    return community_area_w_pop, community_area_groups



    

