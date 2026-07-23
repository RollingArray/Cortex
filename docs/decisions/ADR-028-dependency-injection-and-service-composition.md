# ADR-028: Dependency Injection and Service Composition

**Status:** Accepted

**Date:** 2026-07-23

**Authors:** Ranjoy Sen

---

# Context

Cortex is designed as a modular, enterprise-grade platform consisting of multiple architectural layers including:

- API
- Services
- Repositories
- Infrastructure
- AI Providers
- Storage
- Persistence

As the platform grows, services increasingly depend on one another. Examples include:

- WorkspaceService using DocumentService
- DocumentService using StorageService
- RetrievalService using VectorStoreProvider
- AI Services using EmbeddingProvider and ChatProvider

Directly instantiating dependencies within services tightly couples components, making the application difficult to test, maintain, and extend.

The platform therefore requires a consistent dependency injection strategy that promotes loose coupling and explicit service composition.

---

# Decision

Cortex adopts constructor-based dependency injection.

Each service declares its dependencies through its constructor rather than creating them internally.

Example:

```python
class DocumentService:

    def __init__(
        self,
        database: Session,
        repository: DocumentRepository,
        storage: StorageService,
    ):
        ...
```

Dependencies are composed centrally through dependency providers.

---

# Dependency Composition

The dependency graph follows a layered architecture.

```
API Layer
      │
      ▼
Dependency Providers
      │
      ▼
Application Services
      │
      ▼
Repositories
      │
      ▼
Database
```

Infrastructure services such as storage and AI providers are injected alongside repositories.

```
                API
                 │
                 ▼
         Dependency Provider
                 │
      ┌──────────┴──────────┐
      ▼                     ▼
Repository          Infrastructure
      │                     │
      └──────────┬──────────┘
                 ▼
             Application
               Service
```

---

# Dependency Providers

All service construction is centralized within the dependency injection layer.

Example:

```
backend/
└── di/
    ├── database.py
    ├── repositories.py
    ├── services.py
    └── providers.py
```

Dependency providers are responsible for:

- Creating repositories
- Creating infrastructure services
- Constructing application services
- Wiring dependencies together

API endpoints receive fully constructed services.

Example:

```python
@router.post(...)
def upload_document(
    service: DocumentService = Depends(get_document_service),
):
    ...
```

Endpoints never instantiate services directly.

---

# Service Composition

Application services may compose other application services when appropriate.

Example:

```
WorkspaceService
        │
        ▼
DocumentService
        │
        ▼
StorageService
```

The consuming service interacts only with the public interface of its dependency.

Internal implementation details remain encapsulated.

---

# Repository Responsibilities

Repositories are responsible only for persistence operations.

Typical responsibilities include:

- Create
- Read
- Update
- Delete
- Query construction

Repositories never:

- commit transactions
- rollback transactions
- perform business logic
- coordinate multiple repositories

Repositories are intentionally lightweight.

---

# Transaction Ownership

Business transactions belong exclusively to the service layer.

Example:

```
Service
 ├── Repository A
 ├── Repository B
 ├── StorageService
 └── Commit
```

This enables a single business operation to coordinate multiple persistence actions atomically.

Example:

Document upload:

- Save binary file
- Insert metadata
- Commit transaction

Document delete:

- Delete vector entries
- Delete binary file
- Delete metadata
- Commit transaction

Repositories remain unaware of transactional boundaries.

---

# Benefits

Constructor injection provides several advantages.

## Loose Coupling

Components depend upon abstractions rather than concrete implementations.

---

## Testability

Dependencies can easily be replaced with mocks or fakes.

Example:

```
MockStorageService

FakeEmbeddingProvider

InMemoryRepository
```

No production infrastructure is required during unit testing.

---

## Maintainability

Dependency construction exists in one location.

Changing implementations requires updating only the provider layer.

---

## Extensibility

Future providers can be introduced without changing business logic.

Examples include:

- Azure OpenAI
- OpenAI
- Anthropic
- Amazon Bedrock
- PostgreSQL repositories
- Cloud storage providers

---

## Explicit Dependencies

Constructors clearly communicate the requirements of a service.

There are no hidden dependencies or service locators.

---

# Consequences

## Advantages

- Centralized dependency management
- High testability
- Loose coupling
- Cleaner services
- Clear architectural boundaries
- Easier refactoring
- Consistent object lifecycle

## Trade-offs

- Additional provider layer
- Slightly more initial boilerplate
- Dependency graph becomes larger as the application grows

These trade-offs are acceptable for an enterprise-scale application.

---

# Alternatives Considered

## Direct Service Construction

Example:

```python
storage = StorageService()
repository = DocumentRepository(database)
service = DocumentService(repository, storage)
```

Rejected because:

- Tight coupling
- Difficult testing
- Duplicate construction logic
- Poor scalability

---

## Global Singleton Services

Rejected because:

- Hidden dependencies
- Shared mutable state
- Difficult unit testing
- Poor lifecycle management

---

## Service Locator Pattern

Rejected because:

- Dependencies become implicit
- Harder to understand
- Reduced compile-time visibility
- Considered an anti-pattern in modern application architecture

---

# Future Considerations

The dependency injection architecture provides a foundation for future capabilities including:

- Plugin discovery
- Feature modules
- Background workers
- Event handlers
- Multi-tenant service composition
- Alternate infrastructure providers
- Cloud-native deployment

The constructor-based dependency injection model remains the preferred mechanism for composing application services throughout Cortex.