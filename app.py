import tkinter as tk
from tkinter import ttk

# Conversion dictionaries
length_units = {"Metre": 1, "Kilometre": 0.001, "Centimetre": 100, "Millimetre": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701}
weight_units = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Conversion function
def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()
        
        if category == "Length":
            result = value * length_units[to_unit] / length_units[from_unit]
        elif category == "Weight":
            result = value * weight_units[to_unit] / weight_units[from_unit]
        elif category == "Temperature":
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    result = value + 273.15
                else:
                    result = value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    result = value - 273.15
                elif to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value
        label_result.config(text=f"Result: {result:.4f}")
    except ValueError:
        label_result.config(text="Invalid input!")

# Update unit options based on category
def update_units(event):
    category = combo_category.get()
    if category == "Length":
        units = list(length_units.keys())
    elif category == "Weight":
        units = list(weight_units.keys())
    elif category == "Temperature":
        units = temperature_units
    combo_from["values"] = units
    combo_to["values"] = units
    combo_from.current(0)
    combo_to.current(1)

# GUI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Widgets
tk.Label(root, text="Select Category:").pack(pady=5)
combo_category = ttk.Combobox(root, values=["Length", "Weight", "Temperature"])
combo_category.pack()
combo_category.current(0)

tk.Label(root, text="From:").pack(pady=5)
combo_from = ttk.Combobox(root)
combo_from.pack()

tk.Label(root, text="To:").pack(pady=5)
combo_to = ttk.Combobox(root)
combo_to.pack()

tk.Label(root, text="Enter Value:").pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack()

btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Event binding
combo_category.bind("<<ComboboxSelected>>", update_units)
update_units(None)

root.mainloop()
