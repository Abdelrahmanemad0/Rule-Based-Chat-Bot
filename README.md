# Rule-Based Chatbot with Machine Learning

This repository contains a rule-based chatbot that utilizes Natural Language Processing (NLP) and Machine Learning techniques to classify user queries and provide relevant responses. The chatbot is trained using a labeled dataset and implements TF-IDF vectorization along with a pre-trained classification model to predict query categories and generate responses. The project also includes a Gradio-based user interface for interactive chatbot conversations.

## Features

- **Text Preprocessing**: Tokenization, stopword removal, stemming, and special character filtering
- **Machine Learning Classification**: Uses a trained model for query classification
- **TF-IDF Vectorization**: Converts text queries into numerical representations
- **Response Matching**: Retrieves relevant responses based on predicted query categories
- **Gradio Interface**: Provides a user-friendly web-based chatbot interface

## Technologies Used

- Python
- Scikit-learn
- NLTK (Natural Language Processing Toolkit)
- Joblib (Model Serialization)
- Pandas & NumPy (Data Processing)
- Gradio (Web UI for Chatbot)

## How to Run

Clone the repository:
```bash
git clone https://github.com/Abdelrahmanemad0/Rule-Based-Chat-Bot.git
cd Rule-Based-Chat-Bot
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the chatbot in the terminal:
```bash
python chatbot.py
```

Launch the Gradio web interface:
```bash
python chatbot_ui.py
```

## Project Structure

- `chatbot_core.py` – Shared logic: loads the pre-trained model/vectorizer/label encoder and exposes `chatbot_response()`
- `chatbot.py` – Terminal-based chatbot (imports from `chatbot_core.py`)
- `chatbot_ui.py` – Gradio web interface for the chatbot (imports from `chatbot_core.py`)
- `model.joblib` – Pre-trained machine learning model for query classification
- `vectorizer.joblib` – TF-IDF vectorizer for text transformation
- `label_encoder.joblib` – Label encoder for category prediction
- `icthub_dataset.xlsx` – Dataset containing categorized queries and responses
- `requirements.txt` – Python dependencies

## Fixes in this revision

- **Split the original Colab-exported script into modules.** The old `rule_base_chatbot.py` mixed CLI code, two different Gradio UIs, and a Colab `!pip install` shell command in one file, so it couldn't actually be run with `python rule_base_chatbot.py`. It's now `chatbot_core.py` (shared logic), `chatbot.py` (CLI), and `chatbot_ui.py` (Gradio UI), matching what this README always described.
- **Stopped re-fitting the pre-trained vectorizer/label encoder on import.** The old code loaded `vectorizer.joblib` and `label_encoder.joblib` via `joblib.load()` but then immediately called `.fit_transform()` on them again using the full dataset, silently discarding the pre-trained state every time the module was imported.
- **Fixed a word-filtering bug** in the "is this query meaningful" check, which previously mutated a list while iterating over it (skipping every other word).

## Future Enhancements

- Expand dataset with more queries and responses
- Integrate deep learning models for improved classification
- Implement multi-turn conversation capabilities
- Add speech-to-text support for voice interaction

This chatbot provides a foundation for automated query classification and response generation, making it useful for customer support, FAQ bots, and virtual assistants.

## License

MIT — see [LICENSE](LICENSE).

#Chatbot #NLP #MachineLearning #Gradio #Python #AI #TextProcessing
