"""
chatbot.py -- Terminal-based rule-based chatbot.

Classifies a user query into a category with a TF-IDF vectorizer + a
pre-trained classifier, then returns the canned response associated with
that category from icthub_dataset.xlsx.

Run directly for a CLI chat loop:
    python chatbot.py
"""

import string

import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import words as nltk_words
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

MODEL_PATH = "model.joblib"
VECTORIZER_PATH = "vectorizer.joblib"
LABEL_ENCODER_PATH = "label_encoder.joblib"
DATASET_PATH = "icthub_dataset.xlsx"

_NLTK_RESOURCES = ["punkt", "punkt_tab", "stopwords", "words"]


def ensure_nltk_resources():
    """Download required NLTK corpora if they aren't already present."""
    for resource in _NLTK_RESOURCES:
        nltk.download(resource, quiet=True)


def load_artifacts():
    """Load the trained model, vectorizer, label encoder, and Q&A dataset."""
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)
    dataset = pd.read_excel(DATASET_PATH)
    return model, vectorizer, label_encoder, dataset


def preprocess_query(text: str) -> str:
    """Lowercase, tokenize, strip stopwords/punctuation, and stem a query."""
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalnum()]
    stop_words = set(stopwords.words("english"))
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    stemmer = PorterStemmer()
    return " ".join(stemmer.stem(t) for t in tokens)


def is_meaningful_query(user_input: str, extra_vocab=("icthub",)) -> bool:
    """Return True if at least one word in the input is a recognized word."""
    vocab = set(nltk_words.words()) | set(extra_vocab)
    return any(word in vocab for word in user_input.lower().split())


def get_response_from_category(dataset: pd.DataFrame, category: str) -> str:
    """Look up the canned response for a predicted category."""
    matching_rows = dataset[dataset["Category"] == category]
    if matching_rows.empty:
        return "I'm sorry, I don't have an answer for that yet."
    return matching_rows.iloc[0]["Response"]


class Chatbot:
    """Wraps the trained artifacts and exposes a single `respond` method."""

    def __init__(self):
        ensure_nltk_resources()
        self.model, self.vectorizer, self.label_encoder, self.dataset = load_artifacts()

    def respond(self, user_input: str) -> str:
        if not user_input.strip() or not is_meaningful_query(user_input):
            return "I'm sorry, I didn't understand that."

        processed = preprocess_query(user_input)
        vectorized = self.vectorizer.transform([processed])
        predicted = self.model.predict(vectorized)
        category = self.label_encoder.inverse_transform(predicted)[0]
        return get_response_from_category(self.dataset, category)


def main():
    bot = Chatbot()
    print("Chatbot: Hello! How can I assist you today? (type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.respond(user_input))


if __name__ == "__main__":
    main()
