from random import random
from bokeh.layouts import column # Create Bokeh Layer and Set Structure app
from bokeh.models import Button #  app button
from bokeh.palettes import RdYlBu3 # Color Palettes (Get Bokeh Site)
from bokeh.plotting import figure, curdoc # Create Plot 

p = figure(x_range=(0, 100), y_range=(0, 100)) # Create Bokeh Plot 
result = p.text(x=[], y=[], text=[], text_color=[]) # Text For Axes Plot And Text Color 
dataSource = result.data_source

button = Button(label="ثبت") # Create Button
i = 0

def clickOnSubmit():
    global i # Find i in Out Function
    new_data = {}
    new_data["x"] = dataSource.data["x"] + [random() * 70 + 15] # Get X Axies Plot With Random
    new_data["y"] = dataSource.data["y"] + [random() * 70 + 15] # Get X Axies Plot With Random
    new_data["text_color"] = dataSource.data["text_color"] + [RdYlBu3[i%3]] # Define Text Color 
    new_data["text"] = dataSource.data["text"] + [str(random())]
    print(new_data)
    print("i: " + str(i))
    dataSource.data = new_data
    i = i + i

button.on_click(clickOnSubmit) # Define Event For Button

curdoc().add_root(column(button, p))

