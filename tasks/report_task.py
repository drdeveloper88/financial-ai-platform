from crewai import Task
def build_report_task(agent,data):
    return Task(description=f"Generate executive report: {data}",agent=agent)
