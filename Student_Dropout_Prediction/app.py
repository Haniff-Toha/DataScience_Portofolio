import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load model
model = joblib.load("Student_Dropout_Prediction/rf_model.joblib")

# Load scaler (assuming you've saved it, or redefine the same fit here)
scaler = joblib.load("Student_Dropout_Prediction/scaler.joblib")  # If not saved, manually define it as used before

st.title("🎓 Student Dropout Prediction App")

st.markdown("""
This app predicts whether a student is likely to **drop out** based on their academic and demographic background.
""")

# Define mappings for categorical values
marital_status_map = {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto Union", 6: "Legally Separated"}
application_mode_map = {1: "1st phase - general contingent", 2: "Ordinance No. 612/93", 5: "1st phase - special contingent (Azores Island)", 
                        7: "Holders of other higher courses", 10: "Ordinance No. 854-B/99", 15: "International student (bachelor)", 
                        16: "1st phase - special contingent (Madeira Island)", 17: "2nd phase - general contingent", 
                        18: "3rd phase - general contingent", 26: "Ordinance No. 533-A/99, item b2) (Different Plan)", 
                        27: "Ordinance No. 533-A/99, item b3 (Other Institution)", 39: "Over 23 years old", 42: "Transfer", 
                        43: "Change of course", 44: "Technological specialization diploma holders", 51: "Change of institution/course", 
                        53: "Short cycle diploma holders", 57: "Change of institution/course (International)"}
course_map = {33: "Biofuel Production Technologies", 171: "Animation and Multimedia Design", 8014: "Social Service (evening attendance)", 
              9003: "Agronomy", 9070: "Communication Design", 9085: "Veterinary Nursing", 9119: "Informatics Engineering", 
              9130: "Equinculture", 9147: "Management", 9238: "Social Service", 9254: "Tourism", 9500: "Nursing", 
              9556: "Oral Hygiene", 9670: "Advertising and Marketing Management", 9773: "Journalism and Communication", 
              9853: "Basic Education", 9991: "Management (evening attendance)"}
previous_qualification_map = {1: "Secondary education", 2: "Higher education - bachelor's degree", 3: "Higher education - degree", 
                              4: "Higher education - master's", 5: "Higher education - doctorate", 6: "Frequency of higher education", 
                              9: "12th year of schooling - not completed", 10: "11th year of schooling - not completed", 
                              12: "Other - 11th year of schooling", 14: "10th year of schooling", 15: "10th year of schooling - not completed", 
                              19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.", 38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.", 
                              39: "Technological specialization course", 40: "Higher education - degree (1st cycle)", 42: "Professional higher technical course", 
                              43: "Higher education - master (2nd cycle)"}
nationality_map = {1: "Portuguese", 2: "German", 6: "Spanish", 11: "Italian", 13: "Dutch", 14: "English", 17: "Lithuanian", 
                   21: "Angolan", 22: "Cape Verdean", 24: "Guinean", 25: "Mozambican", 26: "Santomean", 32: "Turkish", 
                   41: "Brazilian", 62: "Romanian", 100: "Moldova (Republic of)", 101: "Mexican", 103: "Ukrainian", 
                   105: "Russian", 108: "Cuban", 109: "Colombian"}
parents_qualification_map = {
    1: "Secondary Education - 12th Year of Schooling",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle",
    38: "Basic Education 2nd Cycle",
    39: "Technological specialization course",
    40: "Higher education - degree",
    44: "Higher Education - Doctorate"
}
occupation_map = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(blank)",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces personnel",
    112: "Directors of administrative and commercial services",
    114: "Hotel, catering, trade and other services directors",
    121: "Specialists in the physical sciences, mathematics, engineering and related techniques",
    122: "Health professionals",
    123: "Teachers",
    124: "Specialists in finance, accounting, administrative organization, public and commercial relations",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    135: "Information and communication technology technicians",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "Personal service workers",
    152: "Sellers",
    153: "Personal care workers and the like",
    154: "Protection and security services personnel",
    161: "Market-oriented farmers and skilled agricultural and animal production workers",
    163: "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    171: "Skilled construction workers and the like, except electricians",
    172: "Skilled workers in metallurgy, metalworking and similar",
    174: "Skilled workers in electricity and electronics",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    181: "Fixed plant and machine operators",
    182: "Assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants",
    195: "Street vendors (except food) and street service providers"
}


# ---- Input form ----
st.header("🔍 Student Information")

col1, col2 = st.columns(2)

with col1:
    marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()), format_func=lambda x: marital_status_map[x])
    application_mode = st.selectbox("Application Mode", list(application_mode_map.keys()), format_func=lambda x: application_mode_map[x])
    application_order = st.slider("Application Order", 0, 9, 1)
    course = st.selectbox("Course", list(course_map.keys()), format_func=lambda x: course_map[x])
    daytime_evening = st.selectbox("Attendance", [0, 1], format_func=lambda x: "Daytime" if x == 1 else "Evening")
    previous_qualification = st.selectbox("Previous Qualification", list(previous_qualification_map.keys()), format_func=lambda x: previous_qualification_map[x])
    nationality = st.selectbox("Nationality", list(nationality_map.keys()), format_func=lambda x: nationality_map[x])
    mother_qualification = st.selectbox("Mother's Qualification", list(parents_qualification_map.keys()), format_func=lambda x: parents_qualification_map[x])
    father_qualification = st.selectbox("Father's Qualification", list(parents_qualification_map.keys()), format_func=lambda x: parents_qualification_map[x])
    mother_occupation = st.selectbox("Mother's Occupation", list(occupation_map.keys()), format_func=lambda x: occupation_map[x])
    father_occupation = st.selectbox("Father's Occupation", list(occupation_map.keys()), format_func=lambda x: occupation_map[x])

with col2:
    prev_qualification_grade = st.number_input("Previous Qualification Grade (0-200)", min_value=0.0, max_value=200.0, step=1.0)
    admission_grade = st.number_input("Admission Grade (0-200)", min_value=0.0, max_value=200.0, step=1.0)
    displaced = st.radio("Displaced", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    special_needs = st.radio("Educational Special Needs", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    debtor = st.radio("Debtor", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    fees_up_to_date = st.radio("Tuition Fees Up-to-Date", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    gender = st.radio("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    scholarship = st.radio("Scholarship Holder", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    age = st.slider("Age at Enrollment", 16, 70, 20)
    international = st.radio("International Student", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
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

