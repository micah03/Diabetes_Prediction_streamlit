# Diabetes_Prediction_streamlit_Web_App
## Mini-Project in Semester 4

This is a Python application for predicting whether an individual is diabetic or non-diabetic based on input features such as Pregnancies, Glucose level, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age. The application uses a machine learning model trained on a diabetes dataset.

## Prerequisites
Before running this application, make sure you have the required libraries installed. You can install them using pip:

```pip install numpy pandas scikit-learn matplotlib seaborn streamlit```


## Usage
1. Clone this repository or download the code to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the code.

3. Run the app by executing the following command in shell:

```streamlit run WebApp.py```

This will open a local web server, and you can access the web app in your browser.

4. Enter the values for the following input features:

* `Pregnancies`
* `Glucose`
* `Blood Pressure`
* `Skin Thickness`
* `Insulin`
* `BMI (Body Mass Index)`
* `Diabetes Pedigree Function`
* `Age`

5. Click the ```Test for Diabetes``` button to make a prediction.

6. The application will display whether the individual is `Diabetic` or `Non-diabetic` based on the input features.

## Working

* The code uses a trained machine learning model to predict diabetes based on the input features provided by the user.

* The model used is a Random Forest Classifier, which is a supervised learning algorithm.

* The user input is processed, standardized, and fed into the model to make a prediction.

* The result of the prediction is displayed on the web app.

* The trained Random Forest Classifier model is saved using the Pickle library (trained_model.sav) and loaded when making predictions in the web app.

## About the Code
* The code uses the `streamlit` library to create a user-friendly web interface for diabetes prediction.

* It also uses libraries such as NumPy `(numpy)`, Pandas `(pandas)`, Scikit-Learn `(sklearn)`, Matplotlib `(matplotlib)`, and Seaborn `(seaborn)` for data processing, modeling, and visualization.

* You can further improve the model's accuracy by using a larger and more diverse dataset for training.

* This code is intended for educational and demonstrative purposes.

Feel free to explore, modify, and use this code for your own projects or as a starting point for building web applications with machine learning capabilities. :)
