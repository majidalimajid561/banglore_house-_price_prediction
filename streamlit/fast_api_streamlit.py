import pandas as pd 
import numpy as np
import streamlit as st
import joblib
import requests
# ---------- Page config ----------
st.set_page_config(
    page_title="House Price prediction",
    page_icon="🛖",
    layout="centered"
)

st.title("🛖House price prediction")
st.markdown("""
    Enter  details below and find out how would be price of this house.
""")
api="http://localhost:8000/predict"

st.divider()
df=joblib.load('../data/processed_df.csv')
location=df['location_processed'].unique()

sqft=st.number_input("total area square feet",min_value=280,max_value=20000)
bath=st.number_input("total number of bath",min_value=1,max_value=10)
bhk=st.number_input("Number of Bhk",min_value=1,max_value=10)
location=st.selectbox("Location",location)


if st.button("Predict_price"):
    input_data={
        'area_sqft':sqft,
        'bhk':bhk,
        'bath':bath,
        'location':location
    }
    try:
         response=requests.post(api,json=input_data)
         if response.status_code==200:
              result=response.json()
              st.success(f"prediction price is {result['Price']}")
         else:
              st.error(f"API error {response.status_code} - {response.content}")
    except Exception as e:
    # Adding 'as e' and printing it will show you the exact error if it fails again
     st.error(f"error in response: {e}")





