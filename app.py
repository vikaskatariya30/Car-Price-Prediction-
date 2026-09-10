import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))


st.title('Car Price Predictor')

brand=st.selectbox('Select Brand', ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Ford', 'Mahindra', 'Tata', 'Renault', 'Volkswagen', 'Skoda'])
car_name=st.text_input('Enter car name')
year=st.selectbox('Select Year', [i for i in range(2024, 1982, -1)])
km_driven=st.number_input('Enter km driven', min_value=0, step=10000000)
fuel_type=st.selectbox('Select Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
seller_type=st.selectbox('Select Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])
transmission=st.selectbox('Select Transmission Type', ['Manual', 'Automatic'])
owner=st.selectbox('Select Owner Type', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

data=pd.DataFrame([[car_name, year, km_driven, fuel_type, seller_type, transmission, owner, brand]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'company'])

if st.button('Predict Price'):
    prediction=model.predict(data)
    st.write(f'Predicted Price: {prediction[0]}')

