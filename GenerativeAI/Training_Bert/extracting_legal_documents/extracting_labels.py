import re
from transformers import pipeline

# === Text from document ===
document_text = """
Case: 0:20-cr-00020-DLB-CJS Doc #: 49 Filed: 01/23/25 Page: 1 of 2 - Page ID#: <pageID>
UNITED STATES DISTRICT COURT
EASTERN DISTRICT OF KENTUCKY
NORTHERN DIVISION
AT ASHLAND
CRIMINAL CASE NO. 20-20-DLB-CJS
CIVIL ACTION NO. 24-84-DLB-CJS
UNITED STATES OF AMERICA
V.
ORDER ADOPTING REPORT AND RECOMMENDATION
LAMON TOLBERT
** ** ** ** ** ** ** **
PLAINTIFF
DEFENDANT
This matter is before the Court upon the Report and Recommendation ("R&R") of
United States Magistrate Judge Candace J. Smith (Doc. #48), wherein she recommends
that Defendant's Motion to Vacate, Set Aside, or Correct a Sentence under 28 U.S.C.
§ 2255 (Doc. # 45) be denied. No objections having been filed, and the time to do so
having now expired, the R&R is ripe for the Court's consideration.
The Court having reviewed the R&R, concluding that it is sound in all respects, and being otherwise
sufficiently advised,
IT IS ORDERED as follows:
(1) The Magistrate Judge's R&R (Doc. # 48) is hereby ADOPTED as the
findings of fact and conclusions of law of the Court;
(2) The Defendant's Motion to Vacate, Set Aside, or Correct a Sentence under
28 U.S.C. § 2255 (Doc. #45) is hereby DENIED;
(3) This matter is DISMISSED with prejudice and STRICKEN from the Court's
active docket; and
Case: 0:20-cr-00020-DLB-CJS Doc #: 49 Filed: 01/23/25 Page: 2 of 2 - Page ID#: <pageID>
(4) For the reasons set forth herein and in Judge Smith's Report and
Recommendation (Doc. #48), the Court determines that there is no arguable merit for an
appeal in this matter and, therefore, NO CERTIFICATE OF APPEALABILITY SHALL
ISSUE.
This 23rd day of January, 2025.
Signed By:
David L. Bunning DB
United States District Judge
"""

#  a list to store our annotations
annotations = []

# === 1. Rule-Based Annotation using Regular Expressions ===

#  regex patterns for different entities
patterns = {
    "DATE": r"\b\d{1,2}/\d{1,2}/\d{2,4}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?,\s+\d{4}\b",
    "CASE_NUMBER": r"\b\d{1,2}:\d{2,}-\w{2,}-\d{5,}-[A-Z]{2,}(?:-[A-Z]{2,})?\b|\b\d{2,}-\d{2,}-[A-Z]{3,}(?:-[A-Z]{3,})?\b",
    # Adjusted for both formats
    "DOCUMENT_REFERENCE": r"\(Doc\. #\s*\d+\)",
    "STATUTE_REFERENCE": r"\b28 U\.S\.C\.\s+§\s+\d+\b",
    "COURT_NAME": r"UNITED STATES DISTRICT COURT\s+EASTERN DISTRICT OF KENTUCKY\s+NORTHERN DIVISION\s+AT ASHLAND"
}

for entity_label, pattern in patterns.items():
    for match in re.finditer(pattern, document_text):
        annotations.append({
            "text": match.group(0),
            "label": entity_label,
            "start_char": match.start(),
            "end_char": match.end(),
            "method": "Regex"
        })

# === 2. AI-Based Annotation for PERSON names using Hugging Face Transformers ===

try:
    # `grouped_entities=True` groups parts of a multi-word name together.
    ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)


    ai_entities = ner_pipeline(document_text)

    for entity in ai_entities:
        # The model we chose labels persons as 'PER'
        if entity['entity_group'] == 'PER':
            annotations.append({
                "text": entity['word'],
                "label": "PERSON",  # Standardizing our label
                "start_char": entity['start'],
                "end_char": entity['end'],
                "method": "AI (Hugging Face)"
            })
except Exception as e:
    print(f"Could not run AI entity extraction: {e}")
    print("Make sure you have an internet connection to download the model,")
    print("and the 'transformers' and 'torch' (or 'tensorflow') libraries installed.")
    print("You can install them with: pip install transformers torch")

# === 3. Print Annotations ===
print("Found Annotations:")
# Sorted annotations by their starting character position for readability
annotations.sort(key=lambda x: x['start_char'])

for ann in annotations:
    print(f"- Text: '{ann['text']}'")
    print(f"  Label: {ann['label']}")
    print(f"  Position: {ann['start_char']}-{ann['end_char']}")
    print(f"  Method: {ann['method']}")
    print("-" * 20)