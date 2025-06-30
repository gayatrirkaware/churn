from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
from pymongo import MongoClient

# Init app
app = Flask(__name__)



# Load model and scaler
model = load_model('model/best_churn_model.h5')
scaler = joblib.load('model/scaler.pkl')


# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["churn_db"]
collection = db["predictions"]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form if request.form else request.get_json()

        features = [
            float(data['CreditScore']),
            float(data['Age']),
            float(data['Tenure']),
            float(data['Balance']),
            float(data['NumOfProducts']),
            float(data['HasCrCard']),
            float(data['IsActiveMember']),
            float(data['EstimatedSalary']),
            int(data['Geography_Germany']),
            int(data['Geography_Spain']),
            int(data['Gender_Male'])
        ]

        scaled_features = scaler.transform([features])
        prediction_prob = model.predict(scaled_features)[0][0]
        prediction = int(prediction_prob > 0.5)

        # Store in MongoDB
        record = {
            "input": features,
            "prediction": prediction,
            "confidence": float(prediction_prob)
        }
        collection.insert_one(record)

        return jsonify({
            "prediction": prediction,
            "confidence": round(float(prediction_prob), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
