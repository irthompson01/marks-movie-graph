# crew_runner.py
from crewai import Agent, Task, Crew, Process
import os, subprocess

REPO = os.getcwd()

system_guardrails = """
You are a senior full-stack engineer building Mark's movie collection management system.
Follow PLAN.md step-by-step, using DATAMODEL.md for data structure guidance.
- Only modify files in this repo.
- Small, verifiable steps; clear headings and checklists.
"""

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=REPO)

researcher = Agent(
    role="Movie Collection Planner",
    goal="Create a detailed, phased task plan with estimates based on PLAN.md, GUARDRAILS.md, DATAMODEL.md.",
    backstory="You break complex builds into actionable steps.",
    verbose=True,
    allow_delegation=False,
)

architect = Agent(
    role="Movie Database Architect",
    goal="Design Neo4j schema, FastAPI endpoints, and React components; write clear API contracts.",
    backstory="You design scalable graph-backed apps.",
    verbose=True,
    allow_delegation=False,
)

# NOTE: No tools yet; get files written via output_file on tasks

tasks = [
    Task(
        description="Read PLAN.md, GUARDRAILS.md, and DATAMODEL.md. Create TASKS.md with a 6-phase plan and time estimates. Include explicit acceptance checks per phase.",
        agent=researcher,
        expected_output="TASKS.md with phased checklist and estimates",
        output_file="TASKS.md",
    ),
    Task(
        description="Propose Neo4j constraints/indexes, API route specs, and React components. Produce DESIGN.md with data contracts and example payloads.",
        agent=architect,
        expected_output="DESIGN.md with schema, API specs, UI architecture",
        output_file="DESIGN.md",
    ),
]

crew = Crew(
    agents=[researcher, architect],
    tasks=tasks,
    process=Process.sequential,
    cache=False,
    max_rpm=60,
    max_steps=50
)

if __name__ == "__main__":
    sh('git add . && git commit -m "chore: baseline" || true')
    result = crew.kickoff(
        inputs={"guardrails": system_guardrails}
    )
    print(result)
