from agents import Agent,ModelSettings
from agents.agent import StopAtTools
from my_config.gemini_config import Model
from my_tool.my_tools import plus,subtract
# from my_schema.agent_output import MyDataOutput
# from dataclasses import dataclass

# @dataclass
# class MyData:
#    # n1:int = None # optional
#     n1:int
#     n2:int
#     res:int


math_agent = Agent(
              name= "math teacher", 
              instructions= "you are my assistant.", 
              model= Model,
              tools= [plus,subtract],
              # tool_use_behavior="stop_on_first_tool",
              # tool_use_behavior=StopAtTools(stop_at_tool_names= ["subtract"])
            model_settings= ModelSettings(tool_choice="required")
            )

agent = Agent(
              name= "teacher", 
              instructions= "you are my assistant.", 
              model= Model,
              tools=[math_agent.as_tool(tool_name="math_teacher",
              tool_description="You are math teacher.")]
)