import os

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing pickle df)
filename = 'join_sources_df.pkl'
path = os.path.join('..', '..', 'data', 'processed', filename)
df = pd.read_pickle(path)
df.reset_index(inplace = True)
df.fillna(0)
dropdown_options = [{"label": col, "value": col} for col in df.columns]

print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_var1",
                 options=dropdown_options,
                 multi=False,
                 value="Ingresos",
                 style={'width': "40%"}
                 ),
    
    dcc.Dropdown(id="slct_var2",
                 options=dropdown_options,
                 multi=False,
                 value="Ocupacion",
                 style={'width': "40%"}
                 ),
    
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='time_series1', figure={})

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
      Output(component_id='time_series1', component_property='figure')],
    [Input(component_id='slct_var1', component_property='value'),
     Input(component_id='slct_var2', component_property='value'),]
)
def update_graph(option_slctd1, option_slctd2):
    print(option_slctd1)
    print(type(option_slctd1))

    container = "The year chosen by user was: {}".format(option_slctd1)
    
    dff = df.copy()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(x=df['Fecha'], y=dff[option_slctd1], name="yaxis data"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df['Fecha'], y=dff[option_slctd2], name="yaxis data"),
        secondary_y=True,
    )
    
    # Add figure title
    fig.update_layout(
        title_text="Double Y Axis Example"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="xaxis title")

    # Set y-axes titles
    fig.update_yaxes(
        title_text="<b>primary</b> yaxis title", 
        secondary_y=False)
    fig.update_yaxes(
        title_text="<b>secondary</b> yaxis title", 
        secondary_y=True)
    
    return container, fig


#------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


