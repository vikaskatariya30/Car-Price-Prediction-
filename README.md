# Car Price Prediction 🚗

A machine learning web application that predicts the resale price of a used car based on details like company, model, manufacturing year, kilometers driven, fuel type, seller type, transmission, and ownership history. Built with **Flask** and **scikit-learn**.

## Demo

The app presents a simple form where a user selects a car's company, model, year, and other details, then returns a predicted resale price instantly.

## Features

- Predicts used car prices using a trained regression model
- Clean, form-based UI (HTML/CSS)
- Dropdowns dynamically populated from the dataset (companies, models, years, fuel types, etc.)
- Lightweight Flask backend serving predictions in real time

## Tech Stack

- **Backend:** Python, Flask
- **ML/Data:** pandas, NumPy, scikit-learn
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Model persistence:** Pickle

## Project Structure

```
Car-Price-Prediction-/
├── static/css/          # Stylesheets
├── template/             # HTML templates (main.html)
├── app.py                # Flask application
├── cleaned_car.csv       # Cleaned dataset used to populate form options
├── model.pkl             # Trained regression model (pickled)
├── modeltraining.ipynb   # Notebook: data cleaning, EDA, model training
├── LICENSE
└── README.md
```

## How It Works

1. `app.py` loads `cleaned_car.csv` and the pre-trained `model.pkl`.
2. On the home page (`/`), dropdown options (company, model, year, km driven, fuel type, seller type, transmission, owner) are generated from the unique values in the dataset.
3. When the form is submitted (`/predict`), the selected inputs are passed to the trained model as a DataFrame.
4. The model returns a predicted price, which is displayed to the user.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/vikaskatariya30/Car-Price-Prediction-.git
cd Car-Price-Prediction-

# Install dependencies
pip install flask pandas numpy scikit-learn
```

### Run the app

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## Model Training

The model was trained in `modeltraining.ipynb`, which covers:

- Data cleaning and preprocessing of raw car listing data
- Encoding categorical features (company, model, fuel type, seller type, transmission, owner)
- Training a regression model to predict `Price` from the remaining features
- Exporting the trained pipeline as `model.pkl`

## Input Features

| Feature | Description |
|---|---|
| Company | Car manufacturer (e.g., Maruti, Hyundai) |
| Name | Specific car model |
| Year | Manufacturing year |
| Kms Driven | Total kilometers driven |
| Fuel Type | Petrol / Diesel / CNG / etc. |
| Seller Type | Individual / Dealer |
| Transmission | Manual / Automatic |
| Owner | Number of previous owners |

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

## Author

**Vikas Katariya**
GitHub: [@vikaskatariya30](https://github.com/vikaskatariya30)