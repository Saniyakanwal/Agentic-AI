from agents import Agent
from my_config.gemini_config import Model

next_js_assistant = Agent(
    name= "Next js Asssistant",
    instructions= "Your are helpful next js assistant",
    model= Model
)

python_assistant = Agent(
     name= "Python Asssistant",
    instructions= "Your are helpful python assistant",
    model= Model
)

triage_agent = Agent(
    name= "Triage Agent",
    instructions="You are helpful assistant handoff the request to the correct agent according to the query.",
    handoffs=[next_js_assistant,python_assistant],
    model= Model
)