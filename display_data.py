import numpy
import api_call
import datetime
#sales data is in millions of dollars

def getData():


    print("Hello world")
    # format_url_constraints('us', 2022, 'Quarter 1', 't01', 'QTAXCAT1', 'Utah')


#
# def format_url_constraints(ch, t, q, d, c, s):
#     choice = ch
#     time = t
#     quarter = q
#     data_type_code = d
#     catagory_code = c
#     state = s
#
#
#     base_url = 'https://api.census.gov/data/timeseries/eits/qtax?get='
#     base_url_us = 'https://api.census.gov/data/timeseries/eits/qtax?get=NAME,DATA_TYPE_CODE,SEASONALLY_ADJ,CATEGORY_CODE,TIME_SLOT_DATE,CELL_VALUE,ERROR_DATA&for=us:*&time=2012-Q3'
#     base_url_all_states = 'https://api.census.gov/data/timeseries/eits/qtax?get=NAME,DATA_TYPE_CODE,SEASONALLY_ADJ,CATEGORY_CODE,TIME_SLOT_DATE,CELL_VALUE,ERROR_DATA&for=state:*&time=2012-Q3'
#
#     # Define a dictionary with the state/territory names as keys and their corresponding numbers as values
#     state_dict = {
#         "All": '*',
#         "Alabama": '01',
#         "Alaska": '02',
#         "Arizona": '04',
#         "Arkansas": '05',
#         "California": '06',
#         "Colorado": '08',
#         "Connecticut": '09',
#         "Delaware": 10,
#         "Florida": 12,
#         "Georgia": 13,
#         "Hawaii": 15,
#         "Idaho": 16,
#         "Illinois": 17,
#         "Indiana": 18,
#         "Iowa": 19,
#         "Kansas": 20,
#         "Kentucky": 21,
#         "Louisiana": 22,
#         "Maine": 23,
#         "Maryland": 24,
#         "Massachusetts": 25,
#         "Michigan": 26,
#         "Minnesota": 27,
#         "Mississippi": 28,
#         "Missouri": 29,
#         "Montana": 30,
#         "Nebraska": 31,
#         "Nevada": 32,
#         "New Hampshire": 33,
#         "New Jersey": 34,
#         "New Mexico": 35,
#         "New York": 36,
#         "North Carolina": 37,
#         "North Dakota": 38,
#         "Ohio": 39,
#         "Oklahoma": 40,
#         "Oregon": 41,
#         "Pennsylvania": 42,
#         "Rhode Island": 44,
#         "South Carolina": 45,
#         "South Dakota": 46,
#         "Tennessee": 47,
#         "Texas": 48,
#         "Utah": 49,
#         "Vermont": 50,
#         "Virginia": 51,
#         "Washington": 53,
#         "West Virginia": 54,
#         "Wisconsin": 55,
#         "Wyoming": 56
#     }
#
#     # indicator datasets interpreted as catagories
#     catagories_code = {
#         "QTAXCAT1": "Table 1 - Latest National Totals of State and Local Tax Revenue",
#         "QTAXCAT2": "Table 2 - Latest National Totals of State Tax Revenue",
#         "QTAXCAT3": "Table 3 - Latest State Tax Collections by State and Type of Tax"
#     }
#     # specific data type all in millions of dollars
#     data_types = {
#         "TO1": "TO1 Property Taxes",
#         "TO14QE": "TO1 Property Taxes, 4 Quarters Ending",
#         "TO9": "TO9 General Sales and Gross Receipts Taxes",
#         "TO94QE": "TO9 General Sales and Gross Receipts Taxes, ⅐ Quarters Ending",
#         "T10": "T10 Alcoholic Beverages Sales Tax",
#         "T1040E": "T10 Alcoholic Beverages Sales Tax, 4 Quarters Ending",
#         "T11": "TI1 Amusements Sales Tax",
#         "T12": "T12 Insurance Premiums Sales Tax",
#         "T13": "TI3 Motor Fuels Sales Tax",
#         "T134QE": "TI3 Motor Fuels Sales Tax, # Quarters Ending",
#         "T14": "T14 Pari-Mutuels Sales Tax",
#         "T15": "TIS Public Utilities Sales Tax",
#         "T16": "T16 Tobacco Products Sales Tax",
#         "T164QE": "T16 Tobacco Products Sales Tax, 4 Quarters Ending",
#         "T19": "T19 Other Selective Sales and Gross Receipts Taxes",
#         "T20": "T20 Alcoholic Beverages License"
#     }
#
#     # choose specific quarter if wanted
#     quarter_dict = {
#         "Quarter 1": "Q1",
#         "Quarter 2": "Q2",
#         "Quarter 3": "Q3",
#         "Quarter 4": "Q4"
#     }
#
#     try:
#
#         # time = int(2023)  # HARDCODED
#         current_year = datetime.datetime.now().year
#
#         if current_year >= time > 1992:
#             print("Valid year entered:", time)
#         else:
#             raise ValueError("Year must be greater than 1992 and less than or equal to the current year ", current_year, ".")
#
#     except ValueError as e:
#
#         print("Error:", e)
#
#     except Exception as e:
#
#         print("An unexpected error occurred:", e)
#
#     if choice == "state":
#
#         if state not in state_dict:
#             print("Invalid state name")
#         else:
#
#             if data_type_code not in data_types:
#                 print("Invalid data type code.")
#             else:
#                 if quarter not in quarter_dict:
#                     print("Invalid quarter.")
#                 else:
#                     # Construct the URL
#                     formated_us = f'https://api.census.gov/data/timeseries/eits/qtax?get=NAME,SEASONALLY_ADJ,TIME_SLOT_DATE,CELL_VALUE,ERROR_DATA,CATEGORY_CODE&=DATA_TYPE_CODE={data_type_code}&for=state:{state_dict[state]}&time={time}-{quarter_dict[quarter]}'
#                     print(formated_us)
#                     print(
#                         f"You chose to see the entire {state_dict[state]} state data with category code {catagory_code}, data type code {data_type_code}, and quarter {quarter_dict[quarter]}.")
#
#                     api_call(formated_us)
#
#
#
#     elif choice == "us":
#         # Choose a category code
#         if catagory_code not in catagories_code:
#             print("Invalid category code.")
#         else:
#             # Choose a data type code
#             if data_type_code not in data_types:
#                 print("Invalid data type code.")
#             else:
#                 # Choose a quarter
#                 if quarter not in quarter_dict:
#                     print("Invalid quarter.")
#                 else:
#                     # Construct the URL
#                     formated_us = f'https://api.census.gov/data/timeseries/eits/qtax?get=NAME,SEASONALLY_ADJ,TIME_SLOT_DATE,CELL_VALUE,ERROR_DATA&=CATEGORY_CODE={catagory_code}&=DATA_TYPE_CODE={data_type_code}&for=us:*&time={time}-{quarter_dict[quarter]}'
#                     print(formated_us)
#                     print(
#                         "You chose to see the entire U.S. data with category code {catagory_code}, data type code {data_type_code}, and quarter {quarter_dict[quarter]}.")
#
#                     api_call(formated_us)
#
# # getData()
