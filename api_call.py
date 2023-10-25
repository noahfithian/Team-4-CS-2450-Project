import json
import pprint
import requests
import urllib.parse

#global variables 

#base url 
base_url = 'https://api.census.gov/data/timeseries/eits/'
#parameters needed for the api call
url_params  = {
     
    "time_slot_id": "time_slot_id",
    "cell_value": "cell_value",
    "error_data": "error_data",
    "seasonally_adj": "seasonally_adj",
    "category_code": "category_code",
    "data_type_code": "data_type_code",
    "for": "for",
    "time": "2019"
}


def format_url(base_url):

        #indicator datasets interpreted as catagories 
    catagories = {
        "Construction Spending (VIP)": "vip",
        "New Residential Sales (NRS)": "ressales",
        "New Residential Construction (NRC)": "resconst",
        "Monthly Wholesale Trade Inventories": "mwts",
        "Advance Monthly Retail Sales (MARTS)": "marts",
        "Monthly Trade & Inventory Sales (MTIS)": "mtis",
        "Monthly Retail Sales (MRTS)": "mrts",
        "International Trade (FTD)": "ftd",
        "Housing Vacancies & Homeownership Rate": "hv",
        "Quarterly Financial Report (QFR)": "qfr",
        "Quarterly Summary of State and Local Taxes": "qtax"
    }

    print("List of Catagories: ")
    for key in catagories:
         print(key)
    
    selected_catagory = input("Please choose a catagory for the list above: ")

    if selected_catagory in catagories:
         key = catagories[selected_catagory]
         print(f'{base_url}{key}?get=cell_value,time_slot_id&')
    else:
         print("The key chose is not a key in the dictionary. We would suggest copying and pasting key. ")

    


    
format_url(base_url)




#send HTTPS request
def api_call(f_url): 

        try:
            response = requests.get(f_url)

            
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


