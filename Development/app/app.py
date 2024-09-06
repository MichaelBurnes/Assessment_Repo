from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
# Assuming you're using scikit-learn for ML. Adjust imports as necessary.
from sklearn.externals import joblib

app = Flask(__name__)

# Load your machine learning model
model_path = os.path.join('models', 'your_model_filename.pkl')
model = joblib.load(model_path)

@app.route('/')
def index():
    """Homepage with links to different sections of the application."""
    return render_template('index.html')

@app.route('/eda')
def eda():
    # Example data
    chart_data = {
        'chart1': {'labels': ['Label 1', 'Label 2'], 'data': [10, 20]},
        # Add data for other charts as needed
    }
    return render_template('eda.html', chart_data=chart_data)

@app.route('/api/data/chart1')
def chart1_data():
    # Fetch or generate data for chart 1
    data = {'labels': ['Label 1', 'Label 2'], 'data': [10, 20]}
    return jsonify(data)


@app.route('/insights')
def insights():
    """Page for displaying Machine Learning Insights."""
    # Generate insights here or prepare data to be displayed on the webpage
    # For demonstration, we'll just pass an empty context
    context = {}
    return render_template('insights.html', **context)

@app.route('/test_model', methods=['GET', 'POST'])
def test_model():
    """Page for running the model on test data."""
    if request.method == 'POST':
        # Process test data from the form and run the model
        # For demonstration, we'll assume input data is in a form field named 'input_data'
        input_data = request.form.get('input_data')
        # Convert input_data to the format your model expects, run the model, and prepare the output
        # Here, we'll just return a dummy response
        output = "Model output based on input data"
        return render_template('test_model.html', output=output)
    else:
        # GET request, just render the page
        return render_template('test_model.html', output=None)

if __name__ == '__main__':
    app.run(debug=True)
