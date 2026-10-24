from fastapi import FastAPI
from schema.user_input import BangaloreHouse
from modling.model import prediction,model_version


app=FastAPI()
@app.get('/')
def home():
    return "home price predction api"
@app.get('/health')
def health():
    return {"status":"Ok","model_load":"True","model_version":model_version}
@app.post('/predict')
def prediction_method(user_input:BangaloreHouse):
        input_data={ 
                'total_sqft':user_input.area_sqft,
                'bath':user_input.bath,
                'location_processed':user_input.location,
                'bhk':user_input.bhk
            }
        predicted_price=prediction(input_data)
        return {"Price":f"{predicted_price} lac"}
