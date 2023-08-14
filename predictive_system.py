import numpy as np
import pickle


# Loading the saved model
loaded_model = pickle.load(open(r'E:\SEMESTER-4 2022-23\MiniProject2\Using_Streamlit\trained_model.sav', 'rb'))
# Instead of r u can change all \ to /

# input_data = (4,110,92,0,0,37.6,0.191,30) # Non-Diabetic
input_data = (5,166,72,19,175,25.8,0.587,51) # Diabetic

# change input_data to a NumPy Array
input_data_as_numpy_array = np.asarray(input_data)
print("TYPE: ", type(input_data_as_numpy_array))

# reshape the array as we are predicting for one instance as -- we are just using one datapoint not all 768 datapoints
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input_data
# std_data = scaler.transform(input_data_reshaped)
# print(std_data)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0: #prediction is a list containing one element..your output is the first element of this list
  print("Non-diabetic")
elif prediction[0]==1:
  print("Diabetic")

print("Executed")