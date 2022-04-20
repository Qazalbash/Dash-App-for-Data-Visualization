# import os
# import pathlib

# import pandas as pd
# import plotly.express as px
# from dash import Dash, dcc, html
# from dash.dependencies import Input, Output

# from constant import *

# # Initialize app

# app = Dash(__name__,
#            meta_tags=[{
#                "name": "viewport",
#                "content": "width=device-width, initial-scale=1.0"
#            }])

# app.title = app_title
# server = app.server

# # Load data

# APP_PATH = str(pathlib.Path(__file__).parent.resolve())

# df = pd.read_csv(os.path.join(APP_PATH, "us-counties.csv"))

# columns = df.columns

# # App layout

# app.layout = html.Div(
#     id="root",
#     children=[
#         html.Div(id="header",
#                  children=[
#                      html.H4(children="Rate of US Covid Deaths"),
#                      html.P(id="description",
#                             children="Data Visualization with Python")
#                  ]),
#         html.Div(
#             id="app-container",
#             children=[
#                 html.Div(
#                     id="graph-container",
#                     children=[
#                         dcc.Dropdown(
#                             options=[{
#                                 "label": date,
#                                 "value": date
#                             } for date in columns],
#                             multi=False,
#                             placeholder='search',
#                             clearable=False,
#                             #    default="deaths",
#                             id="chart-dropdown"),
#                         dcc.Graph(id="box plot"),
#                         dcc.Graph(id="bar chart"),
#                         dcc.Graph(id="total deaths")
#                     ])
#             ])
#     ])

# deaths = {
#     county: df[df["county"] == county].describe()["deaths"]["count"]
#     for county in set(df["county"])
# }

# @app.callback(
#     Output(component_id="box plot", component_property="figure"),
#     Input(component_id="chart-dropdown", component_property="value"))
# def update_figure(selected):

#     figPie = px.box(df,
#                     y=selected,
#                     color_discrete_sequence=px.colors.sequential.RdBu)

#     return figPie

# if __name__ == "__main__":
#     app.run_server(debug=True)

from plotly import graph_objs as go
import pandas as pd
import os
import pathlib

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
# df = pd.read_csv(os.path.join(APP_PATH, "us-counties.csv"))
df = pd.read_csv(
    os.path.join(
        APP_PATH,
        # "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/data/us-county-Ziebach.csv"
        "D:/4/Data-Structure-II/CS-201-Data-Structure-II-Project/src/us-counties.csv"
    ))

# fig = go.Figure()

# fig.add_trace(
#     go.Box(y=df["cases"],
#            name="cases",
#            marker_size=2,
#            line_width=1,
#            boxpoints='all',
#            jitter=0.5,
#            whiskerwidth=0.2))
# fig.add_trace(
#     go.Box(y=df["deaths"],
#            name="deaths",
#            marker_size=2,
#            line_width=1,
#            boxpoints='all',
#            jitter=0.5,
#            whiskerwidth=0.2))

# fig.update_layout(title='Blah blah',
#                   yaxis=dict(autorange=True,
#                              showgrid=True,
#                              zeroline=True,
#                              dtick=5,
#                              gridcolor='rgb(255, 255, 255)',
#                              gridwidth=1,
#                              zerolinecolor='rgb(255, 255, 255)',
#                              zerolinewidth=2),
#                   margin=dict(l=40, r=30, b=80, t=100),
#                   paper_bgcolor='rgb(243, 243, 243)',
#                   plot_bgcolor='rgb(243, 243, 243)',
#                   showlegend=False)

# fig.show()