from crewai import Task
def build_extraction_task(agent,text):
    return Task(description=f"Extract financial metrics from: {text}",agent=agent)
