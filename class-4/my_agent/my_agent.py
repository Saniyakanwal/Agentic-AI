from agents import Agent
from my_config.gemini_config import Model
from my_tool.accounts import multiply,plus

agent = Agent(name = "Ratan lal", instructions = "You are helpful assistant",
model= Model,tools=[plus,multiply], tool_use_behavior="run_llm_again")

