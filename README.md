#Cardiovascular Disease Detection App

#Overview
This is a web-based application for predicting the likelihood of cardiovascular disease based on input features provided by the user. The application is built using Python and Streamlit, and it implements a machine learning model trained with Random Forest Classifier, achieving an accuracy of 90%.

#Features
Predicts the probability of cardiovascular disease based on user input.
Provides a simple and intuitive user interface for entering input features.
Displays the prediction result along with the probability score.

#Installation
Clone the repository: git clone https://github.com/Aditya2874/CVD_Detection.git
Navigate to the project directory: cd cardiovascular-disease-detection-app
Install the required dependencies: pip install streamlit
Start the Streamlit server:
streamlit run app.py
Open your web browser and go to http://localhost:8501 to access the application.
Enter the input features (e.g., age, sex, blood pressure, cholesterol, etc.) in the provided fields.
Click the "Predict" button to generate the prediction. The application will display the prediction result.
#Model Training
The machine learning model used in this application was trained using a Random Forest Classifier. The dataset used for training the model is not provided in this repository. However, you can train your own model using the dataset of your choice and replace the existing model file (model.pkl) with your trained model.
