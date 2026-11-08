import streamlit as st
import joblib
import pandas as pd

# load the saved model
data = joblib.load("water_model.pkl")
model = data["model"]
features = data["features"]
medians = data["medians"]

st.title("Water Potability Predictor")
st.write("Enter the water measurements below.")

# collect inputs (one box per column)
values = {}
for f in features:
    values[f] = st.number_input(f, value=float(medians[f]))

# predict and show result
if st.button("Predict"):
    result = model.predict(pd.DataFrame([values]))[0]
    if result == 1:
        st.success("Water is safe to drink")
    else:
        st.error("Water is NOT safe to drink")