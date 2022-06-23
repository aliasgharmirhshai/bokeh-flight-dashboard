from matplotlib.pyplot import title
import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable
"""
Create Tab For Show Data as Table 
"""

def table_tab(data):

    d = data.groupby("name")["arr_delay"].describe()
    d["mean"] = d["mean"].round(1)
    d["std"] = d["std"].round(1)
    d = d.reset_index()

    columndata = ColumnDataSource(d)
    #Convert To Bokeh Table
    flights_tabele =  DataTable(
        source=columndata,
        columns=[
            TableColumn(field='name', title="ایرلاین"),
            TableColumn(field="count", title="تعداد پرواز"),
            TableColumn(field="mean", title="میانگین تاخیر"),
            TableColumn(field="std", title="انحراف استاندارد تاخیر"),
            TableColumn(field="min", title="کمینه تاخیر"),
            TableColumn(field="25%", title="25%"),
            TableColumn(field="50%", title="50%"),
            TableColumn(field="75%", title="75%"),
            TableColumn(field="max", title="بیشینه تاخیر")
        ],
        width = 1500
    )
    
    tab = Panel(child=flights_tabele, title="خلاصه تاخیر ها")
    return tab


 