from crewai import Task
def build_risk_task(agent,data):
    return Task(description=f"Assess risks: {data}",agent=agent)
