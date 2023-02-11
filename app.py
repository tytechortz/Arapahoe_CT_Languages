# import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

header = html.Div("Arapahoe County", className="h2 p-2 text-white bg-primary text-center")


app.layout = dbc.Container(
    [
        header,
        # dbc.Row([dbc.Col(ct_map)]),
        # dbc.Row(dbc.Col(table, className="py-4")),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)