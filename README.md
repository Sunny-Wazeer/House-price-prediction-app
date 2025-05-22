
# 🏡 California Housing Price Prediction Web App

This project is a complete machine learning pipeline that predicts California housing prices using the **California Housing Dataset**. It includes:

- A **Jupyter Notebook** for data exploration, visualization, training and evaluation.
- A **Flask web app** for user interaction and house price prediction based on input features.

---

## 📁 Project Structure

```
├── app.py                  # Flask web application
├── model_training.ipynb    # Jupyter notebook for EDA and model training
├── house_price_model.pkl   # Trained XGBoost model (saved using pickle)
├── templates/
│   └── index.html          # Frontend HTML for user input
├── static/
│   └── style.css           # (Optional) styling file
├── requirements.txt        # Project dependencies
└── README.md               # Project description
```

---

## 📊 Dataset

- Dataset: **California Housing Dataset** (`sklearn.datasets.fetch_california_housing`)
- Target: `Median House Value`

---

## 🔍 Features Used

- `MedInc`: Median income
- `HouseAge`: Average house age in the block
- `AveRooms`: Average number of rooms
- `AveBedrms`: Average number of bedrooms
- `Population`: Block population
- `AveOccup`: Average occupancy
- `Latitude`: Geo-coordinate
- `Longitude`: Geo-coordinate

---

## 🧠 Model

- **Algorithm**: XGBoost Regressor
- **Training Environment**: Jupyter Notebook (`model_training.ipynb`)
- **Metrics**:
  - R² (R-squared)
  - MAE (Mean Absolute Error)

The model is serialized with `pickle` as `house_price_model.pkl` for deployment in the Flask web app.

---

## 🌐 Web Application

### 🖥️ How it works:

- Users input house features via a web form.
- The app loads the pre-trained model.
- The model predicts and displays the median house price.

---

## 🚀 How to Run the Project

### 1. Clone the repository and navigate to the folder:
```bash
git clone https://github.com/YourUsername/California-House-Price-App.git
cd California-House-Price-App
```

### 2. Create virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask App:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🧪 Example Prediction (From Notebook)

```python
new_house = pd.DataFrame({
    'MedInc': [6.0],
    'HouseAge': [30],
    'AveRooms': [5.5],
    'AveBedrms': [1.1],
    'Population': [1000],
    'AveOccup': [3.0],
    'Latitude': [34.05],
    'Longitude': [-118.25]
})
predicted_price = model.predict(new_house)
print(f"Predicted Median House Value: ${predicted_price[0] * 100000:.2f}")
```

---

## 📎 Requirements

- Python 3.x
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- xgboost
- pickle

---

## ✍️ Author

Developed by **[Sunny Wazeer]** — for learning and internship purposes.

