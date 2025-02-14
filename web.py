import os
import pickle  # pre-trained model loading
import streamlit as st  # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout="wide",
                   page_icon="🤒")

# getting the working directory of main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f"{working_dir}\saved_models\diabetes_model.sav", "rb"))
heart_model = pickle.load(open(f"{working_dir}\saved_models\heart_model.sav", "rb"))
parkinsons_model = pickle.load(open(f"{working_dir}\saved_models\parkinsons_model.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    selected=option_menu("Prediction of Disease Outbreak System",
                         ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
                         menu_icon="hospital-fill", icons=["activity", "heart", "person"], default_index=0)
    
# Diabetes prediction page
if selected == "Diabetes Prediction":
    # page title
    st.title("Diabetes Prediction using ML")

    # getting user input
    col1, col2, col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input("Number of pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        bloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        skinThickness = st.text_input("Skin Thickness Value")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        bmi = st.text_input("BMI Value")
    with col1:
        diabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        age = st.text_input("Age of the person")

# Heart disease prediction page
elif selected == "Heart Disease Prediction":
    # page title
    st.title("Heart Disease Prediction using ML")

    # getting user input
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Gender (1 = Male, 0 = Female)")
    with col3:
        cp = st.text_input("Chest pain type (categorical: 0–3)")
    with col1:
        trestbps = st.text_input("Resting blood pressure")
    with col2:
        chol = st.text_input("Serum cholesterol")
    with col3:
        fbs = st.text_input("Fasting blood sugar > 120 mg/dL (1 = True, 0 = False)")
    with col1:
        restecg = st.text_input("Resting ECG results (categorical: 0–2)")
    with col2:
        thalach = st.text_input("Maximum heart-rate achieved")
    with col3:
        exang = st.text_input("Exercise-induced angina (1 = Yes, 0 = No)")
    with col1:
        oldpeak = st.text_input("ST depr (exercise to rest)")
    with col2:
        slope = st.text_input("Slope of peak exercise ST (categorical: 0–2)")
    with col3:
        ca = st.text_input("No. major vessels colored")
    with col1:
        thal = st.text_input("Thalassemia (categorical: 1–3)")

# Parkinson's disease prediction page
else:
    # page title
    st.title("Parkinson's Prediction using ML")

    # getting user input
    col1, col2, col3, col4 = st.columns(4)
    inputs = [
        ("mdvp_fo", "Avg. fundamental frequency"),
        ("mdvp_fhi", "Max. fundamental frequency"),
        ("mdvp_flo", "Min. fundamental frequency"),
        ("mdvp_jitter_perc", "Jitter %"),
        ("mdvp_jitter_abs", "Jitter (absolute)"),
        ("mdvp_rap", "RAP"),
        ("mdvp_ppq", "PPQ"),
        ("jitter_ddp", "Jitter DDP"),
        ("mdvp_shimmer", "Shimmer"),
        ("mdvp_shimmer_db", "Shimmer dB"),
        ("shimmer_apq3", "APQ3"),
        ("shimmer_apq5", "APQ5"),
        ("mdvp_apq", "APQ"),
        ("shimmer_dda", "Shimmer DDA based on APQ3"),
        ("nhr", "NHR"),
        ("hnr", "HNR"),
        ("rpde", "RPDE"),
        ("dfa", "DFA"),
        ("d2", "D2"),
        ("spread1", "Spread1"),
        ("spread2", "Spread2"),
        ("ppe", "PPE")
    ]

    cols = [col1, col2, col3, col4]

    variables = {}
    for i, (var_name, desc) in enumerate(inputs):
        with cols[i % 4]:
            variables[var_name] = st.text_input(desc)

# Code for diabetes prediction
if selected == "Diabetes Prediction" and st.button("Diabetes Test Result"):
    user_input = [pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]

    # Check for empty strings in user inputs
    if "" in user_input:
        st.warning("Please fill out all the inputs")

    else:
        user_input = [float(x) for x in user_input]
        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            st.error("The person is diabetic")
        else:
            st.success("The person is not diabetic")

# Code for heart disease prediction
elif selected == "Heart Disease Prediction" and st.button("Heart Disease Test Result"):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    # Check for empty strings in user inputs
    if "" in user_input:
        st.warning("Please fill out all the inputs")

    else:
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            st.error("The person has heart disease")
        else:
            st.success("The person does not have heart disease")

# Code for parkinson's disease prediction
elif selected == "Parkinson's Prediction" and st.button("Parkinson's Disease Test Result"):

    # Check for empty strings in user inputs
    if "" in variables.values():
        st.warning("Please fill out all the inputs")

    else:
        user_input = [float(x) for x in variables.values()]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            st.error("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")