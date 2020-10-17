import pandas as pd

# Read in zipped trip files
trips_2019_q2 = pd.read_csv('divvy_data/Divvy_Trips_2019_Q2.csv')
trips_2019_q3 = pd.read_csv('divvy_data/Divvy_Trips_2019_Q3.csv')

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
trips_2019_q2_q3 = trips_2019_q2.append(trips_2019_q3, ignore_index=True)
