# Development Guardrails

## Core Principles
- **Incremental Development**: Follow PLAN.md step-by-step. Complete one task before moving to the next.
- **Test-Driven Development**: Write tests before implementing features. Run tests frequently.
- **Code Quality**: Maintain high standards with linting, formatting, and documentation.
- **Security First**: Implement security best practices from the start.

## File System Restrictions

### Safe Directories
Only modify files within these approved directories:
- `/api` - FastAPI backend code
- `/web` - React frontend code
- `/scripts` - Utility and deployment scripts
- `docker-compose.yml` - Container orchestration
- `Dockerfile.*` - Container definitions
- `requirements*.txt` - Python dependencies
- `package*.json` - Node.js dependencies
- `*.md` - Documentation files

### Restricted Areas
**NEVER modify:**
- Root-level configuration files (unless explicitly approved)
- Database files or Neo4j data directories
- System-level configurations
- Third-party dependencies
- Production deployment files (until Phase 5)

## Development Workflow

### Commit Strategy
- Use conventional commit format:
  ```
  type(scope): description

  Types: feat, fix, docs, style, refactor, test, chore
  Examples:
  - feat(api): add movie search endpoint
  - fix(web): resolve form validation error
  - test(api): add movie CRUD integration tests
  - docs: update API documentation
  ```

### Branch Management
- `main`: Production-ready code (only merge via PR)
- `develop`: Integration branch for feature testing
- `feature/*`: Individual feature branches
- Never commit directly to `main` or `develop`

### Pull Request Requirements
- All PRs require code review
- Must pass all CI checks (linting, tests, security scans)
- Include test coverage for new features
- Update documentation if APIs change

## Code Quality Standards

### Backend (FastAPI/Python)
- **Linting**: Use `black` for formatting, `flake8` for style
- **Type Hints**: Required for all function parameters and return types
- **Docstrings**: Use Google-style docstrings for all public functions
- **Error Handling**: Implement proper exception handling with custom error responses
- **Validation**: Use Pydantic models for all API inputs/outputs
- **Logging**: Use structured logging with appropriate levels

### Frontend (React/TypeScript)
- **TypeScript**: Strict mode enabled, no `any` types
- **Component Structure**: Use functional components with hooks
- **State Management**: Use React Query for server state, Context for global state
- **Styling**: Consistent design system (Material-UI or Tailwind)
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Lazy loading, code splitting, memoization

### Database (Neo4j)
- **Query Optimization**: Use EXPLAIN ANALYZE for complex queries
- **Constraints**: Define unique constraints and existence constraints
- **Indexes**: Create indexes for frequently queried properties
- **Transactions**: Use transactions for multi-step operations
- **Error Handling**: Proper handling of database connection issues

## Testing Requirements

### Test Coverage
- **Backend**: >80% coverage for API endpoints and business logic
- **Frontend**: >70% coverage for components and utilities
- **Integration**: Full coverage for critical user journeys
- **E2E**: Key user workflows tested with Cypress

### Test Types Required
- **Unit Tests**: Individual functions and components
- **Integration Tests**: API endpoints with Neo4j
- **End-to-End Tests**: Complete user workflows
- **Performance Tests**: Search and data loading operations

### Test Execution
- Run tests before every commit
- Run full test suite before merging to develop
- Automated testing in CI/CD pipeline

## Security Guardrails

### Authentication & Authorization
- Implement JWT-based authentication for user management
- Role-based access control (Mark as admin, family as users)
- Secure password hashing with bcrypt
- Session management with proper timeouts

### API Security
- Input validation and sanitization
- Rate limiting on public endpoints
- CORS properly configured for frontend origin
- HTTPS required for all external communications

### Data Protection
- Encrypt sensitive data at rest
- Implement data backup and recovery procedures
- GDPR compliance for personal data handling
- Secure API keys and environment variables

## Performance Standards

### Response Times
- API endpoints: <500ms for simple queries, <2s for complex operations
- Frontend page loads: <2s initial load, <1s subsequent loads
- Search operations: <300ms for local search, <1s for full database search

### Scalability
- Support for 10,000+ movies and relationships
- Efficient pagination for large result sets
- Database query optimization for complex relationships
- Frontend virtualization for large lists

## Error Handling & Monitoring

### Error Responses
- Consistent error format across all APIs
- Appropriate HTTP status codes
- User-friendly error messages
- Detailed logging for debugging

### Monitoring
- Application performance monitoring
- Database query performance tracking
- Error tracking and alerting
- User analytics and usage patterns

## Documentation Requirements

### API Documentation
- OpenAPI/Swagger documentation for all endpoints
- Example requests and responses
- Authentication requirements documented
- Rate limiting and error codes explained

### Code Documentation
- README files for setup and deployment
- Inline comments for complex logic
- Architecture decision records (ADRs)
- Database schema documentation

## Deployment Guardrails

### Environment Management
- Separate configurations for development, staging, production
- Environment variables for sensitive data
- Database backups before deployments
- Rollback procedures documented

### Docker Best Practices
- Minimal base images
- Multi-stage builds for optimization
- Proper security scanning
- Resource limits and health checks

## Risk Mitigation

### Development Risks
- **Scope Creep**: Stick to PLAN.md tasks only
- **Technical Debt**: Regular refactoring sessions
- **Integration Issues**: Daily integration testing
- **Knowledge Silos**: Pair programming for complex features

### Operational Risks
- **Data Loss**: Automated backups and recovery testing
- **Performance Degradation**: Regular performance monitoring
- **Security Vulnerabilities**: Dependency scanning and updates
- **Downtime**: Blue-green deployment strategy

## Communication & Collaboration

### Progress Tracking
- Update PROGRESS.md every 30 minutes with current status
- Document blockers and decisions
- Share learnings and best practices
- Regular status updates for stakeholders

### Code Review Process
- Constructive feedback focused on code quality
- Knowledge sharing during reviews
- Automated checks don't replace human review
- Approve only when standards are met

These guardrails ensure high-quality, maintainable code while following best practices for full-stack development with Neo4j, FastAPI, and React.
