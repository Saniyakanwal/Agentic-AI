# import asyncio
# from agents import  Runner
# from my_agents.teacher import math_teacher


# async def main():
#     result = await Runner.run(math_teacher,"Plus 10 in 100?")
#     print(result.final_output)

# asyncio.run(main())

from agents import Agent,OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key= gemini_api_key, base_url= gemini_base_url)
model = OpenAIChatCompletionsModel(openai_client= client, model = str
(gemini_model_name))

agent:Agent = Agent(
    name = "Math Agent",
    instructions="""
    -You are helpful math agent
    -you can solve complex math questions and expression
    -Do Not answer if request is not about math questions
    -Do Not generate answer on yourself if question are not about math
    -you can simply refuse the answer if you dont know
    """,
    model = model
)

# prompt = input("Enter your number")
result = Runner.run_sync(agent, "sum of 2 and 4")
print(result.final_output)