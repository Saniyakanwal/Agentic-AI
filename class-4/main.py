from agents import Runner , set_tracing_disabled
from my_agents.my_agent import agent
from my_agents.handoff_agent import triage_agent

set_tracing_disabled(True)

# res = Runner.run_sync(starting_agent= agent,input = "100 plus 20 ")
res = Runner.run_sync(
    starting_agent= triage_agent,
    input= "mujhe python ki routing k hawale se help chahye"
)

print(res.final_output)
print(res.last_agent)# konsa agent ans karha hai

# res = Runner.run_streamed(
    # starting_agent= triage_agent,
    # input= "mujhe nextjs ki routing k hawale se help chahye"
# )
# async for next in res.stream_events():
    #   print("event>>>>>",event)

# Runner.run_sync
# Runner.run
# Runner.run_streamed
# print(res.last_agent)
# print(res.final_output)


