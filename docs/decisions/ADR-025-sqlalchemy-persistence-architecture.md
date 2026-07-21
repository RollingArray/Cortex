# ADR-025: SQLAlchemy Persistence Architecture

## Status

Accepted

---

## Context

Cortex requires a persistence framework capable of supporting an evolving enterprise AI platform while maintaining a clean separation between domain logic and database implementation.

The persistence layer must satisfy several architectural goals:

- Support complex domain relationships
- Provide provider-independent persistence
- Integrate naturally with the Service Layer architecture
- Support multiple database engines
- Enable future schema evolution through migrations
- Maintain strong typing and modern Python development practices

Rather than writing raw SQL or tightly coupling business logic to a specific database technology, Cortex requires an Object-Relational Mapping (ORM) solution that promotes maintainability, extensibility, and consistency.

---

## Decision

Adopt SQLAlchemy 2.x as the primary persistence framework for Cortex.

The persistence architecture consists of four layers:

1. SQLAlchemy ORM Models
2. Repository Layer
3. Service Layer
4. Database Provider

SQLite will be used for local development.

PostgreSQL is the target production database.

Database-specific implementation details remain isolated from the business domain.

---

## Architecture

```text
                API Layer
                    │
                    ▼
             Service Layer
                    │
                    ▼
           Repository Layer
                    │
                    ▼
            SQLAlchemy ORM
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   SQLite (Development)   PostgreSQL (Production)
```

The application communicates exclusively through repositories and services.

Business logic never directly interacts with SQLAlchemy sessions.

---

## Responsibilities

### SQLAlchemy ORM

Responsible for:

- Object-relational mapping
- Relationship management
- Query generation
- Change tracking

Not responsible for:

- Business logic
- Authorization
- Validation
- API contracts

---

### Repository Layer

Responsible for:

- Database access
- Query execution
- Persistence operations
- Transaction boundaries

Not responsible for:

- Business rules
- Request validation
- AI workflows

---

### Service Layer

Responsible for:

- Business logic
- Domain orchestration
- Repository coordination
- Validation

Not responsible for:

- SQL generation
- Session management

---

### Database Provider

Responsible for:

- Physical data storage
- Transaction durability
- Constraint enforcement
- Query execution

Not responsible for:

- Domain modeling
- Business workflows

---

## Design Principles

### ORM Abstraction

Business logic remains independent of SQL syntax.

Repositories expose domain operations rather than database operations.

---

### Repository Pattern

All persistence operations flow through repositories.

Direct database access outside repositories is prohibited.

---

### Strong Typing

All entities use SQLAlchemy 2.x typed mappings.

Example:

```python
name: Mapped[str]
documents: Mapped[list["Document"]]
```

This improves readability, IDE support, and static analysis.

---

### Database Independence

The domain model remains independent of the underlying database engine.

Development and production databases may differ without requiring application changes.

---

### Explicit Relationships

Relationships are explicitly defined.

Each relationship specifies:

- Cardinality
- Loading strategy
- Cascade behavior
- Bidirectional navigation

---

### Explicit Constraints

Constraints and indexes are defined within the ORM model.

This ensures the model accurately represents database behavior.

---

## Consequences

### Positive

- Strong separation of concerns
- Provider-independent persistence
- Excellent Python ecosystem support
- Modern type-safe ORM
- Reduced SQL boilerplate
- Easier testing
- Simplified repository implementation
- Clear relationship management

### Negative

- ORM learning curve
- Additional abstraction layer
- Complex queries may require ORM optimization
- Database migrations require ongoing management

---

## Alternatives Considered

### Raw SQL

Pros

- Maximum control
- Potentially simpler SQL optimization

Cons

- High maintenance
- Business logic becomes database-aware
- Reduced portability

---

### SQLModel

Pros

- Simplified syntax
- Pydantic integration

Cons

- Smaller ecosystem
- Less mature for complex enterprise architectures

---

### Django ORM

Pros

- Mature framework
- Rich feature set

Cons

- Tightly coupled to Django
- Unsuitable for FastAPI-first architecture

---

### No Repository Layer

Pros

- Less code

Cons

- SQLAlchemy becomes tightly coupled to business logic
- Difficult testing
- Reduced maintainability

---

## Future Considerations

Future persistence improvements may include:

- Alembic schema migrations
- Read/write database separation
- Connection pooling optimization
- Multi-database support
- Query performance monitoring
- Database sharding
- Multi-tenant persistence

The persistence architecture should remain stable while supporting these enhancements.

---

## Related Decisions

- ADR-003: API-First Architecture
- ADR-013: Service Layer Pattern
- ADR-024: Domain-Driven Persistence Model

---

## Outcome

This decision establishes SQLAlchemy as the persistence foundation for Cortex.

All persistence operations follow a consistent architectural path.

```text
Before

API
 │
 ▼
Database

After

API
 │
 ▼
Service
 │
 ▼
Repository
 │
 ▼
SQLAlchemy ORM
 │
 ▼
Database
```

This architecture provides a scalable, provider-independent persistence layer that supports future database evolution while maintaining a clear separation between business logic and infrastructure.

---

## Implementation Status

| Component | Status |
|-----------|--------|
| SQLAlchemy 2.x | Complete |
| Typed ORM Models | Complete |
| Repository Pattern | Complete |
| Session Management | Complete |
| SQLite Development Support | Complete |
| PostgreSQL Target Architecture | Complete |
| Alembic Integration | Planned |
| Read/Write Separation | Planned |
| Documentation | Complete |
| Production Ready | In Progress |