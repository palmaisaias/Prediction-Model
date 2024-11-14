import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

def build_model(input_shape):
    """
    Builds and compiles an LSTM model for stock price prediction.
    
    Args:
        input_shape (tuple): Shape of the input data (sequence_length, number of features).
        
    Returns:
        model: Compiled LSTM model.
    """
    model = Sequential([
        LSTM(units=50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(units=50, return_sequences=True),
        Dropout(0.2),
        LSTM(units=50),
        Dropout(0.2),
        Dense(units=1)  # Output layer for price prediction
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(model, X_train, y_train, X_val, y_val):
    """
    Trains the LSTM model on the provided training data.
    
    Args:
        model: Compiled LSTM model.
        X_train (numpy.ndarray): Training features.
        y_train (numpy.ndarray): Training targets.
        X_val (numpy.ndarray): Validation features.
        y_val (numpy.ndarray): Validation targets.
        
    Returns:
        model: Trained LSTM model.
    """
    early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val), callbacks=[early_stop])
    return model

def save_model(model, file_path='../models/lstm_model.keras'):
    """
    Saves the trained model to the specified file path in the Keras format.
    
    Args:
        model: Trained LSTM model.
        file_path (str): Path where the model will be saved.
    """
    model.save(file_path, save_format='keras')
