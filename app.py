import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load trained pipeline/model
model = joblib.load("heart_disease_model.pkl")

st.title("❤️ Heart Disease Prediction App")
st.write("Please enter the patient's clinical information below.")

st.subheader("Patient Information")

age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex", ["M", "F"])

chest_pain_type = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure",
    min_value=0,
    max_value=300,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0,
    max_value=700,
    value=200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST", "LVH"]
)

max_hr = st.number_input(
    "Max Heart Rate",
    min_value=60,
    max_value=250,
    value=150
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["Y", "N"]
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=-5.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

if st.button("Predict"):
    # Create data exactly in the feature format used while training
    input_data = pd.DataFrame([{
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        # One-Hot Encoded categorical columns
        "Sex_M": int(sex == "M"),

        "ChestPainType_ATA": int(chest_pain_type == "ATA"),
        "ChestPainType_NAP": int(chest_pain_type == "NAP"),
        "ChestPainType_TA": int(chest_pain_type == "TA"),
        # ASY is the base/reference category; all above become 0.

        "RestingECG_Normal": int(resting_ecg == "Normal"),
        "RestingECG_ST": int(resting_ecg == "ST"),
        # LVH is the base/reference category.

        "ExerciseAngina_Y": int(exercise_angina == "Y"),

        "ST_Slope_Flat": int(st_slope == "Flat"),
        "ST_Slope_Up": int(st_slope == "Up"),
        # Down is the base/reference category.
    }])

    # Features created during model training
    input_data["Cholesterol*Age"] = (
        input_data["Cholesterol"] * input_data["Age"]
    )

    input_data["HR_per_Age"] = (
        input_data["MaxHR"] / input_data["Age"]
    )

    # Match exactly the saved model's expected feature columns and their order.
    expected_features = model.named_steps["model"].feature_names_in_
    input_data = input_data.reindex(
        columns=expected_features,
        fill_value=0
    )

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Result")

    if prediction == 1:
        st.error(
            f"High Risk of Heart Disease — Probability: {probability:.2%}"
        )
    else:
        st.success(
            f"Low Risk of Heart Disease — Probability: {probability:.2%}"
        )

    st.caption(
        "This application is for educational purposes and is not a medical diagnosis."
    )
