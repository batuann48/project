import pandas as pd
import os


def save_to_csv(data, filename="carbon_data.csv"):
    """Save individual data to CSV file."""
    if not os.path.exists(filename):
       df = pd.DataFrame(columns=["Name", "Electricity (kg CO2)","Gas (kg CO2)","Travel (kg CO2)","Total (kg CO2)"])


    else:
       df = pd.read_csv(filename)

    new_row = pd.DataFrame([data])
    if not new_row.isnull().all(axis=1).any():
       df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(filename, index=False)
   
