import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data(file_path):
    """
    Load the stock data, preprocess it by parsing dates and scaling values.
    
    Args:
        file_path (str): Path to the stock data file.
        
    Returns:
        tuple: Scaled data as a NumPy array, scaler object for inverse scaling.
    """
    # Load data
    data = pd.read_csv(file_path, header=None)
    data.columns = ["TICKER", "PER", "DATE", "TIME", "OPEN", "HIGH", "LOW", "CLOSE", "VOL", "OPENINT"]

    # Parse dates with error handling
    try:
        data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d', errors='coerce')
    except Exception as e:
        print(f"Date parsing error: {e}")
    
    # Drop rows with invalid dates
    data = data.dropna(subset=['DATE'])
    data.set_index('DATE', inplace=True)
    
    # Selecting necessary columns
    data = data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']]
    
    # Scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    return scaled_data, scaler

def split_data(data, sequence_length=60):
    """
    Split data into sequences for LSTM input.
    
    Args:
        data (numpy.ndarray): Scaled stock data.
        sequence_length (int): Length of the sequence for LSTM input.
        
    Returns:
        tuple: Arrays of X (features) and y (target values).
    """
    X, y = [], []
    for i in range(sequence_length, len(data)):
        X.append(data[i-sequence_length:i])
        y.append(data[i, 3])  # Predicting 'CLOSE' price
    return np.array(X), np.array(y)
