import streamlit as st
import pandas as pd
import numpy as np
import joblib 
st.set_page_config(
    page_icon="🛖",
    page_title="House price predition",
    layout='centered'
)

@st.cache_resource
def load_model():
    return joblib.load('models/random_f.pkl')
model = load_model()
# ---------- Header ----------
st.title("🛖House price predition")
st.markdown("""
    Enter  details below and find out how would be price of this house.
""")
st.divider()
df=joblib.load('data/processed_df.csv')
location=df['location_processed'].unique()
sqft=st.number_input("total area square feet",min_value=270,max_value=20000)
bath=st.number_input("total number of bath",min_value=1,max_value=10)
bhk=st.number_input("Number of Bhk",min_value=1,max_value=10)
location=st.selectbox("Location",location)

if st.button('Predict'):
    input_data=pd.DataFrame(
        {"total_sqft":[sqft],
         "bath":[bath],
         "location_processed":[location],
         "bhk":[bhk]})
    predict_price=model.predict(input_data)[0]
    st.metric(label="Predicted Price", value=round(predict_price,2))

