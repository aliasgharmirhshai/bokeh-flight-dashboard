from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from os.path import dirname, join
import pandas as pd
from hist import hist_tab
from table import table_tab

data = pd.read_csv(r"H:\My Life\Data\VisBokeh\example\dataset\Flights.csv", index_col=0).dropna()

tab_hist = hist_tab(data)
tab_table = table_tab(data)
tabs = Tabs(tabs=[tab_hist, tab_table])
curdoc().add_root(tabs)

