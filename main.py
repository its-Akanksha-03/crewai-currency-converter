import os
from crewai import Agent, Task, Crew, LLM

# Use Ollama as the provider
llm = LLM(
    model="ollama/llama2",   # Make sure you already pulled this model with: ollama pull llama2
    provider="ollama"
)

# Define an agent
agent = Agent(
    role="AI Assistant",
    goal="Answer questions clearly and helpfully",
    backstory="You are a helpful assistant running on Ollama LLaMA2.",
    llm=llm
)

# Define a task for the agent
task = Task(
    description="Explain what CrewAI is in simple words.",
    agent=agent
)

# Create a crew with the task
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True  # This ensures logs are shown
)

# Run the crew
result = crew.kickoff()
print("\n=== RESULT ===\n")
print(result)
