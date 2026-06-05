from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME
def get_report_agent():
    return Agent(role="Executive Report Generator",goal="Create executive summaries",backstory="Reporting expert",llm=ChatOpenAI(model=MODEL_NAME),verbose=True)
