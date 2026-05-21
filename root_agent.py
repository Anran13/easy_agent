from google.adk.agents import Agent
from . import root_prompt as prompt
from dotenv import load_dotenv
from .hello_agent import hello_agent
from .weather_agent import weather_agent
load_dotenv()


root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description=prompt.ROOT_AGENT_DESCRIPTION,
    instruction=prompt.ROOT_AGENT_INSTRUCTION,
    sub_agents= [
        hello_agent,
        weather_agent
    ]
)