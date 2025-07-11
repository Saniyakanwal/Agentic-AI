import chainlit as cl
from main import math_agent
from agents import Runner


@cl.on_message
async def main(message: cl.Message):
    # my prompt
    prompt = message.content
    # agent get
    result = Runner.run_sync(math_agent, prompt) 
    await cl.Message(content = f"AI-Response: {result.final_output}").send()