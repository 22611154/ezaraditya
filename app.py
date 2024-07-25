import streamlit as st
import pandas as pd
import joblib

# Memuat model
model = joblib.load('model.pkl')

# Definisikan fungsi untuk prediksi
def predict(input_data):
    df = pd.DataFrame(input_data, index=[0])
    st.write("Input Data for Prediction:")
    st.write(df)
    prediction = model.predict(df)
    return prediction[0]

# Membuat aplikasi Streamlit
st.title('Body Fat Prediction App')

# Membuat form input
with st.form("prediction_form"):
    density = st.number_input('Density', min_value=0.0, max_value=2.0, value=1.05)
    age = st.number_input('Age', min_value=0, max_value=100, value=25)
    weight = st.number_input('Weight (in pounds)', min_value=0.0, max_value=500.0, value=150.0)
    height = st.number_input('Height (in inches)', min_value=0.0, max_value=100.0, value=65.0)
    neck = st.number_input('Neck Circumference (in cm)', min_value=0.0, max_value=100.0, value=40.0)
    chest = st.number_input('Chest Circumference (in cm)', min_value=0.0, max_value=200.0, value=100.0)
    abdomen = st.number_input('Abdomen Circumference (in cm)', min_value=0.0, max_value=200.0, value=85.0)
    hip = st.number_input('Hip Circumference (in cm)', min_value=0.0, max_value=200.0, value=95.0)
    thigh = st.number_input('Thigh Circumference (in cm)', min_value=0.0, max_value=100.0, value=60.0)
    knee = st.number_input('Knee Circumference (in cm)', min_value=0.0, max_value=100.0, value=40.0)
    ankle = st.number_input('Ankle Circumference (in cm)', min_value=0.0, max_value=100.0, value=25.0)
    biceps = st.number_input('Biceps Circumference (in cm)', min_value=0.0, max_value=100.0, value=30.0)
    forearm = st.number_input('Forearm Circumference (in cm)', min_value=0.0, max_value=100.0, value=25.0)
    wrist = st.number_input('Wrist Circumference (in cm)', min_value=0.0, max_value=100.0, value=15.0)
    
    # Tombol submit
    submitted = st.form_submit_button("Predict")

if submitted:
    # Menyusun data input untuk prediksi
    input_data = {
        'Density': density,
        'Age': age,
        'Weight': weight,
        'Height': height,
        'Neck': neck,
        'Chest': chest,
        'Abdomen': abdomen,
        'Hip': hip,
        'Thigh': thigh,
        'Knee': knee,
        'Ankle': ankle,
        'Biceps': biceps,
        'Forearm': forearm,
        'Wrist': wrist
    }
    
    # Melakukan prediksi
    result = predict(input_data)
    
    # Menampilkan hasil prediksi
    st.success(f'The predicted body fat percentage is {result:.2f}')
