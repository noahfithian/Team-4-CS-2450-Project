
#global variables 

#catagory place holder
catagory = ""
#base url 
url = 'https://api.census.gov/data/timeseries/eits/'+catagory+"?get=cell_value,time_slot_id&"
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
