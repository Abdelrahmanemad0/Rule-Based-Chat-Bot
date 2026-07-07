"""
Core chatbot logic shared by the CLI (chatbot.py) and the Gradio web UI
(chatbot_ui.py).

Loads the pre-trained TF-IDF vectorizer, label encoder, and classification
model, and exposes chatbot_response() to turn a raw user message into a
reply.
"""

import string

import joblib
import pandas as pd
import nltk
from nltk.corpus import words as nltk_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

for _resource in ("punkt", "punkt_tab", "stopwords", "words"):
    try:
        nltk.data.find(
            f"tokenizers/{_resource}" if "punkt" in _resource else f"corpora/{_resource}"
        )
    except LookupError:
        nltk.download(_resource)

MODEL_PATH = "model.joblib"
VECTORIZER_PATH = "vectorizer.joblib"
LABEL_ENCODER_PATH = "label_encoder.joblib"
DATASET_PATH = "icthub_dataset.xlsx"

# These three artifacts are pre-trained/fitted offline (see the original
# training notebook) and loaded as-is here. Earlier versions of this module
# re-fit the vectorizer and label encoder on the full dataset every time it
# was imported, which silently discarded the pre-trained state on every run.
best_model = joblib.load(MODEL_PATH)
tfidf_vectorizer = joblib.load(VECTORIZER_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)
dataset = pd.read_excel(DATASET_PATH)

_stemmer = PorterStemmer()
_stopwords = set(stopwords.words("english"))
_known_words = set(nltk_words.words()) | {"icthub"}


def preprocess_query(text):
    """Lowercase, tokenize, strip punctuation/stopwords, and stem a query."""
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalnum()]
    tokens = [t for t in tokens if t not in _stopwords and t not in string.punctuation]
    tokens = [_stemmer.stem(t) for t in tokens]
    return " ".join(tokens)


def get_response_from_category(category):
    """Look up the canned response associated with a predicted category."""
    matching_rows = dataset[dataset["Category"] == category]
    if matching_rows.empty:
        return "I'm sorry, I don't have a response for that category yet."
    return matching_rows.iloc[0]["Response"]


def is_meaningful_query(user_input):
    """True if at least one word in the input is a recognized English word
    (or a known project-specific term like "icthub")."""
    input_words = user_input.lower().split()
    return any(word in _known_words for word in input_words)


def chatbot_response(user_input):
    """Classify a raw user message and return the matching canned response."""
    if not is_meaningful_query(user_input):
        return "I'm sorry, I didn't understand that."

    processed = preprocess_query(user_input)
    vectorized = tfidf_vectorizer.transform([processed])
    predicted = best_model.predict(vectorized)
    predicted_category = label_encoder.inverse_transform(predicted)[0]
    return get_response_from_category(predicted_category)
