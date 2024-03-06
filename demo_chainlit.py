import os
import chainlit as cl
# from test import Greetings
from punjabi import reply









@cl.on_chat_start
async def on_chat_start():
    cl.Message(
        content="A new chat session has started!",
    ).send()



@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content= reply(message.content),
    ).send()



# cl.session_state.session_id
# cl.user_session.get("id")
