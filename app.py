import streamlit as st
import pandas as pd
import joblib

# Memuat model
model = joblib.load('model.pkl')

# Definisikan fungsi untuk prediksi
def predict(bodyfat, age, weight, height):
    data = {'BodyFat': [bodyfat], 'Age': [age], 'Weight': [weight], 'Height': [height]}
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return prediction[0]

# Membuat aplikasi Streamlit
st.title('Body Fat Prediction App')

bodyfat = st.number_input('Body Fat', min_value=0.0, max_value=100.0, value=20.0)
age = st.number_input('Age', min_value=0, max_value=100, value=25)
weight = st.number_input('Weight', min_value=0.0, max_value=500.0, value=70.0)
height = st.number_input('Height', min_value=0.0, max_value=250.0, value=170.0)

if st.button('Predict'):
    result = predict(bodyfat, age, weight, height)
    st.success(f'The predicted body fat is {result:.2f}')
