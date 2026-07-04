"""Terminal-based chatbot. Run with: python chatbot.py"""

from chatbot_core import chatbot_response


def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))


if __name__ == "__main__":
    main()
