from random import random
from bokeh.layouts import column
from bokeh.models import Button, Select
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
import display_data
import api_call
import numpy
import matplotlib
import datetime
from bokeh.models import Dropdown


# #creating a plot
# p = figure(x_range = (0, 100), y_range = (0,100), toolbar_location = None)
# p.border_fill_color = 'black'
# p.border_fill_color = 'white'
# p.outline_line_color = None
# p.grid.grid_line_color = None

# # add text renderer to plot
# r = p.text(x=[], y = [], text=[], text_color=[], text_font_size = "26px", text_baseline="middle", text_align="center")
# i = 0
# ds = r.data_source

# making the variables to use in the call
choice = ""
year_start = 2000
year_end = year_start + 1
category = ''
data_type = ''
quarter = ''
state = 'All'

#state update
def update_state(_, __, new):  # _ is for linter to ignore the variables att, old /dont complain
    global choice
    choice = new
    print(choice) #checking for updated state

state_menu = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi"]
state_dropdown = Select(title='Select a state', options=state_menu)
state_dropdown.on_change('value', update_state)

#year update 
def update_years(_, __, new):
    global year_start
    #global year_end
    year_start = new
    #year_end = new+1 // a string so cant add 1, REWORK 
    #print(year_end)
    print(year_start)
year_menu = ["1992", "1993", "1994", "1995", "1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009", "2010"]
year_dropdown = Select(title ='Select a year', options = year_menu)
year_dropdown.on_change('value',update_years)

curdoc().add_root(column(state_dropdown, year_dropdown))

# Calls Api and gets data
# def callback():
#     link = format_url_constraints(choice, year_start, year_end, quarter, data_type, category, state)
#     data = api_call.api_call(link)
#     for d in data:
#         cell_value = d[0]
#         state_name = d[1]
#         time = d[6]

# button = Button(label="Submit")
# button.on_event('button_click', callback)
