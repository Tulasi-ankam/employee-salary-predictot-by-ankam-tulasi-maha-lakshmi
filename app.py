
import streamlit as st
import pickle
import pandas as pd

# Load model and encoders
with open('model.pkl', 'rb') as f:
    data = pickle.load(f)
    model = data['model']
    encoders = data['encoders']

st.title("💼 Employee Salary Prediction")
st.write("Enter the following details to predict your salary:")

# Inputs
age = st.slider("Age", 18, 65, 25)
gender = st.selectbox("Gender", encoders['Gender'].classes_)
education = st.selectbox("Education", encoders['Education'].classes_)
job_role = st.selectbox("Job Role", encoders['Job Role'].classes_)
experience = st.slider("Years of Experience", 0, 40, 2)
workclass = st.selectbox("Workclass", encoders['Workclass'].classes_)
marital_status = st.selectbox("Marital Status", encoders['Marital Status'].classes_)
relationship = st.selectbox("Relationship", encoders['Relationship'].classes_)
race = st.selectbox("Race", encoders['Race'].classes_)

# Preprocess input
input_dict = {
    'Age': age,
    'Gender': encoders['Gender'].transform([gender])[0],
    'Education': encoders['Education'].transform([education])[0],
    'Job Role': encoders['Job Role'].transform([job_role])[0],
    'Years of Experience': experience,
    'Workclass': encoders['Workclass'].transform([workclass])[0],
    'Marital Status': encoders['Marital Status'].transform([marital_status])[0],
    'Relationship': encoders['Relationship'].transform([relationship])[0],
    'Race': encoders['Race'].transform([race])[0],
}

input_df = pd.DataFrame([input_dict])

if st.button("Predict Salary"):
    salary = model.predict(input_df)[0]
    st.success(f"💰 Predicted Salary: ₹{int(salary):,}")
