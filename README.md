# Car Price Prediction

This project is a web application for predicting car prices based on various features. The application is built using Flask for the backend, with a machine learning model based on Linear Regression for the predictions. The project is deployed on Heroku.

## Features

- Predict car prices based on company, model, year, fuel type, and kilometers driven.
- User-friendly web interface for inputting car details and viewing predictions.

## Main Libraries Used

- **Flask**: For web development and creating the server-side application.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For machine learning model (Linear Regression).
- **Joblib**: For model serialization and deserialization.
- **Gunicorn**: For deploying the Flask application on Heroku.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/car-price-prediction.git
  
2. Change to the project directory:
   ```sh
   cd car-price-prediction
   
3. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
4. Install the required libraries:
    ```sh
    pip install -r requirements.txt

## Usage 

1. Run the Flask application:
   ```sh
     flask run
2. Open your browser and go to **http://127.0.0.1:5000/** to access the application.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

