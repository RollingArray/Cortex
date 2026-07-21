# ADR-024: Domain-Driven Persistence Model

## Status

Accepted

---

## Context

As Cortex evolved from a proof-of-concept into an enterprise AI platform, a consistent persistence strategy became necessary.

Early development focused on establishing API contracts, service abstractions, AI provider interfaces, and retrieval workflows. However, no architectural decision existed to standardize how domain entities should be represented and persisted.

Without a common persistence model, each entity risked defining its own conventions for:

- Identity
- Auditing
- Ownership
- Soft deletion
- Relationships
- Constraints
- Naming conventions

This would introduce inconsistency across the domain model, increase maintenance effort, and make future entities more difficult to implement.

Cortex requires a reusable persistence model that provides consistency across all domain entities while remaining independent of specific business capabilities.

---

## Decision

Adopt a domain-driven persistence model based on reusable persistence traits.

Every persistent entity shall inherit common capabilities through shared base classes rather than duplicating infrastructure fields.

The persistence model standardizes:

- Entity identity
- Auditing
- Ownership
- Soft deletion
- Relationship modeling
- Constraint naming
- Indexing strategy
- Enum persistence

Business entities focus solely on domain-specific behavior while infrastructure concerns remain centralized.

---

## Architecture

```text
                    Base
                      │
                      ▼
                 SQLAlchemy ORM
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
     Entity      Auditable      Ownable
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
               SoftDeletable
                      │
                      ▼
              Business Entity
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
    Workspace                  Document
```

Each domain entity composes persistence capabilities through inheritance rather than implementing them individually.

---

## Responsibilities

### Entity

Responsible for:

- Globally unique identifiers
- Primary key definition

Not responsible for:

- Auditing
- Ownership
- Business rules

---

### Auditable

Responsible for:

- Creation timestamp
- Modification timestamp

Not responsible for:

- Ownership
- Deletion lifecycle

---

### Ownable

Responsible for:

- Creator identity
- Last modifier identity

Not responsible for:

- Authorization
- Access control

---

### SoftDeletable

Responsible for:

- Logical deletion
- Deletion audit information

Not responsible for:

- Physical record removal

---

### Business Entities

Responsible for:

- Domain attributes
- Relationships
- Business constraints

Not responsible for:

- Infrastructure concerns
- Audit implementation
- Identifier generation

---

## Design Principles

### Separation of Concerns

Infrastructure concerns are implemented once through reusable persistence traits.

Business entities remain focused on domain behavior.

---

### Consistency

Every persistent entity follows the same persistence conventions.

This ensures predictable implementation across the entire platform.

---

### Explicit Constraints

Primary keys, foreign keys, unique constraints, check constraints, and indexes are explicitly named.

This improves readability, debugging, migration management, and production support.

---

### Composition over Duplication

Persistence capabilities are inherited through reusable traits instead of repeated across every entity.

---

### Database Integrity

Business rules are enforced at both the application layer and database layer through constraints.

The database remains responsible for protecting its own integrity.

---

### Provider Independence

The persistence model remains independent of the underlying database engine.

Development currently uses SQLite while production deployments may use PostgreSQL without requiring changes to the domain model.

---

## Consequences

### Positive

- Consistent entity design
- Reduced duplication
- Centralized auditing
- Standardized ownership model
- Standardized soft deletion
- Explicit database constraints
- Easier onboarding for new contributors
- Simplified future domain expansion

### Negative

- Additional abstraction layer
- Slightly steeper learning curve for new developers
- Shared traits require disciplined evolution to avoid unintended side effects

---

## Alternatives Considered

### Independent Entity Definitions

Pros

- Simple initial implementation
- No inheritance hierarchy

Cons

- Significant duplication
- Inconsistent entity design
- Difficult long-term maintenance

---

### Database-First Modeling

Pros

- Rapid schema creation

Cons

- Business model driven by database implementation
- Weak separation between domain and persistence concerns

---

### Framework-Generated Models

Pros

- Faster scaffolding

Cons

- Limited architectural consistency
- Reduced control over naming conventions
- Difficult to enforce enterprise standards

---

## Future Considerations

Future entities should inherit the established persistence model without modification.

Additional reusable traits may be introduced where appropriate, for example:

- Versioning
- Tenant isolation
- Archival lifecycle
- Domain events

The persistence model should remain stable while supporting continued expansion of the Cortex domain.

---

## Related Decisions

- ADR-003: API-First Architecture
- ADR-008: API Contracts and Schemas
- ADR-013: Service Layer Pattern
- ADR-014: Document Ingestion Architecture
- ADR-015: Document Chunking Strategy
- ADR-016: Embedding Abstraction Strategy
- ADR-017: Vector Store Abstraction
- ADR-018: Knowledge Indexing Pipeline

---

## Outcome

This decision establishes a standardized persistence foundation for Cortex.

Every future business entity follows the same architectural conventions for identity, auditing, ownership, soft deletion, relationships, constraints, and indexing.

```text
Before

Workspace
    │
    ├── Custom ID
    ├── Custom Audit Fields
    ├── Custom Ownership
    └── Custom Constraints

Document
    │
    ├── Different Audit Fields
    ├── Different Ownership
    └── Different Conventions

After

                 Entity
                    │
             Auditable
                    │
              Ownable
                    │
           SoftDeletable
                    │
     ┌──────────────┴──────────────┐
     ▼                             ▼
 Workspace                    Document
```

This decision provides the persistence architecture that future Cortex domains—including Knowledge, Chunk, Embedding, Conversation, Agent, and Evaluation—will build upon, ensuring consistency, maintainability, and scalability across the platform.

---

## Implementation Status

| Component | Status |
|-----------|--------|
| Architecture | Complete |
| SQLAlchemy Models | Complete |
| Trait-Based Persistence | Complete |
| Constraint Naming | Complete |
| Indexing Strategy | Complete |
| SQLite Development Support | Complete |
| PostgreSQL Compatibility | Planned |
| Alembic Migration Support | Planned |
| Documentation | Complete |
| Production Ready | In Progress |