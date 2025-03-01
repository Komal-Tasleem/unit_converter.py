import streamlit as st
from forex_python.converter import CurrencyRates
import time

# Page Configuration
st.set_page_config(page_title='Universal Unit Converter', page_icon='🚀', layout='wide')

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #2c3e50;
            text-transform: uppercase;
        }
        .stButton>button {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white !important;
            font-size: 18px;
            padding: 12px 20px;
            border-radius: 8px;
            width: 100%;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2a5298, #1e3c72);
            transform: scale(1.05);
        }
        .stSelectbox, .stTextInput, .stNumberInput {
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        .success-message {
            font-size: 20px;
            font-weight: bold;
            color: #27ae60;
            text-align: center;
            padding: 10px;
            background-color: #eafaf1;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1 class='main-title'>🚀 Universal Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("Easily convert different units of Length, Weight, Temperature, and Currency.")

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox("Choose Conversion Type", [
    "Length", "Weight", "Temperature", "Currency"
])

# Length Conversion
if conversion_type == "Length":
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701}
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        converted_value = value * (length_units[to_unit] / length_units[from_unit])
        st.markdown(f"<p class='success-message'>{value} {from_unit} = {converted_value:.4f} {to_unit}</p>", unsafe_allow_html=True)

# Weight Conversion
elif conversion_type == "Weight":
    weight_units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1e6, "Pounds": 2.20462, "Ounces": 35.274}
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        converted_value = value * (weight_units[to_unit] / weight_units[from_unit])
        st.markdown(f"<p class='success-message'>{value} {from_unit} = {converted_value:.4f} {to_unit}</p>", unsafe_allow_html=True)

# Temperature Conversion
elif conversion_type == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", temp_units)
    to_unit = st.selectbox("To Unit", temp_units)
    value = st.number_input("Enter Value", format="%.2f")
    
    def convert_temperature(val, from_u, to_u):
        if from_u == to_u:
            return val
        elif from_u == "Celsius" and to_u == "Fahrenheit":
            return (val * 9/5) + 32
        elif from_u == "Celsius" and to_u == "Kelvin":
            return val + 273.15
        elif from_u == "Fahrenheit" and to_u == "Celsius":
            return (val - 32) * 5/9
        elif from_u == "Fahrenheit" and to_u == "Kelvin":
            return (val - 32) * 5/9 + 273.15
        elif from_u == "Kelvin" and to_u == "Celsius":
            return val - 273.15
        elif from_u == "Kelvin" and to_u == "Fahrenheit":
            return (val - 273.15) * 9/5 + 32
        return val
    
    if st.button("Convert"):
        converted_value = convert_temperature(value, from_unit, to_unit)
        st.markdown(f"<p class='success-message'>{value} {from_unit} = {converted_value:.2f} {to_unit}</p>", unsafe_allow_html=True)

# Currency Conversion
elif conversion_type == "Currency":
    c = CurrencyRates()
    currency_list = ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"]
    from_currency = st.selectbox("From Currency", currency_list)
    to_currency = st.selectbox("To Currency", currency_list)
    amount = st.number_input("Enter Amount", min_value=0.01, format="%.2f")
    if st.button("Convert"):
        with st.spinner("Fetching exchange rate..."):
            time.sleep(2)  # Fake delay for better UX
            try:
                converted_amount = c.convert(from_currency, to_currency, amount)
                st.markdown(f"<p class='success-message'>{amount} {from_currency} = {converted_amount:.2f} {to_currency}</p>", unsafe_allow_html=True)
            except:
                st.error("Error fetching exchange rate. Try again later.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; font-size: 16px; color: grey;'>❤️ Made with love by <b>KOMAL TASLEEM</b> using Streamlit.</p>", unsafe_allow_html=True)
