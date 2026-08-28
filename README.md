# Spam Email / MMS Detection Project

This project demonstrates a machine learning-based spam detection system for emails and SMS messages. It combines natural language preprocessing, TF-IDF vectorization, and a logistic regression classifier to detect whether a message is likely spam or not spam.

## Features

- Text preprocessing and cleaning
- TF-IDF feature extraction
- Logistic Regression classifier
- Real-time prediction in a Streamlit dashboard
- SQLite-based monitoring of recent detections
- Model persistence with joblib

## Project structure

- `app.py` - Streamlit dashboard
- `train_model.py` - Train and save the spam detection model
- `spam_detector/model_utils.py` - NLP + ML logic
- `spam_detector/db.py` - SQLite helper functions
- `data/spam_data.csv` - Sample training data
- `models/` - Saved model artifacts

## Setup

1. Create a virtual environment (optional but recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python train_model.py
```

4. Run the dashboard:

```bash
streamlit run app.py
```

## Usage

- Enter an email or SMS in the dashboard
- Click "Analyze message"
- View the predicted class and confidence score
- Review recent detections stored in SQLite

## Model

This project uses:

- TF-IDF vectorizer
- Logistic Regression classifier

The model is saved in the `models/` folder after training.

Quick start on Windows

- Use the provided helper script to create a virtual environment, install deps and run the app:

```
run.bat
```

- Or follow the manual steps in the Setup section (create venv, pip install -r requirements.txt, then `streamlit run app.py`).
