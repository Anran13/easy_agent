from google.adk.agents import Agent
from . import hello_prompt as prompt
from dotenv import load_dotenv

load_dotenv()

hello_agent = Agent(
    name="hello_agent",
    model="gemini-2.5-flash",
    description=prompt.HELLO_AGENT_DESCRIPTION,
    instruction=prompt.HELLO_AGENT_INSTRUCTION
)