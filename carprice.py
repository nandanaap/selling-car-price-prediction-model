import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Load and prepare the dataset
df = pd.read_csv('cardata.csv')
inputs = df.drop(['Car_Name', 'Owner', 'Seller_Type'], axis='columns')
target = df.Selling_Price

# Encode categorical features
Numerics = LabelEncoder()
inputs['Fuel_Type_n'] = Numerics.fit_transform(inputs['Fuel_Type'])
inputs['Transmission_n'] = Numerics.fit_transform(inputs['Transmission'])

# Prepare the features
inputs_n = inputs.drop(['Fuel_Type', 'Transmission', 'Selling_Price'], axis='columns')

# Train the model
model = linear_model.LinearRegression()
model.fit(inputs_n.values, target)

# Initialize the main application window
root = tk.Tk()

# Set window title
root.title("SECOND HAND CAR SELLING PRICE PREDICTION SYSTEM")

# Set window size
root.geometry("800x400")

# Add a label
title_label = tk.Label(root, text="Car Price Prediction App", font=('Helvetica', 16, "bold"))
title_label.grid(row=0, column=1, columnspan=2,pady=10)

# Create entry fields for user inputs
tk.Label(root, text="Year of the Car", font=('Helvetica', 12)).grid(row=1, column=0, sticky=tk.W, padx=10)
year_entry = tk.Entry(root)
year_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="Current Price of the Car", font=('Helvetica', 12)).grid(row=2, column=0, sticky=tk.W, padx=10)
current_price_entry = tk.Entry(root)
current_price_entry.grid(row=2, column=1, padx=10)

tk.Label(root, text="Kms Driven         ", font=('Helvetica', 12, )).grid(row=3, column=0, sticky=tk.W, padx=10)
kms_driven_entry = tk.Entry(root)
kms_driven_entry.grid(row=3, column=1, padx=10)

tk.Label(root, text="Fuel Type : Petrol=0, Diesel=1, CNG=2", font=('Helvetica', 12)).grid(row=4, column=0, sticky=tk.W, padx=10)
fuel_type_entry = tk.Entry(root)
fuel_type_entry.grid(row=4, column=1, padx=10)

tk.Label(root, text="car model : Manual=0, Automatic=1  ", font=('Helvetica', 12)).grid(row=5, column=0, sticky=tk.W, padx=10)
transmission_entry = tk.Entry(root)
transmission_entry.grid(row=5, column=1, padx=10)

# Function to display the dataset
def show_dataset():
    dataset_window = tk.Toplevel(root)
    dataset_window.title("Dataset")
    dataset_window.geometry("1000x400")
    
    tree = ttk.Treeview(dataset_window)
    tree.pack(expand=True, fill=tk.BOTH)

    # Define columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    
    # Define headings
    for column in tree["columns"]:
        tree.heading(column, text=column)
    
    # Add data to the tree
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    # Add a scrollbar
    scrollbar = ttk.Scrollbar(dataset_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

# Button to display the dataset
df_button = tk.Button(root, text="Show Dataset", command=show_dataset)
df_button.grid(row=6, column=0, columnspan=2, pady=10)

# Function to predict the price
def predict_price():
    try:
        year = float(year_entry.get())
        current_price = float(current_price_entry.get())
        kms_driven = float(kms_driven_entry.get())
        fuel_type = int(fuel_type_entry.get())
        transmission = int(transmission_entry.get())
        
        prediction = model.predict([[year, current_price, kms_driven, fuel_type, transmission]])
        messagebox.showinfo("Predicted Selling Price", f"Predicted Selling Price: {prediction[0]:.2f}")
    except Exception as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Add a button to make prediction
predict_button = tk.Button(root, text="Predict Price", command=predict_price)
predict_button.grid(row=7, column=0, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()
