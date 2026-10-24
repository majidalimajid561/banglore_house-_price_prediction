import joblib
import pandas as pd
import numpy as np
model=None
try:
    model=joblib.load('../models/random_f.pkl')
    model_version='1.0'
except Exception as e:
    raise Exception(f"paht is not valid {e}")
def prediction(input:dict):
    # try to get df
    if model is None:
         raise RuntimeError("The machine learning model is not initialized or loaded.")
    try:
      input_df=pd.DataFrame([input])
      predicted_price=model.predict(input_df)[0]
      return round(predicted_price,2)
    except Exception as e:
        return {f"{e}"}

