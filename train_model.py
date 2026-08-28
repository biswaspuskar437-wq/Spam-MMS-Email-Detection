from spam_detector.model_utils import train_model

if __name__ == "__main__":
    result = train_model()
    print(f"Training complete. Accuracy: {result['accuracy']}")
    print(f"Model saved to: {result['model_path']}")
