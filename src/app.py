import json
from turtle import width

import numpy as np
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from plotly import express as px

from constant import *

app = Dash(__name__,
           meta_tags=[{
               "name": "viewport",
               "content": "width=device-width, initial-scale=1.0"
           }])

mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.A(
                    html.Img(id="logo",
                             src=app.get_asset_url("dash-logo.png")),
                    href="https://plotly.com/dash/",
                ),
                html.A(
                    html.Button("Enterprise Demo", className="link-button"),
                    href="https://plotly.com/get-demo/",
                ),
                html.A(
                    html.Button("Source Code", className="link-button"),
                    href=
                    "https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-opioid-epidemic",
                ),
                html.H4(children="Rate of US Poison-Induced Deaths"),
                html.P(
                    id="description",
                    children=
                    "Deaths are classified using the International Classification of Diseases, \
                    Tenth Revision (ICD–10). Drug-poisoning deaths are defined as having ICD–10 underlying \
                    cause-of-death codes X40–X44 (unintentional), X60–X64 (suicide), X85 (homicide), or Y10–Y14 \
                    (undetermined intent).",
                ),
            ],
        ),
        html.Div(
            id="body",
            children=[
                html.Div(id="left column",
                         children=[
                             html.P("Heat map of Cases of Covid 19"),
                             dcc.Graph(
                                 id="heat map",
                                 figure=dict(layout=dict(mapbox=dict(
                                     layers=[],
                                     accesstoken=mapbox_access_token,
                                     style=mapbox_style,
                                     center=dict(lat=38.72490, lon=-95.61446),
                                     zoom=DEFAULT_ZOOM,
                                     pitch=0),
                                                         autosize=True))),
                             dcc.RadioItems(id="selector",
                                            options=[{
                                                "label": "Cases",
                                                "value": "cases"
                                            }, {
                                                "label": "Deaths",
                                                "value": "deaths"
                                            }],
                                            value="cases")
                         ]),
                html.Div(
                    id="right column",
                    children=[
                        html.Div(html.P("Here right columns")),
                        dcc.Graph(
                            id="Some bar",
                            figure=dict(
                                # data=[dict(x=0, y=0)],
                                layout=dict(paper_bgcolor="#F4F4F8",
                                            plot_bgcolor="#F4F4F8",
                                            autofill=True,
                                            margin=dict(
                                                t=75, r=50, b=100, l=50))))
                    ])
            ])
    ])

counties = json.load(
    open(
        "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/geojson-counties-fips.json",
        "r"))

# 'https:/raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json'

df = pd.read_csv(
    "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-state-death-cases-summary.csv",
    dtype={"fips": str})


@app.callback(Output(component_id="heat map", component_property="figure"),
              Input(component_id="selector", component_property="value"))
def map_gen(field: str) -> None:
    fig = px.choropleth_mapbox(df,
                               geojson=counties,
                               locations='fips',
                               color=np.log10(df[field] + 1),
                               center=dict(lat=38.72490, lon=-95.61446),
                               zoom=DEFAULT_ZOOM,
                               mapbox_style="open-street-map",
                               opacity=DEFAULT_OPACITY,
                               labels={field: field})

    fig.update_layout(coloraxis_colorbar=dict(title=field.upper(),
                                              ticktext=[0, df[field].max()]))

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

# map_gen("cases")
# map_gen("deaths")
