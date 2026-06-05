from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME
def get_risk_agent():
    return Agent(role="Risk Assessment Agent",goal="Identify risks",backstory="Risk specialist",llm=ChatOpenAI(model=MODEL_NAME),verbose=True)
