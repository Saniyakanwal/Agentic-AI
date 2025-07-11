from agents import Agent
from my_config.gemini_config import Model
from my_tool.weather_tool import fetch_weather

weather_agent = Agent (
    name= "Weather Assistant",
    instructions= "You are helpful weather assistant by calling fetch_weather tool",
    model= Model,
    tools= [fetch_weather])