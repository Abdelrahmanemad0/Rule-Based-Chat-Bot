"""Gradio web interface for the chatbot. Run with: python chatbot_ui.py"""

import os

import gradio as gr

from chatbot_core import chatbot_response

LOGO_PATH = "icthub_logo.jpg"

conversation = []


def respond(user_input, _history=None):
    global conversation

    if user_input.lower() == "exit":
        conversation.append(
            ("Chatbot", "Goodbye! Click 'Start New Conversation' to begin a new chat.")
        )
        return conversation, gr.update(value="", interactive=False)

    response = chatbot_response(user_input)
    conversation.append(("You", user_input))
    conversation.append(("Chatbot", response))
    return conversation, gr.update(value="")


def reset_chat():
    global conversation
    conversation = []
    return conversation, gr.update(value="", interactive=True)


with gr.Blocks() as iface:
    if os.path.exists(LOGO_PATH):
        gr.Image(LOGO_PATH, elem_id="logo")

    chatbot = gr.Chatbot(elem_id="chatbot")

    with gr.Row():
        with gr.Column(scale=7):
            user_input = gr.Textbox(
                label="You", placeholder="Type a message...", lines=1, elem_id="user_input"
            )
        with gr.Column(scale=1):
            with gr.Row():
                send_button = gr.Button("Send", elem_id="send_button")
            with gr.Row():
                new_conversation_button = gr.Button(
                    "Start New Conversation", visible=True, elem_id="new_conversation_button"
                )

    send_button.click(respond, inputs=user_input, outputs=[chatbot, user_input])
    new_conversation_button.click(reset_chat, outputs=[chatbot, user_input])
    user_input.submit(respond, inputs=user_input, outputs=[chatbot, user_input])


if __name__ == "__main__":
    iface.launch()
