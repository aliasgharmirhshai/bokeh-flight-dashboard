from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from os.path import dirname, join
import pandas as pd
from hist import hist_tab


data = pd.read_csv("H:\My Life\Data\VisBokeh\example\dataset\Flights.csv", index_col=0).dropna()

hist_tab(data)