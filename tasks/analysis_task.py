from crewai import Task
def build_analysis_task(agent,data):
    return Task(description=f"Analyze financial health: {data}",agent=agent)
