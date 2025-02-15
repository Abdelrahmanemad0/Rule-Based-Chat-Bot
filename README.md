# **Rule-Based Chatbot with Machine Learning**  

This repository contains a **rule-based chatbot** that utilizes **Natural Language Processing (NLP)** and **Machine Learning** techniques to classify user queries and provide relevant responses. The chatbot is trained using a labeled dataset and implements **TF-IDF vectorization** along with a **pre-trained classification model** to predict query categories and generate responses. The project also includes a **Gradio-based user interface** for interactive chatbot conversations.  

## **Features**  
- **Text Preprocessing:** Tokenization, stopword removal, stemming, and special character filtering  
- **Machine Learning Classification:** Uses a trained model for query classification  
- **TF-IDF Vectorization:** Converts text queries into numerical representations  
- **Response Matching:** Retrieves relevant responses based on predicted query categories  
- **Gradio Interface:** Provides a user-friendly web-based chatbot interface  

## **Technologies Used**  
- Python  
- Scikit-learn  
- NLTK (Natural Language Processing Toolkit)  
- Joblib (Model Serialization)  
- Pandas & NumPy (Data Processing)  
- Matplotlib (Visualization)  
- Gradio (Web UI for Chatbot)  

## **How to Run**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/rule-based-chatbot.git
   cd rule-based-chatbot
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the chatbot in the terminal:  
   ```bash
   python chatbot.py
   ```  
4. Launch the Gradio web interface:  
   ```bash
   python chatbot_ui.py
   ```  

## **Project Structure**  
- `chatbot.py` – Terminal-based chatbot implementation  
- `chatbot_ui.py` – Gradio web interface for chatbot  
- `model.joblib` – Pre-trained machine learning model for query classification  
- `vectorizer.joblib` – TF-IDF vectorizer for text transformation  
- `label_encoder.joblib` – Label encoder for category prediction  
- `icthub_dataset.xlsx` – Dataset containing categorized queries and responses  

## **Future Enhancements**  
- Expand dataset with more queries and responses  
- Integrate deep learning models for improved classification  
- Implement multi-turn conversation capabilities  
- Add speech-to-text support for voice interaction  

This chatbot provides a **foundation for automated query classification and response generation**, making it useful for **customer support, FAQ bots, and virtual assistants**.  

#Chatbot #NLP #MachineLearning #Gradio #Python #AI #TextProcessing
