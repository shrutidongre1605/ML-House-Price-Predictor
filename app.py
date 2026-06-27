import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("models/model.pkl")

# Load Dataset
data = pd.read_csv("data/housing.csv")

# Title
st.title("🏠 House Price Predictor")

# Inputs
house_id = st.number_input(
    "House ID",
    min_value=1,
    value=1
)

area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=2000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

floors = st.number_input(
    "Floors",
    min_value=1,
    max_value=5,
    value=2
)

yearbuilt = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2025,
    value=2010
)

location = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Suburban"]
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Fair", "Good"]
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

# Prediction Button
if st.button("Predict Price"):

    input_data = [[
        house_id,
        area,
        bedrooms,
        bathrooms,
        floors,
        yearbuilt,
        location_map[location],
        condition_map[condition],
        garage_map[garage]
    ]]

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ₹{prediction[0]:,.0f}"
    )

    # Visualization
    st.subheader("📊 Area vs Price Visualization")

    fig, ax = plt.subplots(figsize=(8, 5))

    # Existing houses
    ax.scatter(
        data["Area"],
        data["Price"],
        alpha=0.6,
        label="Dataset Houses"
    )

    # User prediction
    ax.scatter(
        area,
        prediction[0],
        s=250,
        marker="*",
        label="Your House"
    )

    ax.set_xlabel("Area (sq ft)")
    ax.set_ylabel("Price")
    ax.set_title("Area vs Price")

    ax.legend()

    st.pyplot(fig)

# Dataset Preview
st.subheader("📋 Dataset Preview")
st.dataframe(data.head())