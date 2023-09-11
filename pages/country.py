from dash import dcc, html


layout = html.Div([
    html.H1('Country-specific Dashboard'),
    dcc.Dropdown(
        id='country-dropdown',
        
        value='United States'
    ),
    dcc.Graph(id='country-graph')
])