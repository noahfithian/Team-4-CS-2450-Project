import json
import pprint
import requests


url = 'https://api.census.gov/data/timeseries/eits/qss?get=cell_value,time_slot_id,seasonally_adj&data_type_code&category_code&time=2017'

try:
    response = requests.get(url)

    
    if response.status_code == 200:
       
        data = response.json()  
        pprint.pprint(data)
    else:
        # If the request was not successful, handle the error
        print(f"Request failed with status code: {response.status_code}")
        

except requests.exceptions.RequestException as e:
   
    print(f"Request error: {e}")

except Exception as e:
    
    print(f"An error occurred: {e}")