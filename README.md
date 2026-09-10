# 🚗 Car Price Prediction

A machine learning web app that predicts the resale price of a used car based on details like brand, car name, year, kilometers driven, fuel type, seller type, transmission, and ownership history.

Built with a scikit-learn regression pipeline and served through an interactive **Streamlit** app.

## 🔗 Live Demo / Repo

[github.com/vikaskatariya30/Car-Price-Prediction-](https://github.com/vikaskatariya30/Car-Price-Prediction-)

## 📌 Features

- Predicts used car prices in real time based on user input
- Clean, interactive Streamlit UI — no page reloads, instant results
- Dropdowns/inputs for brand, car name, year, km driven, fuel type, seller type, transmission, and owner
- Trained `LinearRegression` model wrapped in an sklearn `Pipeline`
- Categorical features (name, seller_type, transmission, owner, company) encoded with `OneHotEncoder` via `ColumnTransformer`

## 🧠 How It Works

1. **Data**: `cleaned_car.csv` — a cleaned dataset of used car listings used to train the model.
2. **Model Training**: `modeltraining.ipynb` walks through data cleaning, feature encoding, and training a Linear Regression model.
3. **Model Artifact**: The trained pipeline is saved as `model.pkl`.
4. **Web App**: `app.py` is a Streamlit app that loads `model.pkl`, collects car details through input widgets, builds a single-row DataFrame, and displays the predicted price when you click **Predict Price**.

## 🛠️ Tech Stack

- **Python**, **scikit-learn**, **pandas** — data processing & model training
- **Streamlit** — interactive web app
- **Jupyter Notebook** — model development and experimentation

## 📂 Project Structure

```
Car-Price-Prediction-/
├── .gitignore           # Files/folders excluded from version control
├── LICENSE              # Apache-2.0 license
├── README.md            # Project documentation (this file)
├── app.py               # Streamlit app — loads model.pkl, collects inputs, shows prediction
├── cleaned_car.csv      # Cleaned used-car dataset used for training
├── model.pkl            # Trained LinearRegression pipeline (saved with pickle)
└── modeltraining.ipynb  # Notebook: data cleaning, encoding, and model training
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/vikaskatariya30/Car-Price-Prediction-.git
cd Car-Price-Prediction-
pip install streamlit pandas scikit-learn numpy
```

### Run the app

```bash
streamlit run app.py
```

This opens the app in your browser (typically `http://localhost:8501`). Select the brand, enter the car name, and fill in the remaining details, then click **Predict Price** to see the estimated resale value.

## 📈 Model

The model is a scikit-learn `Pipeline` combining:
- `ColumnTransformer` + `OneHotEncoder` for categorical features (car name, seller type, transmission, owner)
- `LinearRegression` as the estimator

Trained and evaluated in `modeltraining.ipynb`.

## 📄 License

This project is licensed under the **Apache-2.0 License** — see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vikas Katariya**
[GitHub](https://github.com/vikaskatariya30)