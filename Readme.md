# 🏠 Bangalore House Price Predictor

A Machine Learning web application that predicts house prices in Bangalore, India based on key features like total square footage, number of bedrooms (BHK), bathrooms, and location.

## Home Page

<img src="image/house price.png" width="400" alt="Form Page"/>

## 📊 How it Works
1. User inputs house details (Square Feet, Bathrooms, BHK, Location).
2. The Flask backend processes the input.
3. A pre-trained Scikit-learn pipeline (with One-Hot Encoding & Scaling) predicts the price.
4. The estimated price (in ₹ Lakhs) is displayed to the user.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn (Random Forest/Lasso/Ridge)
- **Frontend:** HTML, CSS

## 📂 Project Structure
house-price-predictor/
├── app/ # Flask application package
├── models/ # Saved pipeline (.pkl file)
├── run.py # Entry point
├── requirements.txt # Dependencies
└── README.md


## 🏃‍♂️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/majidalimajid561/house-price-predictor.git
   cd house-price-predictor

2. Create a virtual environment
 '''python -m venv venv
 source venv/bin/activate  '''

3. pip install -r requirements.txt

4. streamlit run.py
