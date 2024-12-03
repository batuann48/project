import tkinter as tk 
from tkinter import messagebox
from calculations import calculate_carbon_footprint
from report_handler import save_to_csv


def calculate_and_save():


    try:
        electricity = float (entry_electricity.get())
        gas = float (entry_gas.get())
        travel = float (entry_travel.get())
        name = entry_name.get()

        if not name :
            raise ValueError("Name can not be empty!")
        
        # perform calculate
        results = calculate_carbon_footprint(electricity,gas,travel)
        results["Name"]= name

        # save results to csv
        save_to_csv(results)


        #display results 
        result_label.config(text=f"Total Carbon Footprint: {results['Total (kg CO2)']:.2f} kg CO2")

    except ValueError:
        messagebox.showerror("Input Error", str())



# !!! gui setup login !!! 

root = tk.Tk ()
root.title ("Carbon Footprint Calculator")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name =tk.Entry(root)
entry_name.grid(row=0, column=1)


tk.Label (root , text="Electricity (kWh):").grid(row=1 , column= 0)
entry_electricity =tk.Entry(root)
entry_electricity.grid(row=1, column=1)

tk.Label(root, text="Gas (m³):").grid(row=2, column=0)
entry_gas = tk.Entry(root)
entry_gas.grid(row=2, column=1)

tk.Label(root, text= "Travel (km):").grid(row=3, column=0)
entry_travel = tk.Entry(root)
entry_travel.grid(row=3, column=1)

tk.Button (root, text="Calculate",command=calculate_and_save).grid(row=4 ,column=0 ,columnspan=2)

result_label =tk.Label(root,text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
