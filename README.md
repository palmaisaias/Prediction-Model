# Stock Prediction Project

This project uses historical stock data and a machine learning model (LSTM) to generate buy/sell recommendations.

## Project Structure
- **data/**: Contains the input data file (`aacg.us.txt`).
- **models/**: Stores the trained model (`lstm_model.h5`) if saved.
- **src/**: Contains the scripts for data preprocessing, model training, prediction, and utility functions.
- **main.py**: Main script to run the end-to-end process.

## Instructions
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the project:
    ```bash
    python main.py
    ```

## Requirements
- Python 3.7+
- TensorFlow
- Pandas
- Numpy
- Scikit-learn
