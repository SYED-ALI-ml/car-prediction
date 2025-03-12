# 🚗 Car Price Prediction

Welcome to the **Car Price Prediction** project! This web application allows users to estimate the price of a used car based on various features. It is built using **Flask** and **Machine Learning**, providing accurate price predictions in a simple and intuitive interface.

## 🌟 Features

- 🔢 **Predict Car Prices** - Enter details like company, model, year, fuel type, and kilometers driven to get an estimated price.
- 🎨 **User-Friendly Interface** - A sleek and easy-to-use web form.
- 🚀 **Fast and Efficient** - Uses a trained **Linear Regression** model for quick predictions.

## 🛠️ Technologies Used

- **Flask** - Web framework for building the application.
- **Pandas** - Data manipulation and preprocessing.
- **Scikit-learn** - Machine learning library for model training.
- **Joblib** - Model serialization for deployment.
- **Gunicorn** - WSGI HTTP server for running Flask applications in production.

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SYED-ALI-ml/car-prediction.git
   cd car-prediction
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open your web browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

3. **Predict car prices:**

   Fill in the details and submit the form to get an estimated price.

## 📊 Dataset

The model is trained on `cleared_Car.csv`, which includes:
- Company
- Model
- Year
- Fuel Type
- Kilometers Driven

📌 The dataset is preprocessed to improve prediction accuracy.

## 🎯 Model Training

- The **Linear Regression** model is trained using the dataset.
- Training is documented in `car_prediction.ipynb`.
- The trained model is saved as `LinearRegression.pkl` for deployment.

## 🌍 Deployment

The application is configured for **Heroku** deployment using a `Procfile`. You can deploy it with:

```bash
heroku create your-app-name
heroku git:remote -a your-app-name
heroku buildpacks:add heroku/python
heroku push origin main
heroku open
```

## 💡 Future Improvements

- ✅ Support for more car attributes (e.g., transmission type, owner history)
- ✅ Integration with a database for user history
- ✅ Enhanced model accuracy with more advanced algorithms

## 🤝 Contributing

Feel free to contribute by submitting issues or pull requests!

## 📜 License

This project is open-source and available under the **MIT License**.

🚀 **Happy Predicting!** 🎉

