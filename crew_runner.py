# crew_runner.py
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool, FileWriteTool, DirectoryReadTool, CodeDocsSearchTool
import os, subprocess

REPO = os.getcwd()
SAFE_DIRS = [
    "api", "web", "scripts", "neo4j",
    "docker-compose.yml", "Dockerfile*", "requirements*.txt", "package*.json",
    "*.md", "TASKS.md", "DESIGN.md", "PROGRESS.md"
]

system_guardrails = f"""
You are a senior full-stack engineer building Mark's movie collection management system.
Follow PLAN.md step-by-step, using DATAMODEL.md for data structure guidance.

CORE REQUIREMENTS:
- Build Neo4j graph database with Movie, Person, Genre, ProductionCompany nodes
- Create FastAPI backend with full CRUD operations
- Develop React frontend with relationship visualization
- Implement dockerized deployment with docker-compose

DEVELOPMENT STANDARDS (from GUARDRAILS.md):
- Only modify files under: {SAFE_DIRS}
- Use conventional commits: feat(api): add movie CRUD, fix(web): resolve validation
- Implement Neo4j constraints and indexes based on DATAMODEL.md
- Write tests before features, maintain >80% coverage
- Update PROGRESS.md every 30 minutes with current task and next steps
- If commands fail, fix and retry (explain what changed)

TECHNICAL STACK:
- Backend: FastAPI + Neo4j + Pydantic models from DATAMODEL.md
- Frontend: React + TypeScript with relationship graphs
- Database: Neo4j with Cypher queries for movie relationships
- Deployment: Docker containers with docker-compose orchestration
"""

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=REPO)

researcher = Agent(
    role="Movie Collection Planner",
    goal="Read PLAN.md, GUARDRAILS.md, and DATAMODEL.md to create detailed TASKS.md with phased implementation checklist for Mark's movie database.",
    backstory="You specialize in breaking down complex movie database projects into actionable, time-estimated tasks while ensuring Neo4j graph relationships are properly planned.",
    verbose=True,
    allow_delegation=False
)

architect = Agent(
    role="Movie Database Architect",
    goal="Design Neo4j database schema, FastAPI endpoints, and React components based on DATAMODEL.md relationships and PLAN.md requirements.",
    backstory="You design scalable movie database architectures with optimized Neo4j queries for relationship traversal and complex movie network analysis.",
    verbose=True,
    allow_delegation=False
)

coder = Agent(
    role="Movie Collection Developer",
    goal="Implement Neo4j database setup, FastAPI CRUD endpoints, and React components following GUARDRAILS.md standards with comprehensive testing.",
    backstory="You build movie database applications with Neo4j graph operations, FastAPI REST APIs, and React interfaces while maintaining high code quality and test coverage.",
    verbose=True,
    allow_delegation=False,
    tools=[
        FileReadTool(), FileWriteTool(), DirectoryReadTool(),
    ]
)

tester = Agent(
    role="Movie Database QA Engineer",
    goal="Create comprehensive test suites for Neo4j operations, FastAPI endpoints, and React components ensuring >80% coverage and docker-compose functionality.",
    backstory="You ensure movie database applications are thoroughly tested with Neo4j integration tests, API endpoint validation, and end-to-end user workflows.",
    verbose=True,
    allow_delegation=False,
    tools=[FileReadTool(), FileWriteTool(), DirectoryReadTool()]
)

tasks = [
    Task(
        description="Read PLAN.md, GUARDRAILS.md, and DATAMODEL.md. Create detailed TASKS.md with 6-phase implementation plan for Mark's movie collection system including time estimates for each task.",
        agent=researcher,
        expected_output="TASKS.md with phased checklist and time estimates"
    ),
    Task(
        description="Design Neo4j schema with constraints/indexes, FastAPI endpoint specifications, and React component architecture based on DATAMODEL.md relationships. Write DESIGN.md with API contracts.",
        agent=architect,
        expected_output="DESIGN.md with Neo4j schema, API specs, and UI architecture"
    ),
    Task(
        description="Execute Phase 1-4 implementation: Set up /api and /web directories, configure Neo4j, build FastAPI CRUD endpoints for movies/persons/genres, create React components with relationship visualization. Use conventional commits and update PROGRESS.md every 30 minutes.",
        agent=coder,
        expected_output="Working movie collection app with Neo4j backend and React frontend"
    ),
    Task(
        description="Create comprehensive test suites for Neo4j operations, FastAPI endpoints, and React components. Build docker-compose environment, write scripts/test.sh, ensure >80% coverage and green test runs.",
        agent=tester,
        expected_output="Complete test suite and dockerized deployment ready for production"
    )
]

crew = Crew(
    agents=[researcher, architect, coder, tester],
    tasks=tasks,
    process=Process.sequential,
    cache=False,
    max_rpm=60,   # keep it gentle
    max_steps=100 # budget the work
)

if __name__ == "__main__":
    # seed repo status and create initial PROGRESS.md
    sh('git add . && git commit -m "chore: baseline" || true')
    sh('echo "# Progress Log\\n\\n## $(date)\\n- Initialized crew runner for Mark\'s movie collection system\\n- Ready to execute PLAN.md phases" > PROGRESS.md')
    result = crew.kickoff(inputs={"guardrails": system_guardrails})
    print(result)
