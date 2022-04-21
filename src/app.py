import json

import numpy as np
import pandas as pd
from plotly import express as px

from constant import *

with open(
        "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/geojson-counties-fips.json",
        "r") as response:

    # 'https:/raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'

    counties = json.load(response)

df = pd.read_csv(
    "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv",
    dtype={"fips": str})
fig = px.choropleth_mapbox(df,
                           geojson=counties,
                           locations='fips',
                           color=np.log10(df["cases"]),
                           mapbox_style="open-street-map",
                           zoom=2.75,
                           center={
                               "lat": 37.0902,
                               "lon": -95.7129
                           },
                           opacity=DEFAULT_OPACITY,
                           labels={'cases': 'Cases'})

fig.update_layout(
    coloraxis_colorbar=dict(title="Cases", ticktext=[0, df["cases"].max()]))

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show()
