#### Author: Nicholas Hamilton
### AI was used sparingly for multiple different aspects of this.
### Giving starting numbers of the hyper-parameters for example,
### and some formatting was adjusted when I felt that my initial code
### was looking too convoluted and deviating from guides too far.


import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
from sklearn.metrics import accuracy_score, f1_score

#Configuration
MODEL_NAME = "distilbert-base-uncased"  # Using DistilBERT for faster training and less memory
DATASET_NAME = "imdb"
NUM_TRAIN_SAMPLES = 2000  # Using a small subset for a quick demonstration
NUM_EVAL_SAMPLES = 1000    # Using a small subset for evaluation
MAX_LENGTH = 256          # Max token length for sequences
OUTPUT_DIR = "./results_sentiment_analysis"
LOGGING_DIR = "./logs_sentiment_analysis"

# Loading and preparing - part 1
def load_and_prepare_data(tokenizer_name):
    print(f"Loading dataset: {DATASET_NAME}")
    # Load IMDb dataset
    dataset = load_dataset(DATASET_NAME)

    # For a faster demonstration, select a small subset
    train_dataset = dataset["train"].shuffle(seed=42).select(range(NUM_TRAIN_SAMPLES))
    eval_dataset = dataset["test"].shuffle(seed=42).select(range(NUM_EVAL_SAMPLES))

    print(f"Using {len(train_dataset)} samples for training and {len(eval_dataset)} for evaluation.")

    # Load Tokenizer
    print(f"Loading tokenizer: {tokenizer_name}")
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Preprocessing function to tokenize text
    def preprocess_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=MAX_LENGTH)

    print("Tokenizing datasets...")
    tokenized_train = train_dataset.map(preprocess_function, batched=True)
    tokenized_eval = eval_dataset.map(preprocess_function, batched=True)

    # Remove columns not needed by the model and rename 'label' to 'labels'
    tokenized_train = tokenized_train.remove_columns(["text"])
    tokenized_eval = tokenized_eval.remove_columns(["text"])
    tokenized_train = tokenized_train.rename_column("label", "labels")
    tokenized_eval = tokenized_eval.rename_column("label", "labels")

    # Set the format to PyTorch tensors
    tokenized_train.set_format("torch")
    tokenized_eval.set_format("torch")

    return tokenized_train, tokenized_eval, tokenizer

# 2. Define Metrics Computation
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions, average='binary') # 'binary' for 2-class sentiment
    return {"accuracy": accuracy, "f1": f1}

# --- Main Fine-Tuning Script
def main():
    print("!!!!!!!!! Starting BERT Fine-Tuning for Sentiment Analysis !!!!!!!!!!")

    #  Part 1: Fine-Tuning BERT
    # Load data and tokenizer
    train_dataset, eval_dataset, tokenizer = load_and_prepare_data(MODEL_NAME)

    # Load Model
    print(f"Loading pre-trained model: {MODEL_NAME} for sequence classification")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2) # 2 labels: positive/negative

    # Define Training Arguments
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=2,  # low for a simple example (e.g., 1-3 epochs)
        per_device_train_batch_size=8,  # Adjust based on my GPU memory
        per_device_eval_batch_size=8,
        warmup_steps=100,  # Number of steps for learning rate warmup
        weight_decay=0.01,  # Strength of weight decay regularization
        logging_dir=LOGGING_DIR,
        logging_steps=50,  # Log training info every 50 steps
        eval_strategy="epoch",  # Evaluate at the end of each epoch
        save_strategy="epoch",  # Save model checkpoint at the end of each epoch
        load_best_model_at_end=True, # Load the best model found during training (based on eval metric)
        metric_for_best_model="accuracy", # accuracy to determine the best model
        report_to="none"  # Disable external reporting tools like wandb for simplicity
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics
    )

    # Start Fine-Tuning
    print("\n--- Training the model (Part 1) ")
    trainer.train()
    # Training logs (loss, learning rate, validation accuracy/F1) will be printed to the console :)


    # Save the fine-tuned model and tokenizer
    model_save_path = f"{OUTPUT_DIR}/fine_tuned_sentiment_model"
    trainer.save_model(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    print(f"\nFine-tuned model and tokenizer saved to: {model_save_path}")


    print("\n--- Evaluating the Fine-Tuned Model")
    eval_results = trainer.evaluate() # Evaluate on the eval_dataset

    print("\n--- Short Analysis of Results (Part 1 Deliverable) ")
    print(f"Fine-tuning completed using the '{MODEL_NAME}' model.")
    print(f"The model was trained for {training_args.num_train_epochs} epoch(s) on {NUM_TRAIN_SAMPLES} training samples.")
    print("The evaluation metrics on the test set are:")
    for key, value in eval_results.items():
        print(f"  {key}: {value:.4f}")
    print("This indicates the model's performance on unseen data for sentiment classification.")
    print(f"Training logs (loss, learning rate, metrics per epoch) were printed above and can also be explored via tools like TensorBoard")

    # Part 2: Debugging Issues

    # This part, I adjusted several inputs into the model. The main thing I needed to change was to go to this smaller model because of my device limitations.
    # Sadly, I only have 16GB of RAM which is such a pain nowadays.

    # Part 3: Evaluating the Model
    print("\n---  Part 3: Evaluating the Model!")
    print("The `compute_metrics` function calculates Accuracy and F1-Score. These were shown above.")
    print("To generate predictions on a test set explicitly:")
    predictions_output = trainer.predict(eval_dataset)
    # print(f"Raw predictions output: {predictions_output}") # Contains predictions, label_ids, metrics
    predicted_labels = np.argmax(predictions_output.predictions, axis=-1)
    print(f"Sample predicted labels: {predicted_labels[:10]}")
    print(f"Sample true labels:      {predictions_output.label_ids[:10]}")


if __name__ == "__main__":
    # Ensure GPU is used if available, for faster training
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    main()