# Development Plan: Mark's Movie Graph

## Overview
Build a full-stack application for managing Mark's DVD/BluRay collection using Neo4j, FastAPI, and React. The application will provide CRUD operations, relationship visualization, and personal note-taking capabilities.

## Project Structure
```
/api (FastAPI backend)
/web (React frontend)
/docker-compose.yml (full stack orchestration)
/neo4j (database configuration)
/scripts (utility scripts)
```

## Phase 1: Project Setup & Infrastructure

### Task 1.1: Directory Structure Setup
- Create `/api` directory with FastAPI project structure
- Create `/web` directory with React project structure
- Initialize git repository with proper .gitignore
- Set up virtual environments for Python and Node.js
- Create initial `docker-compose.yml` with Neo4j, API, and web services

### Task 1.2: Neo4j Configuration
- Configure Neo4j Docker service with authentication
- Create database initialization scripts
- Set up Neo4j constraints and indexes based on DATAMODEL.md
- Test Neo4j connection and basic operations

### Task 1.3: Backend Foundation (FastAPI)
- Initialize FastAPI project with dependencies:
  - `fastapi`, `uvicorn`, `neo4j-driver`
  - `pydantic` for data validation
  - `python-multipart` for file uploads
- Set up basic CORS configuration
- Create database connection utilities
- Implement health check endpoint (`GET /health`)

## Phase 2: Core Backend API Development

### Task 2.1: Movie CRUD Operations
- Create Pydantic models for Movie based on DATAMODEL.md
- Implement endpoints:
  - `GET /movies` - List all movies with pagination and filtering
  - `GET /movies/{id}` - Get movie details with relationships
  - `POST /movies` - Create new movie
  - `PUT /movies/{id}` - Update movie
  - `DELETE /movies/{id}` - Delete movie
- Add search functionality by title, year, genre
- Implement movie import from TMDB/IMDB APIs

### Task 2.2: Person Management
- Create Person CRUD endpoints:
  - `GET /persons` - List persons with roles
  - `GET /persons/{id}` - Get person details with filmography
  - `POST /persons` - Create person
  - `PUT /persons/{id}` - Update person
  - `DELETE /persons/{id}` - Delete person
- Implement role-based filtering (actors, directors, producers)

### Task 2.3: Relationship Management
- Create relationship endpoints:
  - `POST /movies/{id}/cast` - Add actor to movie
  - `POST /movies/{id}/crew` - Add crew member to movie
  - `POST /movies/{id}/genres` - Add genres to movie
  - `DELETE /movies/{id}/relationships/{type}/{target_id}` - Remove relationships
- Implement bulk relationship operations

### Task 2.4: Genre and Production Company Management
- Create Genre CRUD endpoints
- Create ProductionCompany CRUD endpoints
- Implement relationship endpoints for both

## Phase 3: Advanced Backend Features

### Task 3.1: Search and Filtering
- Implement advanced search with multiple criteria
- Add fuzzy search for titles and names
- Create recommendation endpoints based on relationships
- Implement graph traversal queries for "related movies"

### Task 3.2: Data Import/Export
- Create CSV import functionality for bulk movie addition
- Implement TMDB API integration for movie data enrichment
- Add export functionality for backup/collection sharing

### Task 3.3: User Management & Personalization
- Add user authentication (Mark + family members)
- Implement personal ratings and notes
- Create watch history tracking
- Add user-specific filtering and recommendations

## Phase 4: Frontend Development (React)

### Task 4.1: React Setup and Foundation
- Initialize React project with TypeScript
- Set up routing with React Router
- Configure API client (Axios or React Query)
- Create basic layout components (Header, Navigation, Footer)
- Implement theme and styling (Material-UI or Tailwind CSS)

### Task 4.2: Movie Management Interface
- Create movie list page with search and filters
- Build movie detail page with relationships display
- Implement add/edit movie forms with validation
- Add bulk import interface
- Create movie card components for grid/list views

### Task 4.3: Person and Relationship Management
- Build person detail pages with filmography
- Create relationship editing interfaces
- Implement visual relationship graphs (using D3.js or vis.js)
- Add person search and filtering

### Task 4.4: Dashboard and Analytics
- Create main dashboard with collection statistics
- Build genre distribution charts
- Implement recently added/watched sections
- Add search analytics and recommendations

## Phase 5: Integration and Dockerization

### Task 5.1: Full Stack Integration
- Connect frontend to backend APIs
- Implement error handling and loading states
- Add offline support for critical features
- Test end-to-end functionality

### Task 5.2: Docker Configuration
- Create optimized Dockerfiles for API and web services
- Configure docker-compose with proper networking
- Set up volume mounts for data persistence
- Implement environment-based configuration

### Task 5.3: Production Deployment
- Add reverse proxy (nginx) configuration
- Implement SSL/TLS certificates
- Set up monitoring and logging
- Create deployment scripts

## Phase 6: Testing and Quality Assurance

### Task 6.1: Backend Testing
- Write unit tests for all API endpoints
- Create integration tests for Neo4j operations
- Implement data validation tests
- Add performance tests for search operations

### Task 6.2: Frontend Testing
- Write component tests with React Testing Library
- Create end-to-end tests with Cypress
- Implement accessibility testing
- Add cross-browser compatibility tests

### Task 6.3: System Testing
- Test docker-compose deployment
- Verify data persistence across restarts
- Test backup and restore functionality
- Performance testing with large datasets

## Development Workflow

### Commit Strategy
- Use conventional commit messages:
  - `feat(api): add movie search endpoint`
  - `fix(web): resolve movie form validation`
  - `docs: update API documentation`
  - `test: add movie CRUD tests`

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch
- `feature/*`: Feature branches (e.g., `feature/movie-crud`)
- `hotfix/*`: Bug fixes

### Code Quality
- Run linters on every commit (black, flake8, eslint)
- Maintain test coverage > 80%
- Code review required for all PRs
- Update documentation with code changes

## Success Criteria

### Functional Requirements
- ✅ Add, edit, delete movies with all properties
- ✅ Manage relationships between movies, people, genres
- ✅ Search and filter collection by multiple criteria
- ✅ Import movie data from external APIs
- ✅ Export collection data
- ✅ Visual relationship graphs
- ✅ Personal notes and ratings
- ✅ Watch history tracking

### Technical Requirements
- ✅ FastAPI backend with Neo4j integration
- ✅ React frontend with responsive design
- ✅ Full dockerization with docker-compose
- ✅ Comprehensive test coverage
- ✅ RESTful API design
- ✅ TypeScript for type safety
- ✅ Proper error handling and validation

### Performance Requirements
- ✅ Page load times < 2 seconds
- ✅ Search queries < 500ms
- ✅ Support for 10,000+ movies
- ✅ Concurrent user support (Mark + family)

## Risk Mitigation

### Technical Risks
- Neo4j query performance with large datasets → Implement pagination and indexing
- Complex relationship queries → Design efficient Cypher queries
- API rate limits for external services → Implement caching and fallbacks

### Development Risks
- Scope creep → Strict adherence to phased development
- Integration issues → Regular integration testing
- Data consistency → Implement proper validation and constraints

This plan provides a structured approach to building Mark's movie collection management system, ensuring both functionality and maintainability.
