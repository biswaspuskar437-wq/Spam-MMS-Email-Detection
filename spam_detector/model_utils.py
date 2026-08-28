import os
import re

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DEFAULT_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "spam_data.csv")
DEFAULT_MODEL_DIR = os.path.join(PROJECT_ROOT, "models")


def clean_text(text):
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_training_data(csv_path=DEFAULT_DATA_PATH):
    df = pd.read_csv(csv_path)
    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("Training data must contain 'text' and 'label' columns.")
    df = df.copy()
    df["clean_text"] = df["text"].apply(clean_text)
    return df


def train_model(csv_path=DEFAULT_DATA_PATH, model_dir=DEFAULT_MODEL_DIR):
    os.makedirs(model_dir, exist_ok=True)
    df = load_training_data(csv_path)

    X = df["clean_text"]
    y = df["label"].astype(str)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)
    predictions = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, predictions)

    joblib.dump(vectorizer, os.path.join(model_dir, "tfidf_vectorizer.joblib"))
    joblib.dump(model, os.path.join(model_dir, "spam_model.joblib"))

    return {
        "accuracy": round(float(accuracy), 4),
        "model_path": os.path.join(model_dir, "spam_model.joblib"),
    }


def load_model_artifacts(model_dir=DEFAULT_MODEL_DIR):
    vectorizer_path = os.path.join(model_dir, "tfidf_vectorizer.joblib")
    model_path = os.path.join(model_dir, "spam_model.joblib")

    if not os.path.exists(vectorizer_path) or not os.path.exists(model_path):
        raise FileNotFoundError("Model artifacts are missing. Run train_model.py first.")

    vectorizer = joblib.load(vectorizer_path)
    model = joblib.load(model_path)
    return vectorizer, model


def predict_message(message, model_dir=DEFAULT_MODEL_DIR):
    vectorizer, model = load_model_artifacts(model_dir)
    cleaned = clean_text(message)
    features = vectorizer.transform([cleaned])
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    class_index = list(model.classes_).index(prediction)
    confidence = float(probabilities[class_index])
    return prediction, confidence
