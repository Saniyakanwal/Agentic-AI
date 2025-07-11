from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel


key = config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")

client = AsyncOpenAI(api_key= key, base_url=base_url)

Model = OpenAIChatCompletionsModel(model = "gemini-1.5-flash",openai_client= client)