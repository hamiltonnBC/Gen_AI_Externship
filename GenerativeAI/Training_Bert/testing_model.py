# Sample data AI generated



import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np


SAVED_MODEL_PATH = "./results_sentiment_analysis/fine_tuned_sentiment_model"


sample_texts = [
    "This movie was absolutely fantastic! The acting was superb and the plot was gripping.",
    "I was really disappointed with this film. It was boring and the ending made no sense.",
    "An okay movie, not great but not terrible either. Had some good moments.",
    "The special effects were incredible, but the story was a bit weak.",
    "I loved every minute of it, a true masterpiece!",
    "Worst movie I've seen all year. A complete waste of time."
]


print(f"Loading tokenizer from: {SAVED_MODEL_PATH}")
try:
    tokenizer = AutoTokenizer.from_pretrained(SAVED_MODEL_PATH)
    print("Tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading tokenizer: {e}")
    print("Please ensure the SAVED_MODEL_PATH is correct and contains tokenizer files.")
    exit()

print(f"Loading model from: {SAVED_MODEL_PATH}")
try:
    model = AutoModelForSequenceClassification.from_pretrained(SAVED_MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Please ensure the SAVED_MODEL_PATH is correct and contains model files (like pytorch_model.bin).")
    exit()


print("\n-Making Predictions-")

for text in sample_texts:
    inputs = tokenizer(text,
                       padding="max_length",        # Pad to the model's max input size
                       truncation=True,             # Truncate if longer
                       max_length=256,              # Max length used during training (can often be inferred from tokenizer.model_max_length if not set)
                       return_tensors="pt")         # Return PyTorch tensors

    with torch.no_grad():
        outputs = model(**inputs) #  tokenized inputs to the model


    #    The `outputs` object contains `logits`. Logits are raw, unnormalized scores.
    logits = outputs.logits
    probabilities = torch.softmax(logits, dim=-1)
    #    To get the predicted class (0 or 1), we find the index of the highest logit:
    predicted_class_id = torch.argmax(logits, dim=-1).item()

    # 4. Map class ID to human-readable label
    if hasattr(model.config, 'id2label') and model.config.id2label:
        predicted_label = model.config.id2label[predicted_class_id]
    elif predicted_class_id == 1:
        predicted_label = "Positive"
    elif predicted_class_id == 0:
        predicted_label = "Negative"
    else:
        predicted_label = f"Unknown Class ID: {predicted_class_id}"


    print(f"\nReview: \"{text}\"")
    print(f"Probabilities: {probabilities.numpy()}") #
    print(f"Predicted Sentiment: {predicted_label} (Class ID: {predicted_class_id})")

