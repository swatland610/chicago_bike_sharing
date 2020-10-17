import os
import requests
import pandas as pd 
from datetime import datetime, date

def get_chicago_covid_data():
    # Set Endpoint and read data
    url = "https://data.cityofchicago.org/resource/naz8-j4nc.json"
    r = requests.get(url)

    # Convert to DF
    data = pd.read_json(r.text)

    # Drop rows where lab report date is null
    data = data[~data['lab_report_date'].isna()]

    # Convert Datetime Strings to Datetimes
    data['lab_report_date'] = data['lab_report_date'].apply(lambda x: datetime.strptime(str(x), '%Y-%m-%dT%H:%M:%S.%f').date())

    # Filter out rows outside of 04/01/2020 - 09/30/2020
    chicago_covid_data = data[(data['lab_report_date']>=date(2020,4,1)) & (data['lab_report_date']<=date(2020,9,30))]
    
    return chicago_covid_data

