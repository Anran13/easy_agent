from google.adk.agents import Agent
from . import weather_prompt as prompt
from .weather_tool import get_taipei_current_temperature
from dotenv import load_dotenv

load_dotenv()

weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description=prompt.WEATHER_AGENT_DESCRIPTION,
    instruction=prompt.WEATHER_AGENT_INSTRUCTION,
    tools=[get_taipei_current_temperature],
)