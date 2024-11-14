from src.data_preprocessing import load_and_preprocess_data, split_data
from src.model_training import build_model, train_model, save_model
from src.prediction import make_predictions, make_recommendation
from src.utils import plot_predictions, inverse_scale_data

# File path
# Some files are so evident of loss that it takes the training model no more than 26 epocs 
# to decipher that the stock will take a loss
file_path = "data/mara.us.txt"

# Step 1: Load and preprocess data
scaled_data, scaler = load_and_preprocess_data(file_path)
X, y = split_data(scaled_data)

# Step 2: Split data into training and validation sets
split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_val, y_val = X[split:], y[split:]

# Step 3: Build and train the model
model = build_model((X_train.shape[1], X_train.shape[2]))
model = train_model(model, X_train, y_train, X_val, y_val)

# Optionally save the model
save_model(model, "models/lstm_model.h5")

# Step 4: Make predictions for the next 5 days
days_ahead = 5
predicted_prices = make_predictions(model, scaled_data, days_ahead)

# Convert predictions back to original scale
predicted_prices_unscaled = inverse_scale_data(
    [[0, 0, 0, pred, 0] for pred in predicted_prices], scaler)[:, 3]

# Step 5: Generate a recommendation
recommendation, sell_date = make_recommendation(predicted_prices, scaler)
print(f"Recommendation: {recommendation}")
if recommendation == "Buy":
    print(f"Recommended Sell Date: {sell_date}")

# Optional: Plot the predictions
import pandas as pd
dates = pd.date_range(start=pd.Timestamp.now(), periods=days_ahead).date
plot_predictions(dates, [None] * days_ahead, predicted_prices_unscaled)
