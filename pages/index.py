from dash import dcc, html
import plotly.graph_objs as go
from utils import util
import numpy as np
from calculations import monte_carlo as mc

data = util.select_row(params=('GDP growth (annual %)',))

indicator_name = data[0][2]


gdp_growth_rates = [record[5] for record in data]
years = [record[4] for record in data]
mean_growth_rate = np.mean(gdp_growth_rates)
median_value = np.median(gdp_growth_rates)

start_year = 2023
end_year = 2032

# Perform the Monte Carlo simulation
simulated_gdp_trajectories = mc.monte_carlo_simulation(data, start_year, end_year)

# Create traces for simulated GDP trajectories
simulated_traces = []
for i, simulated_gdp in enumerate(simulated_gdp_trajectories):
    trace = go.Scatter(x=list(range(start_year, end_year + 1)), y=simulated_gdp, mode='lines', name=f'Simulation {i + 1}')
    simulated_traces.append(trace)


# Create a Plotly trace for the line chart
trace = go.Scatter(x=years, y=gdp_growth_rates, mode='lines+markers')

# Create a trace for the mean line (dotted line)
mean_trace = go.Scatter(
    x=years,
    y=[mean_growth_rate] * len(years),
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

layout =html.Div(
    [
        dcc.Graph(
            id='original-plot',
            figure={
                'data': [trace, mean_trace, median_trace],  # Add the original data and other traces
                'layout': {
                    'xaxis': {'title': 'Years'},
                    'yaxis': {'title': 'Annual %'},
                    'title': indicator_name,
                    'text': 'GDP: Gross Domestic Product',
                    'legend': {'x': 0, 'y': 1}  # Adjust the legend position
                }
            }
        ),
        dcc.Graph(
            id='monte-carlo-plot',
            figure={
                'data': simulated_traces,  # Add the simulated traces to this graph
                'layout': {
                    'xaxis': {'title': 'Years'},
                    'yaxis': {'title': 'Annual %'},
                    'title': 'Monte Carlo Simulation',
                    'text': 'GDP: Gross Domestic Product',
                    
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

