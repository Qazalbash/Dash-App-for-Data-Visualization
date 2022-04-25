import json
import pathlib

import numpy as np
import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly import express as px

from constant import *

app = Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

app.title = app_title
server = app.server

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.A(
                    html.Button("LinkdIn", className="link-button"),
                    href="https://www.linkedin.com/in/meesumaliqazalbash/",
                ),
                html.A(
                    html.Button("GitHub", className="link-button"),
                    href="https://github.com/MeesumAliQazalbash",
                ),
                html.A(
                    html.Button("Source Code", className="link-button"),
                    href="https://github.com/MeesumAliQazalbash/CS-201-Data-Structure-II-Project.git",
                ),
                html.H4(children="US Covid 19 Stats"),
                html.P(id="description", children="ADD description HERE"),
            ],
        ),
        html.Div(
            className="row",
            id="slider-container",
            style=dict(display="flex"),
            children=[
                html.Div(
                    className="six columns",
                    style=dict(width="50%"),
                    children=[
                        html.Div(
                            id="Radio",
                            children=[
                                html.P(id="slider-radio-text", children="Select Item"),
                                dcc.RadioItems(
                                    id="Radio-Item",
                                    options=[
                                        {"label": "Cases", "value": "cases"},
                                        {"label": "Deaths", "value": "deaths"},
                                    ],
                                    value="cases",
                                ),
                            ],
                        )
                    ],
                ),
                html.Div(
                    className="six columns",
                    style=dict(width="50%"),
                    children=[
                        html.P(id="slider-year-text", children="Select year"),
                        dcc.Slider(
                            id="years-slider",
                            min=min(YEARS),
                            max=max(YEARS),
                            value=YEARS[0],
                            step=1,
                            marks={
                                str(year): {
                                    "label": str(year),
                                    "style": {"color": "#7fafdf"},
                                }
                                for year in YEARS
                            },
                        ),
                    ],
                ),
                html.Div(
                    className="six columns",
                    style=dict(width="50%"),
                    children=[
                        html.Div(
                            id="sliders",
                            children=[
                                html.P(id="slider-month-text", children="Select Month"),
                                dcc.Slider(
                                    id="months-slider",
                                    min=min(MONTHS),
                                    max=max(MONTHS),
                                    value=MONTHS[0],
                                    step=1,
                                    marks={
                                        str(month): {
                                            "label": str(month),
                                            "style": {"color": "#7fafdf"},
                                        }
                                        for month in MONTHS
                                    },
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
        html.Div(
            id="heatmap-container",
            children=[
                html.P(id="heatmap-title"),
                dcc.Graph(
                    id="county-choropleth",
                    figure=dict(
                        layout=dict(
                            height=600,
                            display="inline-block",
                            mapbox=dict(
                                layers=[],
                                accesstoken=mapbox_access_token,
                                style=mapbox_style,
                                center=DEFAULT_CENTER,
                                zoom=DEFAULT_ZOOM,
                                pitch=0,
                            ),
                            autosize=True,
                        )
                    ),
                ),
            ],
        ),
    ],
)

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

counties = json.load(open("geojson-counties-fips.json", "r"))


@app.callback(
    Output("county-choropleth", "figure"),
    [
        Input("years-slider", "value"),
        Input("months-slider", "value"),
        Input("Radio-Item", "value"),
    ],
)
def display_map(selected_year, selected_month, selected_radio):
    if selected_year == 2022 and selected_month > 4:
        selected_month = 4

    df = pd.read_csv(f"data/{selected_year}-{selected_month}.csv", dtype={"fips": str})
    data = df[selected_radio]
    fig = px.choropleth_mapbox(
        df,
        geojson=counties,
        locations="fips",
        color=np.log10(data + 1),
        color_continuous_scale=px.colors.sequential.Mint,
        center=DEFAULT_CENTER,
        zoom=DEFAULT_ZOOM,
        mapbox_style=DEFAULT_MAPBOX_STYLE,
        opacity=DEFAULT_OPACITY,
        labels={selected_year: selected_year},
        hover_name="county",
        hover_data=["cases", "deaths"],
        # title
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(
        coloraxis_colorbar=dict(
            title=f"{selected_year}-{selected_month}",
            ticktext=[0, data.max()],
        )
    )

    return fig


@app.callback(Output("heatmap-title", "children"), [Input("years-slider", "value")])
def update_map_title(year):
    return "Heatmap of age adjusted mortality rates from poisonings in year {0}".format(
        year
    )


if __name__ == "__main__":
    app.run_server(debug=True)
