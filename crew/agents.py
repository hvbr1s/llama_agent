import os
from dotenv import main
from crewai import Agent
from tools.retrieve_tool import retriever_tool
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.agents import load_tools

human_tools = load_tools(["human"])

focused_llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.0
)

creative_llm = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.2
)

groq =  ChatGroq(
            api_key=os.environ['GROQ_API_KEY'],
            model="llama3-70b-8192"
        )

# Load secrets
main.load_dotenv()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Senior Researcher',
  goal='ALWAYS use your Knowledge Base tool to find technical documentation that can help with technical issues related to Ledger products.',
  verbose=True,
  memory=True,
  backstory=(
    """
    Driven by curiosity, you're at the forefront of cybersecurity applied to blockchain and an expert in Ledger products including the Ledger Nano S Plus, Nano X, Ledger Stax and the Ledger Live app.
      
    """
  ),
  tools=[retriever_tool],
  allow_delegation=False,
  llm=groq,
  max_iter=10,
  max_execution_time= 60
)
