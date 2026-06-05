from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME
def get_financial_agent():
    return Agent(role="Financial Analyst",goal="Analyze company performance",backstory="Banking analyst",llm=ChatOpenAI(model=MODEL_NAME),verbose=True)
