import streamlit as st
import joblib

model = joblib.load("models/model.pkl")

st.title("🏠 House Price Predictor")

id = st.number_input("House ID", min_value=1)

area = st.number_input("Area", min_value=100)

bedrooms = st.number_input("Bedrooms", min_value=1)

bathrooms = st.number_input("Bathrooms", min_value=1)

floors = st.number_input("Floors", min_value=1)

yearbuilt = st.number_input("Year Built", min_value=1900)

location = st.selectbox(
    "Location",
    ["Downtown", "Suburban", "Rural"]
)

condition = st.selectbox(
    "Condition",
    ["Fair", "Good", "Excellent"]
)

garage = st.selectbox(
    "Garage",
    ["No", "Yes"]
)

# Encoding
location_map = {
    "Downtown": 0,
    "Rural": 1,
    "Suburban": 2
}

condition_map = {
    "Excellent": 0,
    "Fair": 1,
    "Good": 2
}

garage_map = {
    "No": 0,
    "Yes": 1
}

if st.button("Predict Price"):

    prediction = model.predict([[
        id,
        area,
        bedrooms,
        bathrooms,
        floors,
        yearbuilt,
        location_map[location],
        condition_map[condition],
        garage_map[garage]
    ]])

    st.success(
        f"Predicted House Price: ₹{prediction[0]:,.0f}"
    )