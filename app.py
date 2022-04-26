import json
import pathlib

import numpy as np
import pandas as pd
from dash import Dash, Input, Output, dcc, html
from plotly import express as px

from constant import *

full_df = pd.read_csv("us-counties.csv", dtype={"fips": str})

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
                html.A(html.Button("LinkdIn", className="link-button"), href=LINKDIN),
                html.A(html.Button("GitHub", className="link-button"), href=GITHUB),
                html.A(
                    html.Button("Source Code", className="link-button"), href=SOURCECODE
                ),
                html.H4(children=app_title),
                html.P(id="description", children=DESCRIPTION),
            ],
        ),
        html.Div(
            className="row",
            id="slider-container",
            style=dict(display="flex"),
            children=[
                html.Div(
                    className="six columns",
                    style=dict(width="15%"),
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
                    style=dict(width="20%"),
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
                    style=dict(width="75%"),
                    children=[
                        html.Div(
                            id="sliders",
                            children=[
                                html.P(id="slider-month-text", children="Select Month"),
                                dcc.Slider(
                                    id="months-slider",
                                    min=1,
                                    max=12,
                                    value=1,
                                    step=1,
                                    marks={
                                        month: {
                                            "label": MONTHS[month],
                                            "style": {"color": "#7fafdf"},
                                        }
                                        for month in range(1, 13)
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
def display_map(
    selected_year: int,
    selected_month: int,
    selected_radio: str,
) -> px.choropleth_mapbox:

    if selected_year == 2022 and selected_month > 4:
        selected_month = 4

    df = full_df[full_df["yearmonth"] == f"{selected_year}-{selected_month}"]

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
        hover_name="county",
        hover_data=["cases", "deaths"],
        title=TITLE(selected_radio),
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(
        hoverinfo="skip",
        coloraxis_colorbar=dict(
            title=f"{selected_year}-{selected_month}",
            ticktext=[0, data.max()],
        ),
    )

    return fig


@app.callback(Output("heatmap-title", "children"), [Input("Radio-Item", "value")])
def update_map_title(selected: str) -> str:
    return f"Heatmap of COVID 19 {selected}"


if __name__ == "__main__":
    app.run_server(debug=True)
