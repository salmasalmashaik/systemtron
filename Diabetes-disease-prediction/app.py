import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))




with st.sidebar:
    selected = option_menu('Diabetes Disease Prediction System',

                           ['Diabetes Prediction',
                            ],
                           menu_icon='hospital-fill',
                           icons=['activity'],
                           default_index=0)



if selected == 'Diabetes Prediction':

    
    st.title('Diabetes Prediction using ML')

    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',placeholder="range(1-10)")

    with col2:
        Glucose = st.text_input('Glucose Level',placeholder="range(1-200)")

    with col3:
        BloodPressure = st.text_input('Blood Pressure value',placeholder="range(1-150)")

    with col1:
        SkinThickness = st.text_input('Skin Thickness value',placeholder="range(1-50)")

    with col2:
        Insulin = st.text_input('Insulin Level',placeholder="range(1-250)")

    with col3:
        BMI = st.text_input('BMI value',placeholder="range(1.0-100.0)")

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',placeholder="range(0.1-1.0)")

    with col2:
        Age = st.text_input('Age of the Person',placeholder="range(1-100)")


    
    diab_diagnosis = ''



    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


