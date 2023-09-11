import dash
from dash.dependencies import Input, Output
from dash import dcc, html
from dash import Input, Output
from pages import index, country
from utils.util import select_row
from callbacks.callbacks_index import display_page_callback
app = dash.Dash(__name__)

# Define the sidebar layout
sidebar = html.Div(
    id='sidebar',
    className='sidebar',
    children=[
        html.H2('Dashboard'),
        dcc.Link('Home', href='/', className='sidebar-link'),
        dcc.Link('Country Dashboard', href='/country', className='sidebar-link'),
    ]
)

# Define the main app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id='page-content'),
    html.Link(
        rel='stylesheet',
        href='/assets/sidebar.css'  # Make sure this path is correct
    )
])

display_page_callback(app)



if __name__ == '__main__':
   app.run_server(debug=True)
  

    