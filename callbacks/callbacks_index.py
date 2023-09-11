from dash import dcc, html
from dash import Input, Output
from pages import index, country
from dash.dependencies import Input, Output
import dash
app = dash.Dash(__name__)

def display_page_callback(app):
    @app.callback(Output('page-content', 'children'),
                  Input('url', 'pathname'))
    def display_page(pathname):
        if pathname == '/country':
            return country.layout
        else:
            return index.layout  # Display the home page by default

