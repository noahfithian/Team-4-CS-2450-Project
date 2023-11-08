from bokeh.layouts import column
from bokeh.models import Button, Select, ColumnDataSource, DataTable, DateFormatter, TableColumn
from bokeh.io import show
from bokeh.plotting import figure, curdoc
import display_data
import api_call

from bokeh.models import TableColumn, DataTable, ColumnDataSource

#adding key for codes 
keyData = dict(
    code=["For Categoty", "QTAXCAT1", "QTAXCAT2", "QTAXCAT3", "For Data Types ","TO1", "TO14QE", "T09", "TO94QE","T10","T1040E", "T11", "T12", "T13", "T134QE", "T14", "T15", "T16", "T164QE", "T19", "T20"],
    meaning=[" ", "National Totals of State and Local Tax Revenue", "National Totals of State Tax Revenue", "Tax Collections by State and Type of Tax"," ", "Property Taxes", "Property Taxes, 4 Quarters Ending", " General Sales and Gross Receipts Taxes", "General Sales and Gross Receipts Taxes, ⅐ Quarters Ending","Alcoholic Beverages Sales Tax" , "Alcoholic Beverages Sales Tax, 4 Quarters Ending", "Amusements Sales Tax","Insurance Premiums Salex tax", "Motor fuel sales tax", "Motor Fuels Sales Tax, # Quarters Ending","Pari-Mutuels Sales Tax", "Public Utilities Sales Tax", "Tobacco Products Sales Tax", "Tobacco Products Sales Tax, 4 Quarters Ending","Other Selective Sales and Gross Receipts Taxes", "Alcoholic Beverages License"]
)

columns = [
    TableColumn(field="code", title="Code"),
    TableColumn(field="meaning", title="Meaning")
]

keyDataTable = DataTable(source=ColumnDataSource(keyData), columns=columns, width=600, height=280)

# Initialize variables
choice = ""
year = 2000
data_type = ""
category = ""
state = 'All'
values_list = [0, 0, 0, 0]  # Default values list
data = {'x-values': ['Quarter One', 'Quarter 2', 'Quarter 3', 'Quarter 4'], 'y-values': values_list}
source = ColumnDataSource(data=data)

# State update
def update_state(attr, old, new):
    global choice
    choice = new
    print(choice)  # Checking for updated state

state_menu = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
state_dropdown = Select(title='Select a state', options=state_menu)
state_dropdown.on_change('value', update_state)

# Year update
def update_years(attr, old, new):
    global year
    year = int(new)
    print(year)

year_menu = [str(year) for year in range(1992, 2024)]  # Updated to generate a range of years
year_dropdown = Select(title='Select a year', options=year_menu)
year_dropdown.on_change('value', update_years)

# Update data type
def update_dataTypes(attr, old, new):
    global data_type
    data_type = new
    print(data_type)

dataType_menu = ["TQ1", "TO14QE", "TO9", "TO94QE", "T10", "T1040E", "T11", "T12", "T13", "T134QE", "T14", "T15", "T16", "T164QE", "T19", "T20"]
dataType_dropdown = Select(title="Select datatype", options=dataType_menu)
dataType_dropdown.on_change('value', update_dataTypes)

# Update category
def update_category(attr, old, new):
    global category
    category = new
    print(category)

category_menu = ["QTAXCAT1", "QTAXCAT2", "QTAXCAT3"]
category_dropdown = Select(title="Category", options=category_menu)
category_dropdown.on_change('value', update_category)

# Update Quarter didn't use this because displays all quarters 
# def update_quarter(attr, old, new):
#     global quarter
#     quarter = new
#     print(quarter)

# quarter_menu = ["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"]
# quarter_dropdown = Select(title="Select Quarter", options=quarter_menu)
# quarter_dropdown.on_change('value', update_quarter)

# Callback function
def callback():
    link = display_data.format_url_constraints('state', year, year, "Quarter 1", data_type, category, choice)
    data = api_call.api_call(link)
    
    fetched_values = []
    for d in data:
        cell_value = d[0]
        state_name = d[1]
        time = d[6]
        if cell_value != 'CELL_VALUE':
            fetched_values.append(int(cell_value) / 1_000)
    
    # Fill values_list with fetched values and pad with zeros if fewer than 4
    values_list = [0, 0, 0, 0]
    for i, value in enumerate(fetched_values):
        values_list[i] = value
    
    source.data = {'x-values': ['Quarter One', 'Quarter 2', 'Quarter 3', 'Quarter 4'], 'y-values': values_list}
    print(values_list)

# Button setup
button = Button(label="Submit")
button.on_click(callback)

# Plot setup
plot = figure(x_range=['Quarter One', 'Quarter 2', 'Quarter 3', 'Quarter 4'], title="In Millions of dollars", toolbar_location=None, tools="")
plot.vbar(x='x-values', top='y-values', width=0.5, color="green", source=source)

# Add the plot and widgets to the document
curdoc().add_root(column(state_dropdown, year_dropdown, dataType_dropdown, category_dropdown, keyDataTable, button, plot))
