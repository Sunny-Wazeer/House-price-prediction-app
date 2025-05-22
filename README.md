
# California Housing Price Prediction

This project predicts California housing prices using the California Housing Dataset and a machine learning model (XGBoost Regressor). It includes data visualization, training/testing performance evaluation, and model persistence using pickle.

## Features Used
- Median Income (`MedInc`)
- House Age (`HouseAge`)
- Average Rooms (`AveRooms`)
- Average Bedrooms (`AveBedrms`)
- Population (`Population`)
- Average Occupants (`AveOccup`)
- Latitude (`Latitude`)
- Longitude (`Longitude`)

## Model
- **Model Used**: XGBoost Regressor
- **Metrics**:
  - R-squared score
  - Mean Absolute Error

## Example Prediction
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

## Requirements
- Python
- pandas, numpy, seaborn, matplotlib, scikit-learn, xgboost

## Running the Project
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the script:
```bash
python main.py
```
