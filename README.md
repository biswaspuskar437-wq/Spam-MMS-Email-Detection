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

## Development phases

### Phase 1 — Project Setup

Set up the project structure, Python environment, required dependencies, Git, GitHub repository, `.gitignore`, and project documentation.

### Phase 2 — Dataset Collection & Preprocessing

Collect spam and legitimate SMS/email datasets, remove duplicates and missing data, clean the text, preprocess messages, and prepare the training and testing datasets.

### Phase 3 — Exploratory Data Analysis

Analyze the dataset to understand spam distribution, message length, frequently used words, and other important patterns using charts and visualizations.

### Phase 4 — Machine Learning Model

Convert text into numerical features using TF-IDF and train machine learning models such as Naive Bayes, Logistic Regression, and SVM. Select the best-performing model for spam detection.

### Phase 5 — Model Evaluation

Evaluate the trained model using accuracy, precision, recall, F1-score, and confusion matrix. Save the final trained model and vectorizer for application use.

### Phase 6 — Backend Development

Develop a FastAPI backend that loads the trained ML model and provides APIs for message prediction, prediction history, statistics, and user authentication.

### Phase 7 — Frontend Development

Build a responsive React web application with pages for Home, Spam Detector, Dashboard, History, Login/Register, and Model Information.

### Phase 8 — Database Integration

Integrate PostgreSQL to securely store users, messages, predictions, confidence scores, timestamps, and detection history.

### Phase 9 — Authentication & Security

Implement secure user authentication using JWT, password hashing, input validation, CORS configuration, environment variables, and API security practices.

### Phase 10 — Dashboard & Analytics

Create an interactive dashboard showing total messages analyzed, spam messages, safe messages, spam percentage, prediction history, and visual analytics.

### Phase 11 — Real-Time Email Detection

Integrate an email provider's official API/OAuth system to automatically monitor incoming emails and send new messages to the spam detection model in real time.

### Phase 12 — MMS/Image Spam Detection

Extend the system to analyze MMS content, including text and images, using appropriate machine learning or deep learning models for multimodal spam detection.

### Phase 13 — Testing

Perform unit, integration, API, database, and frontend testing to ensure that all components work correctly and reliably.

### Phase 14 — Deployment

Deploy the React frontend, FastAPI backend, PostgreSQL database, and ML model to cloud platforms and configure the application for production use.

### Phase 15 — Documentation

Complete the GitHub README with project description, features, architecture, installation instructions, screenshots, API documentation, model performance, results, and future improvements.

## Final architecture

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
ML Spam Detection Model
  ↓
Prediction
  ↓
PostgreSQL Database
  ↓
Dashboard & History
```

## Future scope

The project can be further improved by adding multilingual spam detection, phishing/URL detection, advanced deep learning models, image-based spam detection, real-time notifications, and continuous model improvement using newly detected messages.
