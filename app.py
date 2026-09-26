import streamlit as st
import joblib

st.title("Customer Churn Prediction")

st.write("My Predictive Customer Churn Project")

# Load the trained model
model = joblib.load("churn_model.pkl")

st.success("Churn model loaded successfully!")

st.write("The machine learning model is ready.")