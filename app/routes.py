# app/routes.py
# GOAL: This is the "Waiter". It listens for visitors to your website.
# If they go to the homepage ("/"), it shows the HTML form.
# If they submit the form ("/predict"), it takes the data, gives it to utils.py,
# and shows the result.

from flask import Blueprint, render_template, request

# Import the prediction function from utils.py (the "Chef")
from . import utils

# 1. Create a "Blueprint". 
# A Blueprint is like a mini-application that handles a group of URLs.
# We give it the name 'main' so Flask knows what to call it.
bp = Blueprint('main', __name__)
# --- 2. The HOMEPAGE (When user visits http://127.0.0.1:5000/) ---
@bp.route('/')
def home():
    """
    This function runs when you go to the root URL.
    It doesn't calculate anything. It just shows the input form (index.html).
    """
    location=utils.get_valid_locations()
    # render_template looks inside the 'app/templates/' folder.
    # It finds 'index.html' and sends it to the browser.
    return render_template('index.html',location=location)


# --- 3. The PREDICTION URL (When user clicks the "Predict" button) ---
# methods=['POST'] means this only accepts data submitted via a form.
# The form in index.html has action="/predict" and method="POST".
@bp.route('/predict', methods=['POST'])
def predict():
    """
    This runs when the user clicks "Predict Price".
    It grabs the numbers from the form, calls utils.predict_price(),
    and shows the result page.
    """
    try:
        # --- 3a. Get the data the user typed in the HTML form ---
        # The names inside request.form (e.g., 'total_sqft') MUST match
        # the 'name' attributes in your HTML input fields.
        total_sqft = request.form.get('total_sqft')
        bath = request.form.get('bath')
        bhk = request.form.get('bhk')
        location = request.form.get('location')
        
        # --- 3b. Basic Validation: Check if any field is empty ---
        if not all([total_sqft, bath, bhk, location]):
            # If empty, return an error message (the user will see this in the browser)
            return "Error: All fields are required. Please go back and fill everything."
        
        # --- 3c. Call the "Chef" (utils.py) to do the ML prediction ---
        # The result is either a number (e.g., 45.67) or an error string.
        predicted_price = utils.predict_price(total_sqft, bath, bhk, location)
        
        # --- 3d. Check if the prediction returned an error string ---
        # If it's a string, it means something went wrong (e.g., model not loaded)
        if isinstance(predicted_price, str) and "Error" in predicted_price:
            return predicted_price  # Show the error directly to the user
        
        # --- 3e. If successful, render the result page and pass the price ---
        # We send 'price=predicted_price' to the HTML so it can display it.
        # In result.html, we use {{ price }} to show it.
        return render_template('result.html', price=predicted_price)
    
    except Exception as e:
        # If ANYTHING unexpected crashes, show the error on the screen.
        # This is great for debugging when you're a beginner.
        return f"An unexpected error occurred: {str(e)}"