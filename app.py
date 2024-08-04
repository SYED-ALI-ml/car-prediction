from flask import Flask, render_template, request
import pandas as pd 
import pickle
import numpy as np 

app = Flask(__name__)
car = pd.read_csv("cleared_Car.csv")
model = pickle.load(open("LinearRegression.pkl", 'rb'))
@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = car.groupby('company')['name'].apply(list).to_dict()
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_models=car_models, 
                           years=years, fuel_types=fuel_types)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    # Creating the DataFrame with the correct data types
    input_df = pd.DataFrame(data=[[car_model, company, year, kms_driven, fuel_type]], 
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    # Debugging: Check the input data
    print("Input DataFrame:")
    print(input_df)

    try:
        # Perform prediction
        prediction = model.predict(input_df)
        print("Prediction:", prediction)
        return str(np.round(prediction[0]))
    except Exception as e:
        print("Error during prediction:", e)
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
