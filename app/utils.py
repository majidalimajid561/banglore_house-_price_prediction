# app/utils.py
# GOAL: This is the "Brain" of your application.
# It loads the saved model, handles the complex One-Hot Encoding for locations,
# and makes predictions. Routes.py just calls the function in this file.

import joblib
import os
import pandas as pd
import numpy as np

# --- 1. GET THE FILE PATHS (CRITICAL FOR BEGINNERS) ---
# When you run Flask, the "current working directory" might not be where this file is.
# To be 100% safe, we use __file__ which is the absolute path to THIS file (utils.py).


# Example path: C:/Users/You/house_price_predictor/app/utils.py


# os.path.dirname(__file__) -> C:/Users/You/house_price_predictor/app
# os.path.dirname(os.path.dirname(__file__)) -> C:/Users/You/house_price_predictor (The ROOT!)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Now we join the root directory with the 'models' folder and the filenames.

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'random_f.pkl')
print(f"Looking for model at: {MODEL_PATH}")
LOCATIONS_PATH = os.path.join(BASE_DIR, 'models', 'valid_locations.pkl')
# This helps you debug if files are missing

## --- 2. LOAD THE MODEL AND FEATURES (Happens ONLY once when server starts) ---


try:
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print(f"❌ ERROR: Model not found at {MODEL_PATH}")
    print("   Make sure you saved 'best_model.pkl' in the 'models' folder.")
    model = None  # Set to None so we can check later

try:
    with open(LOCATIONS_PATH, 'rb') as f:
        VALID_LOCATIONS = joblib.load(f)
    print("✅ location load  successfully!")
except FileNotFoundError:
    print(f"❌ ERROR: location  not found at {LOCATIONS_PATH}")
    print("   Make sure you saved 'loaction' in the 'models' folder.")
      # Set to None so we can check later
    VALID_LOCATIONS = []
def get_valid_locations():
    """Returns the list of valid locations for the dropdown."""
    return VALID_LOCATIONS





# --- 3. THE PREDICTION FUNCTION (This is called by routes.py) ---
def predict_price(total_sqft, bath, bhk, location):
    """
    Converts user inputs into a DataFrame, runs the model, and returns the price.
    
    Parameters:
        total_sqft (str or float): Total square footage
        bath (str or int): Number of bathrooms
        bhk (str or int): Number of bedrooms
        location (str): Name of the locality (e.g., "Whitefield")
    
    Returns:
        float or str: Predicted price in Lakhs (rounded to 2 decimals), or an error message.
    """
    
     # --- 3a. Safety Check: Make sure the model loaded correctly ---
    if model is None:
         
         return "Error: Model files are missing. Please check your 'models' folder."




    
#      --- 3b. Convert inputs to numbers (floats) ---
#     # We use float() so that if the user types "1200", it becomes 1200.0
#     # If they type "1200.5", it stays 1200.5
    try:
        sqft = float(total_sqft)
        baths = float(bath)
        bedrooms = float(bhk)
    except ValueError:
        return "Error: Please enter valid numbers for Square Feet, Bath, and BHK."
    
     # --- 3. Validate location against the known list ---
    if VALID_LOCATIONS and location not in VALID_LOCATIONS:
        # If location is not in our list, suggest similar or show error
        return f"Error: Location '{location}' not found. Please select from the dropdown list."
    if sqft < 272.251:
        return "Error: Total Square Feet seems too low. Please enter a value greater than 100."
    if sqft > 50000:
        return "Error: Total Square Feet seems too high. Please enter a realistic value."
    if bedrooms < 1:
        return "Error: BHK must be at least 1."
    if bedrooms > 10:
        return "Error: BHK seems too high. Please enter a realistic value."
    input_data = pd.DataFrame([[
        sqft,           # total_sqft
        baths,          # bath
        bedrooms,       # bhk
        location        # location_processed (text)
    ]], columns=['total_sqft', 'bath', 'bhk', 'location_processed'])
    
    # --- 5. Predict using the full pipeline ---
    try:
        predicted_price = model.predict(input_data)[0]
        if predicted_price < 0:
            # Log this so you know it happened
            print(f"⚠️ Warning: Negative prediction ({predicted_price}) for input: {input_data}")
            # Option 1: Return an error
            return f"Error: The prediction resulted in a negative value. Please check your inputs.{predicted_price}"
            # Option 2: Cap at 0 (uncomment if you prefer this)
        return round(predicted_price, 2)
    except Exception as e:
        return f"Prediction Error: {str(e)}"
    

if __name__ == "__main__":
    print("\n--- Running a Quick Test of utils.py ---")
    #Replace these values with real ones from your dataset
    test_price = predict_price(825, 2, 3, "Whitefield")
    print(f"Test Prediction for 800 sqft, 2 Bath, 3 BHK in Whitefield: {test_price} Lakhs")