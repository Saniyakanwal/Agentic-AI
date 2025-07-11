from agents import function_tool

@function_tool
def fetch_weather(city:str) -> str:

 """
 fetch the weather data
 """
 return f"The weather in {city} is sunny"