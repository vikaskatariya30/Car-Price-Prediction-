from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, template_folder='template')
car=pd.read_csv('cleaned_car.csv')

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_model = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    km_driven = sorted(car['km_driven'].unique())
    fuel_type = sorted(car['fuel'].unique())
    seller_type = sorted(car['seller_type'].unique())
    transmissions = sorted(car['transmission'].unique())
    owners = sorted(car['owner'].unique())
    return render_template('main.html', companies=companies, car_model=car_model, year=year, km_driven=km_driven,
                           fuel_type=fuel_type, seller_type=seller_type, transmissions=transmissions, owners=owners)

@app.route('/predict', methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    km_driven=int(request.form.get('km_driven'))
    fuel_type=request.form.get('fuel_type')
    seller_type=request.form.get('seller_type')
    transmissions=request.form.get('transmissions')
    owners=request.form.get('owners')

    prediction=model.predict(pd.DataFrame([[car_model, year, km_driven, fuel_type, seller_type, transmissions, owners, company]], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'company']))

    return str(np.round(prediction[0], 2))
if __name__ == '__main__':
    app.run(debug=True)