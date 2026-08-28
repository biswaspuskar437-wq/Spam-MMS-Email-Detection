import os

import pandas as pd
import streamlit as st

from spam_detector.db import get_recent_messages, init_db, log_prediction
from spam_detector.model_utils import predict_message, train_model

PROJECT_ROOT = os.path.dirname(__file__)
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "spam_data.csv")
MODEL_DIR = os.path.join(PROJECT_ROOT, "models")


def ensure_model_ready():
    model_files = [
        os.path.join(MODEL_DIR, "tfidf_vectorizer.joblib"),
        os.path.join(MODEL_DIR, "spam_model.joblib"),
    ]
    if not all(os.path.exists(path) for path in model_files):
        train_model(DATA_PATH, MODEL_DIR)
    init_db()


st.set_page_config(page_title="Spam Detector", page_icon="📬", layout="wide")

st.title("Spam Email / MMS Detection")
st.caption("AI-powered classification using NLP, TF-IDF, and Logistic Regression")

ensure_model_ready()

with st.sidebar:
    st.header("Model info")
    st.write("Algorithm: Logistic Regression")
    st.write("Features: TF-IDF vectorizer")
    st.write("Storage: SQLite database")

    st.markdown("---")
    if st.button("Retrain model"):
        result = train_model(DATA_PATH, MODEL_DIR)
        st.success(f"Model retrained successfully. Accuracy: {result['accuracy']}")

col1, col2 = st.columns([2, 1])

with col1:
    user_message = st.text_area(
        "Enter an email or SMS message:",
        height=220,
        placeholder="Example: You have won a free prize. Claim now!",
    )

    if st.button("Analyze message"):
        if not user_message.strip():
            st.warning("Please enter a message before analyzing.")
        else:
            label, confidence = predict_message(user_message, MODEL_DIR)
            display_label = "Spam" if label == "spam" else "Not Spam"
            confidence_percent = confidence * 100
            st.success(f"Prediction: {display_label}")
            st.metric("Confidence", f"{confidence_percent:.2f}%")
            log_prediction(user_message, display_label, confidence)

with col2:
    st.subheader("Quick insight")
    st.info(
        "Messages containing urgent offers, prize claims, or suspicious links are often classified as spam."
    )
    st.markdown("- Uses NLP preprocessing")
    st.markdown("- Applies TF-IDF scores")
    st.markdown("- Predicts in real time")

st.subheader("Recent detections")
records = get_recent_messages(limit=10)
if records:
    df = pd.DataFrame(records)
    df["confidence"] = df["confidence"].map(lambda x: f"{x * 100:.2f}%")
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.write("No predictions logged yet.")
