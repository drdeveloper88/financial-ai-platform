from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME
def get_document_agent():
    return Agent(role="Document Extraction Agent",goal="Extract financial information",backstory="Expert in annual reports",llm=ChatOpenAI(model=MODEL_NAME),verbose=True)
