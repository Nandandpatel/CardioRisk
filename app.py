import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Cardiovascular Disease Prediction",
                   layout="wide",
                   page_icon="❤️")

# Function to load the model
def load_model(model_path):
    return pickle.load(open(model_path, 'rb'))

# Load the heart disease prediction model
model_path = os.path.join(os.path.dirname(__file__), 'saved_models', 'heart_disease_model.sav')
heart_disease_model = load_model(model_path)

# Function to preprocess input features
def preprocess_input(features):
    # Map sex to binary
    features[1] = 1 if features[1] == 'Male' else 0
    
    # Map chest pain types to numerical values
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    features[2] = cp_mapping[features[2]]
    
    # Map fasting blood sugar to binary
    features[5] = 1 if features[5] == 'True' else 0
    
    # Map restecg to numerical values
    restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Probable or Definite Left Ventricular Hypertrophy': 2}
    features[6] = restecg_mapping[features[6]]
    
    # Map exercise induced angina to binary
    features[8] = 1 if features[8] == 'Yes' else 0
    
    # Map slope of the peak exercise ST segment to numerical values
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    features[10] = slope_mapping[features[10]]
    
    # Map thal to numerical values
    thal_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
    features[12] = thal_mapping[features[12]]
    
    return [float(x) for x in features]

# Function to make predictions
def make_prediction(model, features):
    prediction = model.predict([features])
    return prediction[0]

# Function to display prediction result
def display_result(prediction):
    if prediction == 1:
        return 'Positive for cardiovascular disease'
    else:
        return 'Negative for cardiovascular disease'

# Sidebar for navigation
with st.sidebar:
    st.title('Navigation')
    selected = option_menu('Cardiovascular Disease Prediction',
                           ['Home', 'Prediction'],
                           menu_icon='heart',
                           default_index=0)

# Main content
if selected == 'Home':
    st.title('Welcome to Cardiovascular Disease Prediction App')
    st.write('This app predicts the likelihood of cardiovascular disease based on various factors.')

    st.subheader('About Cardiovascular Disease')
    st.write('''
Cardiovascular disease (CVD) refers to a group of conditions that affect the heart and blood vessels. These conditions include coronary artery disease, heart failure, stroke, and other vascular diseases of the arteries and veins. CVD is one of the leading causes of death worldwide.''')

    st.subheader('Risk Factors')
    st.write('''
1. **age**(8%): This represents the age of the individual in years. It tells us how old the person is.

2. **sex**(0.3%): This indicates the gender of the individual. A value of 1 typically represents male, while 0 represents female.

3. **chest_pain**(20%): This describes the type of chest pain the individual experiences. It can be categorized into four types: typical angina (a type of chest pain related to heart), atypical angina (different from typical angina), non-anginal pain (chest pain not related to heart), and asymptomatic (no chest pain).

4. **blood_pressure**(15%): This is the resting blood pressure of the individual when admitted to the hospital, measured in millimeters of mercury (mm Hg). It tells us how much pressure the blood is exerting on the walls of the arteries.

5. **serum_cholestoral**(10%): This is the level of cholesterol in the blood, measured in milligrams per deciliter (mg/dl). Cholesterol is a type of fat found in the blood, and high levels can increase the risk of heart disease.

6. **fasting_blood_sugar**(0.2%): This indicates whether the fasting blood sugar level of the individual is greater than 120 mg/dl. High fasting blood sugar levels can indicate diabetes, which is a risk factor for heart disease.

7. **electrocardiographic**(1%): This describes the results of the resting electrocardiogram (ECG or EKG), which measures the electrical activity of the heart. It tells us if there are any abnormalities in the heart's electrical rhythm.

8. **max_heart_rate**(30%): This represents the maximum heart rate achieved by the individual during some form of activity. It gives an indication of the heart's capacity to respond to stress or exercise.

9. **induced_angina**(0.5%): This indicates whether the individual experiences angina (chest pain) induced by exercise. It tells us if physical activity triggers chest pain in the person.

10. **ST_depression**(6%): This measures the amount of depression in the ST segment of the ECG induced by exercise relative to rest. It indicates how much the heart's electrical activity changes during exercise.

11. **slope**(5%): This describes the slope of the peak exercise ST segment on the ECG. It tells us about the pattern of change in the heart's electrical activity during exercise.

12. **no_of_vessels**(3%): This represents the number of major blood vessels (0-3) colored by a special dye during a fluoroscopy procedure. It indicates any blockages or narrowing in the blood vessels of the heart.

13. **thal**(2%): This describes the results of a thallium stress test, which is used to diagnose heart conditions. It tells us about the blood flow to the heart muscle.

14. **diagnosis**: This is the target variable that we want to predict. It indicates the diagnosis of heart disease based on angiographic results, with values representing the severity of narrowing in the coronary arteries.''')

elif selected == 'Prediction':
    st.title('Cardiovascular Disease Prediction')

    # Input fields
    st.subheader('Enter Patient Details')
    age = st.number_input('Age', min_value=0, max_value=120, step=1)
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=250, step=1)
    chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0, max_value=700, step=1)
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, step=1)

    # Validate input values
    if age <= 0 or trestbps <= 0 or chol <= 0 or thalach <= 0:
        st.error("Please enter valid values for Age, Resting Blood Pressure, Serum Cholesterol, and Maximum Heart Rate Achieved.")
    else:
        sex = st.radio('Sex', ['Male', 'Female'])
        cp = st.selectbox('Chest Pain Types', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['False', 'True'])
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T Wave Abnormality', 'Probable or Definite Left Ventricular Hypertrophy'])
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, step=0.1)
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', ['0', '1', '2', '3'])
        thal = st.selectbox('Thal', ['Normal', 'Fixed Defect', 'Reversible Defect'])

        # Make prediction
        if st.button('Predict'):
            features = preprocess_input([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
            prediction = make_prediction(heart_disease_model, features)
            result = display_result(prediction)

            # Display prediction result with styling
            st.subheader('Prediction Result')
            if prediction == 1:
                st.error("The person is predicted to have heart disease")
            else:
                st.success("The person is predicted to not have heart disease")

st.sidebar.title('About')
st.sidebar.info('This app is created by Group 12.')
