Stock Price Prediction Program

Overview

This program predicts future stock prices using a Long Short-Term Memory (LSTM) neural network. It provides a complete pipeline for preprocessing stock data, training a predictive model, and generating actionable buy/sell recommendations. The program includes a user-friendly GUI for managing data files and visualizing results.

Features

	•	Data Preprocessing: Handles stock data with scaling, cleaning, and sequence generation.
	•	LSTM Model: Trained to recognize patterns in historical data and predict future prices.
	•	GUI with Tkinter: A simple interface for adding, removing, and processing data files.
	•	Buy/Sell Recommendations: Evaluates predictions to suggest investment actions.
	•	Visualization: Plots actual vs. predicted stock prices for insights.

Here’s the correct Markdown format for the file structure that will display cleanly:

## File Structure
\```
predictive_model/
├── data_preprocessing.py   # Preprocesses raw stock data
├── model_training.py       # Builds and trains the LSTM model
├── prediction.py           # Generates predictions and recommendations
├── utils.py                # Helper functions for scaling and visualization
├── file_ui.py              # GUI for managing data files
├── main.py                 # Orchestrates the full pipeline
└── README.md               # Documentation for the project
\```

Copy and paste this into your README file, and it should display as intended in any Markdown viewer. Let me know if further tweaks are needed!

Requirements

	•	Python 3.8 or higher
	•	Required libraries:
	•	tensorflow
	•	numpy
	•	pandas
	•	matplotlib
	•	sklearn
	•	tkinter

Install dependencies using:

pip install tensorflow numpy pandas matplotlib scikit-learn

How to Use

- **data/**: Data is available on https://stooq.com/db/h/. Daily ASCII historicals are available

1. Preprocess Data

Run the file_ui.py script to manage and preprocess stock data files:

python file_ui.py

	•	Use the GUI to add .txt files, preprocess them, and log the processed sequences.

2. Train the Model

Edit main.py to point to the desired data file. Then, run:

python main.py

This will:
	•	Preprocess the data again (if necessary).
	•	Split data into training and validation sets.
	•	Train an LSTM model.
	•	Save the trained model to models/lstm_model.h5.

3. Make Predictions

The main.py script will:
	•	Predict stock prices for the next 5 days.
	•	Provide buy/sell recommendations.
	•	Plot predictions for visualization.

Extending the Program

	•	Add More Features: Extend the GUI to include model training or prediction options.
	•	Customize the Model: Modify model_training.py to experiment with LSTM architecture.
	•	Support Multiple Files: Update main.py to handle batch processing.

Example Output

Buy/Sell Recommendation

Recommendation: Buy
Recommended Sell Date: 2024-11-25

Visualization

	•	A plot comparing predicted and actual stock prices over time.

Future Improvements

	•	Add support for real-time stock data.
	•	Integrate with APIs like Alpha Vantage or Yahoo Finance.
	•	Deploy as a web application for broader accessibility.

License

This project is open-source and available under the MIT License.

Author

Developed by Isaias Palma. For inquiries or collaborations, connect with me on LinkedIn at:
https://www.linkedin.com/in/isaias-palma-software-engineer/
