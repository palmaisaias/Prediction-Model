from flask import Flask, request, jsonify, render_template
from src.data_preprocessing import load_and_preprocess_data, split_data
from src.model_training import build_model, train_model
from src.prediction import make_predictions, make_recommendation
from src.utils import inverse_scale_data
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Run the model
    try:
        # Preprocess data
        scaled_data, scaler = load_and_preprocess_data(file_path)
        X, y = split_data(scaled_data)

        # Split data
        split = int(0.8 * len(X))
        X_train, y_train = X[:split], y[:split]
        X_val, y_val = X[split:], y[split:]

        # Build and train the model
        model = build_model((X_train.shape[1], X_train.shape[2]))
        model = train_model(model, X_train, y_train, X_val, y_val)

        # Make predictions
        days_ahead = 5
        predicted_prices = make_predictions(model, scaled_data, days_ahead)

        # Convert predictions back to original scale
        predicted_prices_unscaled = inverse_scale_data(
            [[0, 0, 0, pred, 0] for pred in predicted_prices], scaler)[:, 3]

        # Generate recommendation
        recommendation, sell_date = make_recommendation(predicted_prices, scaler)
        return jsonify({
            'predictions': predicted_prices_unscaled.tolist(),
            'recommendation': recommendation,
            'sell_date': str(sell_date)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)