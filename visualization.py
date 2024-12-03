import pandas as pd
import matplotlib.pyplot as plt

def plot_carbon_footprint():
    """Plot a bar chart of total carbon footprint by user."""
    #load data
    df = pd.read_csv("carbon_data.csv")

    # bar chart for total carbon

    plt.bar(df["Name"],df["Total (kg CO2)"])
    plt.xlabel ("User")
    plt.ylabel("Total Carbon Footprint (kg CO2)")
    plt.title("Carbon Footprint by User")
    plt.show()

def show_table():

    """Display data as a table in the terminal."""

    df = pd.read_csv("carbon_data.csv")
    print(df.to_string(index=False))