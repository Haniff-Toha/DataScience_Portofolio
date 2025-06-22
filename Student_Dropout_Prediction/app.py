import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load model
model = joblib.load("model/rf_model.joblib")

# Load scaler (assuming you've saved it, or redefine the same fit here)
scaler = joblib.load("model/scaler.joblib")  # If not saved, manually define it as used before

st.title("🎓 Student Dropout Prediction App")

st.markdown("""
This app predicts whether a student is likely to **drop out** based on their academic and demographic background.
""")

# ---- Input form ----
st.header("🔍 Student Information")

col1, col2 = st.columns(2)

with col1:
    marital_status = st.selectbox("Marital Status", [1, 2, 3, 4, 5, 6])
    application_mode = st.selectbox("Application Mode", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
    application_order = st.slider("Application Order", 0, 9, 1)
    course = st.selectbox("Course", [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991])
    daytime_evening = st.selectbox("Attendance", [0, 1])
    previous_qualification = st.selectbox("Previous Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43])
    nationality = st.selectbox("Nationality", [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109])
    mother_qualification = st.selectbox("Mother's Qualification", list(range(1, 45)))
    father_qualification = st.selectbox("Father's Qualification", list(range(1, 45)))
    mother_occupation = st.selectbox("Mother's Occupation", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194])
    father_occupation = st.selectbox("Father's Occupation", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 112, 114, 121, 122, 123, 124, 131, 132, 134, 135, 141, 143, 144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 181, 182, 183, 192, 193, 194, 195])

with col2:
    prev_qualification_grade = st.number_input("Previous Qualification Grade (0-200)", min_value=0.0, max_value=200.0, step=1.0)
    admission_grade = st.number_input("Admission Grade (0-200)", min_value=0.0, max_value=200.0, step=1.0)
    displaced = st.radio("Displaced", [0, 1])
    special_needs = st.radio("Educational Special Needs", [0, 1])
    debtor = st.radio("Debtor", [0, 1])
    fees_up_to_date = st.radio("Tuition Fees Up-to-Date", [0, 1])
    gender = st.radio("Gender", [0, 1])  # 0: Female, 1: Male
    scholarship = st.radio("Scholarship Holder", [0, 1])
    age = st.slider("Age at Enrollment", 16, 70, 20)
    international = st.radio("International Student", [0, 1])
    units_approved = st.slider("2nd Sem Units Approved", 0.0, 30.0, 5.0)
    unemployment_rate = st.slider("Unemployment Rate", 0.0, 20.0, 5.0)
    inflation_rate = st.slider("Inflation Rate", -5.0, 20.0, 2.0)
    gdp = st.slider("GDP (Billions)", 0.0, 200.0, 90.0)

# Predict
if st.button("📊 Predict Dropout Risk"):
    # Recreate same feature order used in training
    input_data = np.array([[
        marital_status, application_mode, application_order, course,
        daytime_evening, previous_qualification, prev_qualification_grade, nationality,
        mother_qualification, father_qualification, mother_occupation, father_occupation,
        admission_grade, displaced, special_needs, debtor,
        fees_up_to_date, gender, scholarship, age,
        international, units_approved, unemployment_rate, inflation_rate, gdp
    ]])

    # Normalize numerical features only
    input_data[:, [6, 12, 19, 21, 22, 23, 24]] = scaler.transform(input_data[:, [6, 12, 19, 21, 22, 23, 24]])

    prediction = model.predict(input_data)[0]
    pred_label = "🔴 Likely to Drop Out" if prediction == 1 else "🟢 Not Likely to Drop Out"
    st.subheader(f"🎯 Prediction Result: {pred_label}")
