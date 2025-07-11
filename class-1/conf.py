from agents import OpenAIChatCompletionsModel
from decouple import config
from openai import AsyncOpenAI


my_key = config("GEMINI_API_KEY")

client = AsyncOpenAI(api_key= my_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

MODEL = OpenAIChatCompletionsModel(model = "Gemini 2.5 Flash",
openai_client= client)