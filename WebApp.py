import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(
    r'E:\SEMESTER-4 2022-23\MiniProject2\Using_Streamlit\trained_model.sav', 'rb'))

# Creating a Function for prediction


def diabetes_prediction(input_data):

    # change input_data to a NumPy Array
    input_data_as_numpy_array = np.asarray(input_data)
    print("TYPE: ", type(input_data_as_numpy_array))

    # reshape the array as we are predicting for one instance as -- we are just using one datapoint not all 768 datapoints
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # standardize the input_data
    # std_data = scaler.transform(input_data_reshaped)
    # print(std_data)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:  # prediction is a list containing one     element..your output is the first element of this list
        return "Non-diabetic"
    elif prediction[0] == 1:
        return "Diabetic"


print("Executed")


def main():

    # Title
    st.title('Diabetes Prediction webApp')

   # Getting input from the user
   # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    Pregnancies = st.text_input("Pregnancies: ")
    Glucose = st.text_input("Glucose: ")
    BloodPressure = st.text_input("Blood Pressure: ")
    SkinThickness = st.text_input("Skin Thickness: ")
    Insulin = st.text_input("Insulin: ")
    BMI = st.text_input("BMI: ")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function: ")
    Age = st.text_input("Age: ")

   # Code for Prediction

    diagnosis = ''

  #  Creating Button for Prediction
    if st.button("Test for Diabetes"):
        diagnosis = diabetes_prediction(
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        

    st.success(diagnosis)



if __name__ == '__main__':
    main()


# streamlit run "e:\SEMESTER-4 2022-23\MiniProject2\Using_Streamlit\WebApp.py"