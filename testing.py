import requests
import display_data as dd
import csv 

state_dict = {
        "All": '*',
        "Alabama": '01',
        "Alaska": '02',
        "Arizona": '04',
        "Arkansas": '05',
        "California": '06',
        "Colorado": '08',
        "Connecticut":'09',
        "Delaware": 10,
        "Florida": 12,
        "Georgia": 13,
        "Hawaii": 15,
        "Idaho": 16,
        "Illinois": 17,
        "Indiana": 18,
        "Iowa": 19,
        "Kansas": 20,
        "Kentucky": 21,
        "Louisiana": 22,
        "Maine": 23,
        "Maryland": 24,
        "Massachusetts": 25,
        "Michigan": 26,
        "Minnesota": 27,
        "Mississippi": 28,
        "Missouri": 29,
        "Montana": 30,
        "Nebraska": 31,
        "Nevada": 32,
        "New Hampshire": 33,
        "New Jersey": 34,
        "New Mexico": 35,
        "New York": 36,
        "North Carolina": 37,
        "North Dakota": 38,
        "Ohio": 39,
        "Oklahoma": 40,
        "Oregon": 41,
        "Pennsylvania": 42,
        "Rhode Island": 44,
        "South Carolina": 45,
        "South Dakota": 46,
        "Tennessee": 47,
        "Texas": 48,
        "Utah": 49,
        "Vermont": 50,
        "Virginia": 51,
        "Washington": 53,
        "West Virginia": 54,
        "Wisconsin": 55,
        "Wyoming": 56
    }

            #indicator datasets interpreted as catagories 
catagories_code = {
"QTAXCAT1": "Table 1 - Latest National Totals of State and Local Tax Revenue",
"QTAXCAT2": "Table 2 - Latest National Totals of State Tax Revenue",
"QTAXCAT3": "Table 3 - Latest State Tax Collections by State and Type of Tax"
}
    #specific data type all in millions of dollars        
data_types={
    "TO1": "TO1 Property Taxes",
    "TO14QE": "TO1 Property Taxes, 4 Quarters Ending",
    "TO9": "TO9 General Sales and Gross Receipts Taxes",
    "TO94QE": "TO9 General Sales and Gross Receipts Taxes, ⅐ Quarters Ending",
    "T10": "T10 Alcoholic Beverages Sales Tax",
    "T1040E": "T10 Alcoholic Beverages Sales Tax, 4 Quarters Ending",
    "T11": "TI1 Amusements Sales Tax",
    "T12": "T12 Insurance Premiums Sales Tax",
    "T13": "TI3 Motor Fuels Sales Tax",
    "T134QE": "TI3 Motor Fuels Sales Tax, # Quarters Ending",
    "T14": "T14 Pari-Mutuels Sales Tax",
    "T15": "TIS Public Utilities Sales Tax",
    "T16": "T16 Tobacco Products Sales Tax",
    "T164QE": "T16 Tobacco Products Sales Tax, 4 Quarters Ending",
    "T19": "T19 Other Selective Sales and Gross Receipts Taxes",
    "T20": "T20 Alcoholic Beverages License"
    }
    
    #choose specific quarter if wanted
quarter_dict = {
    "Quarter 1": "Q1",
    "Quarter 2": "Q2",
    "Quarter 3": "Q3",
    "Quarter 4": "Q4"
}
years = [1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

choice = "state"
# time = t
# end_time = t2
# quarter = q
# data_type_code = d
# catagory_code = c
# state = s

# dd.format_url_constraints(choice, time, end_time, quarter, data_type_code, category_code, state)
with open("test_results.csv", "w", newline="") as csvwriter:
    results = csv.writer(csvwriter, delimiter=" ")
    results.writerow(["State","Category","Data_Type","Quarter","Year"])

    for year in years:
        for state_key, state_value in state_dict.items():
            for category_key, category_value in catagories_code.items():
                for data_type_key, data_type_value in data_types.items():
                    for quarter_key, quarter_value in quarter_dict.items():
                        # print(f"State: {state_key}, Category: {category_key}, Data Type: {data_type_key}, Quarter: {quarter_key}")
                        url = dd.format_url_constraints(choice, year, year, quarter_key, data_type_key, category_key, state_key)
                        request = requests.get(url)
                        if request.status_code != 200:
                            results.writerow([state_key, category_key, data_type_key, quarter_key, year])
                        else:
                            continue
