import numpy as np
import matplotlib.pyplot as plt

def scale_data(data, scaler):
    """
    Scales the data using the provided scaler.
    
    Args:
        data (numpy.ndarray): The data to be scaled.
        scaler: The scaler object (e.g., MinMaxScaler).
        
    Returns:
        numpy.ndarray: Scaled data.
    """
    return scaler.transform(data)

def inverse_scale_data(scaled_data, scaler):
    """
    Inversely scales the data back to original values using the provided scaler.
    
    Args:
        scaled_data (numpy.ndarray): Scaled data to be inversely transformed.
        scaler: The scaler object (e.g., MinMaxScaler).
        
    Returns:
        numpy.ndarray: Data in original scale.
    """
    return scaler.inverse_transform(scaled_data)

def plot_predictions(dates, actual_prices, predicted_prices):
    """
    Plots the actual and predicted stock prices for comparison.
    
    Args:
        dates (list): Dates for the x-axis.
        actual_prices (list): Actual closing prices.
        predicted_prices (list): Predicted closing prices.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(dates, actual_prices, color="blue", label="Actual Price")
    plt.plot(dates, predicted_prices, color="red", linestyle="--", label="Predicted Price")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title("Stock Price Prediction")
    plt.legend()
    plt.show()
