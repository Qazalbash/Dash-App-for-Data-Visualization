import json
import pathlib
import re

import numpy as np
import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly import express as px

from constant import *

app = Dash(__name__,
           meta_tags=[{
               "name": "viewport",
               "content": "width=device-width, initial-scale=1.0"
           }])
app.title = app_title
server = app.server

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.A(html.Button("LinkdIn", className="link-button"),
                       href="https://www.linkedin.com/in/meesumaliqazalbash/"),
                html.A(html.Button("GitHub", className="link-button"),
                       href="https://github.com/MeesumAliQazalbash"),
                html.
                A(html.Button("Source Code", className="link-button"),
                  href=
                  "https://github.com/MeesumAliQazalbash/CS-201-Data-Structure-II-Project.git"
                  ),
                html.H4(children="US Covid 19 Stats"),
                html.P(id="description", children="ADD description HERE")
            ]),
        html.Div(id="slider-container",
                 children=[
                     html.P(id="slider-text", children="Heat map of Covid 19"),
                     dcc.RadioItems(id="Radio-Item",
                                    options=[{
                                        "label": "Cases",
                                        "value": "cases"
                                    }, {
                                        "label": "Deaths",
                                        "value": "deaths"
                                    }],
                                    value="cases")
                 ]),
        html.Div(id="heatmap-container",
                 children=[
                     html.P(id="heatmap-title"),
                     dcc.Graph(id="county-choropleth",
                               figure=dict(layout=dict(
                                   mapbox=dict(layers=[],
                                               accesstoken=mapbox_access_token,
                                               style=mapbox_style,
                                               center=DEFAULT_CENTER,
                                               zoom=DEFAULT_ZOOM,
                                               pitch=0),
                                   autosize=True,
                               )))
                 ])
    ])

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

counties = json.load(
    open(
        "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/geojson-counties-fips.json",
        "r"))

# https:/raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json

df = pd.read_csv(
    "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv",
    dtype={"fips": str})

regex_pat = re.compile(r"Unreliable", flags=re.IGNORECASE)
df["deaths"] = df["deaths"].replace(regex_pat, 0)
df["cases"] = df["cases"].replace(regex_pat, 0)


@app.callback(Output("county-choropleth", "figure"),
              [Input("Radio-Item", "value")])
def display_map(RadioValue):

    fig = px.choropleth_mapbox(
        df,
        geojson=counties,
        locations='fips',
        color=np.log10(df[RadioValue] + 1),
        color_continuous_scale=px.colors.sequential.Mint,
        center=DEFAULT_CENTER,
        zoom=DEFAULT_ZOOM,
        mapbox_style=DEFAULT_MAPBOX_STYLE,
        opacity=DEFAULT_OPACITY,
        labels={RadioValue: RadioValue})

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(coloraxis_colorbar=dict(
        title=RadioValue.upper(), ticktext=[0, df[RadioValue].max()]))

    return fig


@app.callback(Output("heatmap-title", "children"),
              [Input("Radio-Item", "value")])
def update_map_title(year):
    return "Heatmap of age adjusted mortality rates from poisonings in year {0}".format(
        year)


if __name__ == '__main__':
    app.run_server(debug=True)
