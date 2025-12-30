from strands import Agent #Imports agentic framework
from strands_tools import http_request

agent = Agent(tools=[http_request]) #Calls AWS BedRock LLMS

agent("What's today's date? Use free api")
