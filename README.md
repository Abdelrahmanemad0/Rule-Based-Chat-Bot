# Rule-Based Chatbot with Machine Learning

A rule-based chatbot that classifies user queries with TF-IDF + a trained classifier and returns a matching canned response. Ships with both a terminal chat loop and a Gradio web UI.

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="Gradio" src="https://img.shields.io/badge/UI-Gradio-FF7C00">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

## Features

- **Text preprocessing** — tokenization, stopword removal, and Porter stemming (NLTK).
- **ML classification** — TF-IDF vectorization + a pre-trained scikit-learn classifier maps each query to a category.
- **Response matching** — the predicted category is mapped back to a canned response from `icthub_dataset.xlsx`.
- **Two interfaces** — a terminal REPL (`chatbot.py`) and a Gradio web chat UI (`chatbot_ui.py`) sharing the same core logic.

## Tech Stack

- Python, scikit-learn, NLTK
- Joblib (model/vectorizer/encoder serialization)
- Pandas (dataset loading)
- Gradio (web UI)

## How to Run

```bash
# Clone the repository
git clone https://github.com/Abdelrahmanemad0/Rule-Based-Chat-Bot.git
cd Rule-Based-Chat-Bot

# Install dependencies
pip install -r requirements.txt

# Run the chatbot in the terminal
python chatbot.py

# Or launch the Gradio web interface
python chatbot_ui.py
```

On first run, the required NLTK corpora (`punkt`, `stopwords`, `words`) are downloaded automatically.

## Project Structure

- `chatbot.py` — core preprocessing/classification logic + terminal chatbot
- `chatbot_ui.py` — Gradio web interface, built on top of `chatbot.py`
- `model.joblib` — pre-trained classifier for query classification
- `vectorizer.joblib` — TF-IDF vectorizer for text transformation
- `label_encoder.joblib` — label encoder for category prediction
- `icthub_dataset.xlsx` — dataset of categorized queries and responses

## Future Enhancements

- Expand the dataset with more queries and responses
- Add deep learning-based classification for improved accuracy
- Support multi-turn, context-aware conversations
- Add speech-to-text for voice interaction

## License

MIT — see [LICENSE](LICENSE).

#Chatbot #NLP #MachineLearning #Gradio #Python #AI #TextProcessing
