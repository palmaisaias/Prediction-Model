import numpy as np
from datetime import timedelta
import pandas as pd

def make_predictions(model, data, days_ahead=5):
    """
    Generate predictions for the next specified number of days.
    
    Args:
        model: Trained LSTM model.
        data (numpy.ndarray): Scaled data (last 60 days) for input.
        days_ahead (int): Number of future days to predict.
        
    Returns:
        list: Predicted closing prices for the specified number of days.
    """
    predictions = []
    input_data = data[-60:].reshape(1, 60, data.shape[1])  # Use last 60 days as input

    for _ in range(days_ahead):
        pred_price = model.predict(input_data)[0, 0]
        predictions.append(pred_price)
        
        # Reshape pred_price to match the feature dimension (5)
        pred_price_reshaped = np.array([[[0, 0, 0, pred_price, 0]]])  # Matching feature size (5)

        # Update input_data with the new prediction
        input_data = np.append(input_data[:, 1:, :], pred_price_reshaped, axis=1)

    return predictions

def make_recommendation(predictions, scaler):
    """
    Generate a buy/sell recommendation based on predicted prices.
    
    Args:
        predictions (list): Predicted closing prices for the upcoming days.
        scaler: Scaler used for inverse transforming predictions.
        
    Returns:
        tuple: (recommendation (str), sell_date (datetime.date) or None)
    """
    # Inverse scale predictions to get actual price values
    predictions_unscaled = scaler.inverse_transform([[0, 0, 0, pred, 0] for pred in predictions])[:, 3]

    # Determine buy/sell signals based on expected price increase
    current_price = predictions_unscaled[0]
    max_price = max(predictions_unscaled)
    buy_signal = max_price / current_price > 1.02  # Arbitrary 2% increase threshold

    if buy_signal:
        sell_day = predictions_unscaled.tolist().index(max_price)
        sell_date = (pd.Timestamp.now() + timedelta(days=sell_day)).date()
        return "Buy", sell_date
    else:
        return "Do not buy", None
