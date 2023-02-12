import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

header = html.Div("Arapahoe County", className="h2 p-2 text-white bg-primary text-center")

df = pd.read_csv('ACSDT5Y2021.C16001-2023-02-11T183920.csv')
df.drop(df.columns[[1,2]], axis=1, inplace=True)
df.drop(df.iloc[:,2::2], axis=1, inplace=True)


gdf = gpd.read_file('/Users/jamesswank/Python_projects/covid_heatmap/Census_Tracts_2020_SHAPE_WGS/Census_Tracts_2020_WGS.shp')
gdf = gdf.to_crs("epsg:4326")
gdf = gdf.set_geometry('geometry')

gdf = gdf.drop(gdf.columns[[1,3,4,5,6,7,8,9,10,11,12,13,14,15]], axis=1)
# print(gdf['TRACTCE20'])
tracts = gdf['TRACTCE20'].tolist()
tracts.insert(0,'Label')
print(tracts)

df.columns = tracts
# print(df)

columnDefs = [
    {
        'headerName': 'Label',
        'field': 'Label'
    }
]

defaultColDef = {
    "filter": True,
    "resizable": True,
    "sortable": True,
    "editable": False,
    "floatingFilter": True,
    "minWidth": 125
}

table = dag.AgGrid(
    id='ct-grid',
    className="ag-theme-alpine-dark",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    defaultColDef=defaultColDef,
    # cellStyle=cellStyle,
    # dangerously_allow_code=True,
    dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single"},
)




app.layout = dbc.Container(
    [
        header,
        # dbc.Row([dbc.Col('ct-grid')]),
        dbc.Row(dbc.Col(table, className="py-4")),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8060)