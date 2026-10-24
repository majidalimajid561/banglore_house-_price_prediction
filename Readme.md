# 🏠 Bangalore House Price Predictor

An end-to-end Machine Learning project that predicts house prices in Bangalore based on various features like location, square footage, number of bedrooms, and more. This project features a modular Flask web application, a FastAPI backend, and a Streamlit frontend.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![FastAPI](https://img.shields.io/badge/FastAPI-0.90%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)

---

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [How to Run Locally](#how-to-run-locally)
- [Screenshots](#screenshots)
- [Author](#author)

---

## 📌 About the Project
Buying a house is a major decision, and prices vary drastically based on location and amenities. This project uses Machine Learning to estimate the price of a house (in Lakhs ₹) in Bangalore. 

The project provides **three different interfaces**:
1. **Flask Web App:** A traditional modular web app serving HTML/CSS templates.
2. **FastAPI Backend:** A high-performance API for programmatic access.
3. **Streamlit App:** A modern, interactive UI that connects to the FastAPI backend.

---

## 📊 Dataset
The model was trained on the famous **Bengaluru House Price Data** (Kaggle).
- **Raw Dataset Shape:** 13,320 rows × 9 columns
- **Features Used:** `area_type`, `availability`, `location`, `size`, `society`, `total_sqft`, `bath`, `balcony`, `price`
- **Target Variable:** `price` (in Lakhs)

---

## 🤖 Model Performance
Multiple regression algorithms were trained and evaluated. The **Random Forest Regressor** was selected as the final model due to its highest accuracy and lowest error.

| Model | Test R² Score | Test RMSE (Lakhs) |
| :--- | :--- | :--- |
| Linear Regression | 0.8746 | 32.99 |
| Lasso Regression | 0.8721 | 33.32 |
| Ridge Regression | 0.8747 | 32.98 |
| Gradient Boosting | 0.8771 | 32.65 |
| **Random Forest (Best)** | **0.8830** | **31.87** |

*The trained pipeline is saved as `random_f.pkl` in the `models/` directory.*

---

## 📂 Project Structure
```text
house-price-predictor/
│
├── app/                        # Flask Application (HTML/CSS Frontend)
│   ├── static/                 # CSS files (style_idx.css, style_res.css)
│   ├── templates/              # HTML files (index.html, result.html)
│   ├── __init__.py             # Flask App Factory
│   ├── routes.py               # Flask Routes (/ and /predict)
│   └── utils.py                # Model loading & prediction logic
│
├── data/                       # Dataset files
│   ├── bengaluru_house_prices.csv
│   └── processed_df.csv
│
├── fast_api/                   # FastAPI Backend
│   ├── config/config.py
│   ├── modling/model.py
│   ├── schema/user_input.py
│   └── main.py                 # API Entry point
│
├── image/                      # Screenshots for README
│   ├── houseprice_home.png
│   └── result.png
│
├── models/                     # Saved ML Models
│   └── random_f.pkl
│
├── Script/                     # Jupyter Notebooks
│   └── house_Price.ipynb       # EDA, Data Cleaning & Model Training
│
├── streamlit/                  # Streamlit Frontend
│   ├── app.py                  # Standard Streamlit app
│   └── fast_api_streamlit.py   # Streamlit app connected to FastAPI
│
├── .gitignore
├── requirements.txt            # Project Dependencies
├── run.py                      # Entry point to run Flask app
└── README.md
```

## 🛠️ Tech Stack
Data Processing & ML: Pandas, NumPy, Scikit-Learn

Backend APIs: Flask, FastAPI, Uvicorn

Frontend: HTML5, CSS3, Streamlit

Model Serialization: Joblib

🚀 How to Run Locally
``` bash
1. Clone the repository
git clone https://github.com/majidalimajid561/house-price-predictor.git
cd house-price-predictor

2. Create a virtual environment and install dependencies
python -m venv venv
pip install -r requirements.txt

3. Run the Flask App
python run.py 

4. Run the FastAPI Backend
uvicorn fast_api.main:app --reload

5. Run the Streamlit App
streamlit run streamlit/app.py
```

### 👨‍💻 Author

Majid Mehmood

GitHub: @majidalimajid561

---
if you find this project useful, please consider giving it a ⭐!

