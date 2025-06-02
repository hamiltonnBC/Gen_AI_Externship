import pandas as pd
import pandas as pd
import numpy as np
import json
import re
import os
import itertools  # Not used in this snippet, but you have it imported
from tqdm import tqdm


# import nltk # Not used directly here for now
# from nltk.corpus import stopwords # Not used directly here for now
# stop_words = set(stopwords.words('english')) # Not used directly here for now

# Define function for text cleaning
def clean(text):
    text = text.replace("\n", " ")
    text = re.sub(r"_", " ", text, 0)
    text = re.sub(r"-{5,}", " ", text, 0)
    text = re.sub(r"\*+", "*", text, 0)
    text = re.sub(r" \.\ ", ".", text, 0)
    text = text.strip()
    return text


corpus = "CUAD_v1/full_contract_txt"
file_list = []  # Renamed to avoid conflict with 'file' module
contract_texts = []  # Renamed for clarity

for i in os.listdir(corpus):
    path = os.path.join(corpus, i)  # Use os.path.join for cross-platform compatibility
    if os.path.isfile(path) and i.endswith('.txt'):  # Ensure it's a text file
        file_list.append(i)
        with open(path, 'r', errors='ignore', encoding='utf-8') as f:  # Added encoding
            text = f.read()
            text = clean(text)
            contract_texts.append(text)

df_final = pd.DataFrame({'file': file_list, 'contract': contract_texts})
df_final['contract'] = df_final['contract'].str.slice(0, 5000)

# Load the CUAD annotations CSV
try:
    cuad_wide_df = pd.read_csv(
        '/GenerativeAI/Training_Bert/extracting_legal_documents/CUAD_v1/master_clauses.csv')
    print("CUAD CSV (wide format) loaded successfully.")
    # --- DEBUG: Print first few filenames from CUAD CSV ---
    print("\nFirst 5 'Filename' entries from CUAD CSV:")
    print(cuad_wide_df['Filename'].head().to_list())
    print("\nFirst 5 'Document Name' entries from CUAD CSV (for comparison):")
    print(cuad_wide_df['Document Name'].head().to_list())
    # --- END DEBUG ---
except FileNotFoundError:
    print("Error: master_clauses.csv not found.")
    exit()
except KeyError as e:
    print(f"KeyError loading or inspecting CUAD CSV: {e}. Check column names like 'Filename' or 'Document Name'.")
    exit()

TARGET_COLUMNS_AS_LABELS = [
    "Parties", "Agreement Date", "Effective Date", "Expiration Date", "Governing Law",
]
processed_data_for_spacy = []

print(f"\nStarting to process {len(df_final)} files from df_final...")
# --- DEBUG: Print first few filenames from df_final ---
if not df_final.empty:
    print("\nFirst 5 'file' entries from df_final:")
    print(df_final['file'].head().to_list())
else:
    print("df_final is empty. Check the file reading loop.")
    exit()
# --- END DEBUG ---

files_matched_count = 0
files_not_matched_count = 0

for index, contract_row in tqdm(df_final.iterrows(), total=df_final.shape[0]):
    contract_filename_from_df_final = contract_row['file']
    full_contract_text = contract_row['contract']
    # --- DEBUG: Print current filename being processed from df_final ---
    print(f'\n\nProcessing index: {index}, Type of index: {type(index)}\n\n')
    if index < 5:  # Limit printing for brevity
        print(f"Current df_final file (from index {index}): {contract_filename_from_df_final}")
    # --- END DEBUG ---

    try:
        # Attempt to match. Which column in cuad_wide_df should be used? 'Filename' or 'Document Name'?
        # Let's try 'Filename' first as per original code, but 'Document Name' might be cleaner.
        # Crucially, are extensions (.txt) present in one but not the other?
        # Are there other path components or identifiers?

        # OPTION 1: Exact match (as in your code) - likely to fail if formats differ
        # annotation_row_matches = cuad_wide_df[cuad_wide_df['Filename'] == contract_filename_from_df_final]

        # OPTION 2: Match 'Document Name' after stripping extension from contract_filename_from_df_final
        base_name_from_df_final = contract_filename_from_df_final.replace('.txt', '')
        annotation_row_matches = cuad_wide_df[cuad_wide_df['Document Name'] == base_name_from_df_final]

        if not annotation_row_matches.empty:
            annotation_row = annotation_row_matches.iloc[
                0]  # Take the first match if multiple (should be unique by Document Name ideally)
            files_matched_count += 1
        else:
            # --- DEBUG: This file from df_final was not found in cuad_wide_df['Document Name'] ---
            if files_not_matched_count < 10:  # Print for the first few misses
                print(
                    f"No matching annotations for '{base_name_from_df_final}' (derived from '{contract_filename_from_df_final}') using 'Document Name' column in master_clauses.csv")
            files_not_matched_count += 1
            continue  # Skip if no annotations found for this file

        labels_for_this_contract = []
        for label_category in TARGET_COLUMNS_AS_LABELS:
            if label_category in annotation_row and pd.notna(annotation_row[label_category]):
                text_span_to_find = str(annotation_row[label_category])
                for match in re.finditer(re.escape(text_span_to_find), full_contract_text):
                    start_char = match.start()
                    end_char = match.end()
                    if start_char < len(full_contract_text) and end_char <= len(full_contract_text):
                        labels_for_this_contract.append([start_char, end_char, label_category])
                    break

        if labels_for_this_contract:  # Only append if we actually found some labels for this contract
            processed_data_for_spacy.append({
                'id': index,
                'data': full_contract_text,
                'label': labels_for_this_contract
            })

    except Exception as e:  # Catch any other unexpected errors during processing a row
        if index < 5:  # Limit printing for brevity
            print(f"Error processing row for {contract_filename_from_df_final}: {e}")
        continue

print(f"\nFiles matched: {files_matched_count}, Files not matched: {files_not_matched_count}")

df_spacy_input = pd.DataFrame(processed_data_for_spacy)

if not df_spacy_input.empty:
    # Filter out rows that ended up with no relevant labels (already handled by appending only if labels_for_this_contract is not empty)
    # df_spacy_input = df_spacy_input[df_spacy_input['label'].map(lambda d: len(d)) > 0].copy() # This might be redundant now
    print(f"\nNumber of documents with extracted annotations: {len(df_spacy_input)}")
    if not df_spacy_input.empty:
        print("\nSample of processed data:")
        print(df_spacy_input.head())
    else:
        print("No documents with annotations after filtering. Check matching logic and TARGET_COLUMNS_AS_LABELS.")
else:
    print("No data processed into df_spacy_input. All files might have failed matching or had no target labels found.")
# ... Now you can proceed with the SpaCy processing steps from the guide,
# using df_spacy_input ...