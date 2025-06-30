# 🧠 Customer Churn Prediction Web App

This project is a Flask-based web application that predicts whether a customer is likely to churn using a trained deep learning model. The system takes input data through a form or JSON and stores predictions in a MongoDB database for further analysis.

---

## 📌 Features

- Predicts customer churn using a trained Keras model.
- Uses a pre-fitted `StandardScaler` for input normalization.
- Accepts form data or JSON input.
- Saves prediction results to MongoDB.
- Simple frontend form using HTML and Flask templates.

---

## 🗂️ Project Structure

├── app.py # Main Flask application
├── model/
│ ├── best_churn_model.h5 # Trained Keras model
│ └── scaler.pkl # Scikit-learn StandardScaler
├── templates/
│ └── index.html # Frontend form
├── static/ # Optional: for CSS or JS
├── requirements.txt # Python dependencies
└── README.md # This file



---

## 🔧 Tech Stack

- **Backend:** Python, Flask
- **Modeling:** TensorFlow/Keras, scikit-learn
- **Database:** MongoDB
- **Frontend:** HTML (Jinja2 template engine)
- **Deployment:** Localhost or any WSGI server (e.g., Gunicorn)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/churn-prediction-app.git
cd churn-prediction-app
```


### 2. Set Up Python Environment
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

Sample requirements.txt:
Flask
numpy
tensorflow
scikit-learn
joblib
pymongo

### 4. Start MongoDB
Ensure MongoDB is installed and the service is running.
```bash
mongod --dbpath "C:/data/db"  # or your MongoDB data path
```

### 5. Run the Flask App
```bash
python app.py
```
