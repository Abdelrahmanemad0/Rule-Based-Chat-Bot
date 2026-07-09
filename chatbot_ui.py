"""
chatbot_ui.py -- Gradio web interface for the rule-based chatbot.

Run directly to launch a local web UI:
    python chatbot_ui.py
"""

import gradio as gr

from chatbot import Chatbot

bot = Chatbot()
conversation = []


def respond(user_input, history):
    global conversation
    if not user_input.strip():
        return conversation, ""
    if user_input.strip().lower() == "exit":
        conversation.append(("You", user_input))
        conversation.append(("Chatbot", "Goodbye! Click 'Start New Conversation' to chat again."))
        return conversation, ""

    reply = bot.respond(user_input)
    conversation.append(("You", user_input))
    conversation.append(("Chatbot", reply))
    return conversation, ""


def reset_chat():
    global conversation
    conversation = []
    return conversation, ""


def build_interface():
    with gr.Blocks(title="ICTHub Chatbot") as demo:
        gr.Markdown("# ICTHub Rule-Based Chatbot")
        chatbot_component = gr.Chatbot(elem_id="chatbot")

        with gr.Row():
            with gr.Column(scale=7):
                user_input = gr.Textbox(
                    label="You", placeholder="Type a message...", lines=1
                )
            with gr.Column(scale=1):
                send_button = gr.Button("Send")
                new_conversation_button = gr.Button("Start New Conversation")

        send_button.click(respond, inputs=[user_input, chatbot_component], outputs=[chatbot_component, user_input])
        user_input.submit(respond, inputs=[user_input, chatbot_component], outputs=[chatbot_component, user_input])
        new_conversation_button.click(reset_chat, outputs=[chatbot_component, user_input])

    return demo


if __name__ == "__main__":
    interface = build_interface()
    interface.launch()
