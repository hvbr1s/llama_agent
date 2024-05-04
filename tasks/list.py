from crewai import Task
from crew.agents import researcher

# Research task
research_issue= Task(
  description=(
    """
    Use your Knowledge base tool to find the best answer to: {topic}.
    ALWAYS use your Knowledge Base tool to answer {topic}.
    If the retrieved data doesn't answer the question, adapt the query and use your Knowledge base tool again.
    Keep looking until you find information that correctly answers: {topic}. 
    Discard the parts that are not useful. Make sure to always cite your sources by adding a plain URL link (no markdown)"""
  ),
  expected_output='A short summary of the EXACT part or parts of the documentation that answers: {topic}. Discard the parts that are not useful to answering the query.',
  agent=researcher,
  async_execution=False,

)
