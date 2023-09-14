import numpy as np
import matplotlib.pyplot as plt
from utils import util


def monte_carlo_simulation(data, start_year, end_year):
    num_simulations = 1000
    # Extract the years and GDP growth rates from your data
    years = [record[4] for record in data]
    gdp_growth_rates = [record[5] for record in data]

    # Number of simulations and simulation parameters
    mean_growth_rate = np.mean(gdp_growth_rates)
    std_dev_growth_rate = np.std(gdp_growth_rates)

    # Initialize arrays to store simulated GDP trajectories
    simulated_gdp_trajectories = []

    # Perform Monte Carlo simulation
    for _ in range(num_simulations):
        # Generate random samples of GDP growth rates
        random_growth_rates = np.random.normal(mean_growth_rate, std_dev_growth_rate, len(years) - 1)

        # Initialize GDP trajectory with the latest available GDP value (2022)
        simulated_gdp = [gdp_growth_rates[-1]]

        # Project future GDP values based on random growth rates
        for year in range(start_year, end_year):
            index = year - years[-1]  # Assuming years are continuous
            projected_gdp = simulated_gdp[-1] * (1 + random_growth_rates[index] / 100)  # Convert to decimal growth rate
            simulated_gdp.append(projected_gdp)

        simulated_gdp_trajectories.append(simulated_gdp)

    return simulated_gdp_trajectories
