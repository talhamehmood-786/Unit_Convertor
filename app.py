import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    # Convert to meters first, then to target unit
    value_in_meters = value / length_units[from_unit]
    return value_in_meters * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    value_in_kg = value / weight_units[from_unit]
    return value_in_kg * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def main():
    st.title("Unit Converter")
    
    # Sidebar for conversion type selection
    conversion_type = st.sidebar.selectbox(
        "Choose conversion type",
        ["Length", "Weight", "Temperature"]
    )
    
    # Input value
    value = st.number_input("Enter value to convert", value=0.0)
    
    # Conversion logic based on type
    if conversion_type == "Length":
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", 
                                   ["meters", "kilometers", "centimeters", "millimeters",
                                    "miles", "yards", "feet", "inches"])
        with col2:
            to_unit = st.selectbox("To",
                                 ["meters", "kilometers", "centimeters", "millimeters",
                                  "miles", "yards", "feet", "inches"])
        
        if st.button("Convert"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            
    elif conversion_type == "Weight":
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From",
                                   ["kilograms", "grams", "milligrams", "pounds", "ounces"])
        with col2:
            to_unit = st.selectbox("To",
                                 ["kilograms", "grams", "milligrams", "pounds", "ounces"])
        
        if st.button("Convert"):
            result = weight_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
            
    elif conversion_type == "Temperature":
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From",
                                   ["celsius", "fahrenheit", "kelvin"])
        with col2:
            to_unit = st.selectbox("To",
                                 ["celsius", "fahrenheit", "kelvin"])
        
        if st.button("Convert"):
            result = temp_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
