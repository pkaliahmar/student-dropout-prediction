import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Load model and supporting files
# --------------------------------------------------

model = joblib.load("student_dropout_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")
default_values = joblib.load("default_values.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Dropout Risk Predictor",
    page_icon="🎓",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎓 Student Dropout Risk Predictor")

st.write(
    "Enter student information below to estimate the probability "
    "of dropout and identify the student's risk category."
)


# --------------------------------------------------
# Student input
# --------------------------------------------------

st.subheader("Student Information")

age = st.number_input(
    "Age at Enrollment",
    min_value=17,
    max_value=70,
    value=20
)

admission_grade = st.number_input(
    "Admission Grade",
    min_value=0.0,
    max_value=200.0,
    value=130.0
)

first_sem_approved = st.number_input(
    "1st Semester Approved Courses",
    min_value=0,
    max_value=30,
    value=5
)

first_sem_grade = st.number_input(
    "1st Semester Grade",
    min_value=0.0,
    max_value=20.0,
    value=12.0
)

scholarship = st.selectbox(
    "Scholarship Holder",
    ["No", "Yes"]
)

tuition = st.selectbox(
    "Tuition Fees Up To Date",
    ["No", "Yes"]
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Dropout Risk"):

    # Start with typical values from the training data
    student = default_values.copy()

    # Replace selected values with user input
    student["Age at enrollment"] = age
    student["Admission grade"] = admission_grade
    student["Curricular units 1st sem (approved)"] = first_sem_approved
    student["Curricular units 1st sem (grade)"] = first_sem_grade

    student["Scholarship holder_1"] = 1 if scholarship == "Yes" else 0
    student["Tuition fees up to date_1"] = 1 if tuition == "Yes" else 0

    # Ensure exact feature order
    student = student[feature_columns]

    # Convert to DataFrame
    student_df = pd.DataFrame([student])

    # Prediction
    prediction = model.predict(student_df)[0]

    # Dropout probability
    probability = model.predict_proba(student_df)[0][1]

    # Risk category
    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.60:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    # --------------------------------------------------
    # Display results
    # --------------------------------------------------

    st.subheader("Prediction Result")

    st.metric(
        "Dropout Probability",
        f"{probability:.2%}"
    )

    if prediction == 1:
        st.error("Prediction: At Risk of Dropout")
    else:
        st.success("Prediction: Not At Risk of Dropout")

    st.info(f"Risk Category: {risk}")
