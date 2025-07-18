from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner

key = config("GEMINI_API_KEY")
base_url = config("GEMINI_BASE_URL")

client = AsyncOpenAI(api_key= key, base_url=base_url)

Model = OpenAIChatCompletionsModel(model = "gemini-1.5-flash",openai_client= client)

agent = Agent(name = "Ratan lal", instructions = "You are helpful assistant",model= Model)

res = Runner.run_sync(agent, input="plus 10 + 20",)

print(res.final_output)