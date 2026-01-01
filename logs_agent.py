from strands import Agent #Imports agentic framework
from strands.models.ollama import OllamaModel
from strands_tools import file_read

SYSTEM_PROMPT = """
You are a Log Analysis Agent.
You are excellent in reading and understanding the log files i.e (.log / var/www/ /system log, etc)
You can deduce results in short and crisp manner
You are helpful and use a DevOps Mindset in Log Analaysis and Root Cause Analysis
You won't hallucinate and suggest new changes.
You will not engage in any production actions, but suggest changes and ideas to DevOps Engineers.
"""


# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.2"               # Specify which model to use
)


#Call Ollama LLMs
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=ollama_model,
    tools=[file_read]
)


agent("Detect how many times the INFO, WARNING and ERROR occurs and return their counts only from app.log")

