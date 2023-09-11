from dash import dcc, html
import plotly.graph_objs as go
from utils import util
import numpy as np

data = util.select_row(params=('GDP growth (annual %)',))
indicator_name = data[0][2]


values = [record[5] for record in data]
years = [record[4] for record in data]
mean_value = sum(values) / len(values)
median_value = np.median(values)



# Create a Plotly trace for the line chart
trace = go.Scatter(x=years, y=values, mode='lines+markers')

# Create a trace for the mean line (dotted line)
mean_trace = go.Scatter(
    x=years,
    y=[mean_value] * len(years),
    mode='lines',
    line=dict(dash='dot'),  # Use 'dot' for a dotted line
    name='Mean',  # Name for the legend
    
)

median_trace = go.Scatter(
    x=years,
    y=[median_value] *len(years),
    mode = 'lines',
    line=dict(dash='dot'),  # Use 'dot' for a dotted line
    name='Median'  # Name for the legend
)

layout = html.Div(
    [
        dcc.Graph(
            id='line-plot',
            figure={
                'data': [trace, mean_trace,median_trace],  # Add the mean trace
                'layout': {
                    'xaxis': {'title': 'Years'},
                    'yaxis': {'title': 'annual %'},
                    'title': indicator_name,
                    'text': 'GDP: Gross Domestic Product',
                    'legend': {'x': 0, 'y': 1}  # Adjust the legend position
                }
            }
        )
    ],
    className='card'
)



external_css = [
    # Link to your external CSS file
    html.Link(
        rel='stylesheet',
        href='/assets/css/styles.css'
    )
]

