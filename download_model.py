import os
from transformers import AutoModel, AutoTokenizer

MODEL_NAME = "intfloat/e5-small-v2"
MODEL_DIR = "model/e5-small-v2"

def download_model():
    os.makedirs(MODEL_DIR, exist_ok=True)
    print(f"Downloading model '{MODEL_NAME}' to '{MODEL_DIR}' ...")

    # Download tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.save_pretrained(MODEL_DIR)

    # Download model weights
    model = AutoModel.from_pretrained(MODEL_NAME)
    model.save_pretrained(MODEL_DIR)

    print("Model and tokenizer downloaded successfully.")

if __name__ == "__main__":
    download_model()
