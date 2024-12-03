def calculate_carbon_footprint(electricity,gas,travel):
    """calculate carbon footprint based on inputs."""

    return {
    "Electricity (kg CO2)": electricity * 0.233 ,
    "Gas (kg CO2)": gas * 2.204 ,
    "Travel (kg CO2)": travel * 0.192,
    "Total (kg CO2)": electricity * 0.233 + gas * 2.204 + travel * 0.192,      
  }

