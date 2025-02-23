import streamlit as st
import base64
import os
from model import predict_heart_disease

# Load HTML file
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Display the HTML UI
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# Embed index.html
html_path = "index.html"
if os.path.exists(html_path):
    st.markdown(load_html(html_path), unsafe_allow_html=True)
else:
    st.error("index.html file not found. Please check the file path.")

# Form handling for predictions
st.subheader("Prediction Form")
with st.form(key="prediction_form"):
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.radio("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
    chol = st.number_input("Cholesterol", min_value=100, max_value=400, value=200)
    fbs = st.radio("Fasting Blood Sugar", ["Yes", "No"])
    restecg = st.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.number_input("CA", min_value=0, max_value=4, value=0)
    thal = st.selectbox("Thal", [0, 1, 2, 3])

    submit_button = st.form_submit_button("Predict")

# Handle prediction logic
if submit_button:
    features = [
        age, 1 if sex == "Male" else 0, cp, trestbps, chol, 1 if fbs == "Yes" else 0,
        restecg, thalach, 1 if exang == "Yes" else 0, oldpeak, slope, ca, thal
    ]
    
    prediction = predict_heart_disease(features)
    result = "❤️ Heart Disease Detected" if prediction == 1 else "✅ No Heart Disease"

    st.success(result)
