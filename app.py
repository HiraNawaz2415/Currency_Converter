import streamlit as st
import requests

st.title("💰 Currency Converter")

# Supported currencies (including Pakistani Rupee - PKR)
currencies = ["USD", "EUR", "GBP", "INR", "CAD", "PKR"]

# User inputs
amount = st.number_input("Enter amount:", min_value=0.01, format="%.2f")
from_currency = st.selectbox("From:", currencies)
to_currency = st.selectbox("To:", currencies)

# Replace with your API key from ExchangeRate-API
API_KEY = "59d310182406f9e89a67f517"
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

if st.button("Convert"):
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        if to_currency in data["conversion_rates"]:
            rate = data["conversion_rates"][to_currency]
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("Invalid currency conversion.")
    else:
        st.error("API request failed. Please try again later.")
