# ADR-026: Application Lifecycle and Startup Architecture

## Status

Accepted

---

## Context

As Cortex expanded beyond a simple FastAPI application, application startup became responsible for initializing multiple infrastructure components before serving requests.

Examples include:

- Database initialization
- Configuration loading
- Logging configuration
- AI provider registration
- Vector database connectivity
- Future background workers
- Future plugin discovery

Initially, initialization logic was embedded directly within the FastAPI application using startup events.

As additional infrastructure components were introduced, this approach resulted in:

- Startup logic becoming centralized inside `main.py`
- Tight coupling between application entry point and infrastructure
- Difficult testing of initialization behavior
- Limited extensibility for future services

Cortex requires a structured application lifecycle that separates application bootstrapping from application composition while remaining aligned with modern FastAPI practices.

---

## Decision

Adopt a layered application lifecycle architecture based on FastAPI's lifespan protocol.

Application startup responsibilities are delegated across dedicated modules.

The startup sequence is organized into four layers:

1. FastAPI Application
2. Lifespan Management
3. Startup Orchestration
4. Infrastructure Initialization

Each layer has a single responsibility.

Infrastructure services register themselves during application startup rather than within the application entry point.

---

## Architecture

```text
                FastAPI
                    │
                    ▼
              lifespan.py
                    │
                    ▼
               startup.py
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
 Configuration   Database   Future Services
                    │
                    ▼
      database_initializer.py
                    │
                    ▼
             SQLAlchemy Engine
```

The FastAPI application remains responsible only for application composition.

Initialization logic is delegated to specialized modules.

---

## Responsibilities

### main.py

Responsible for:

- Application creation
- Router registration
- Middleware registration
- Application composition

Not responsible for:

- Database initialization
- Infrastructure bootstrapping
- Service registration

---

### lifespan.py

Responsible for:

- Managing application startup
- Managing application shutdown
- Coordinating lifecycle execution

Not responsible for:

- Infrastructure implementation
- Business logic

---

### startup.py

Responsible for:

- Orchestrating application initialization
- Invoking infrastructure initialization
- Coordinating startup order

Not responsible for:

- FastAPI configuration
- Request handling

---

### database_initializer.py

Responsible for:

- Database initialization
- Schema creation
- Persistence bootstrapping

Not responsible for:

- Session management
- Business logic

---

### database.py

Responsible for:

- Database engine creation
- Session factory
- Base metadata

Not responsible for:

- Schema creation
- Startup orchestration

---

## Design Principles

### Single Responsibility

Each module performs one well-defined startup responsibility.

Infrastructure initialization is isolated from application composition.

---

### Layered Initialization

Application startup proceeds through clearly defined layers.

Each layer depends only on the layer beneath it.

---

### Modern FastAPI Practices

The application adopts FastAPI's lifespan protocol in place of deprecated startup events.

This ensures long-term compatibility with the framework.

---

### Extensibility

Future infrastructure components can be registered without modifying the application entry point.

Examples include:

- AI providers
- Vector databases
- Cache providers
- Plugin registries
- Message queues

---

### Testability

Initialization logic can be executed independently from the web application.

This enables infrastructure testing without starting the API server.

---

## Consequences

### Positive

- Clean application entry point
- Modern FastAPI lifecycle management
- Clear separation of responsibilities
- Easier infrastructure testing
- Simplified future service registration
- Improved maintainability
- Predictable startup sequence

### Negative

- Additional architectural layers
- More modules to understand
- Startup flow spans multiple files

---

## Alternatives Considered

### Startup Logic in main.py

Pros

- Simple implementation
- Fewer files

Cons

- Poor separation of concerns
- Difficult scalability
- Large application entry point

---

### FastAPI Startup Events

Pros

- Familiar implementation
- Widely used historically

Cons

- Deprecated by FastAPI
- Less flexible lifecycle management
- Not aligned with future framework evolution

---

### Infrastructure Self-Initialization

Pros

- Minimal startup orchestration

Cons

- Unpredictable initialization order
- Hidden dependencies
- Difficult debugging

---

## Future Considerations

As Cortex evolves, additional startup responsibilities may include:

- AI provider initialization
- Embedding model loading
- Vector database health verification
- Plugin discovery
- Knowledge graph initialization
- Background task scheduler
- Distributed worker registration
- Telemetry and observability services

The startup architecture should remain stable while accommodating these infrastructure capabilities.

---

## Related Decisions

- ADR-003: API-First Architecture
- ADR-006: Structured Logging
- ADR-010: Request Tracing and Middleware
- ADR-013: Service Layer Pattern
- ADR-024: Domain-Driven Persistence Model
- ADR-025: SQLAlchemy Persistence Architecture

---

## Outcome

This decision establishes a modular application lifecycle for Cortex.

Application startup becomes a predictable orchestration process rather than a collection of framework callbacks.

```text
Before

FastAPI
   │
   ▼
main.py
   │
   ├── Configuration
   ├── Database
   ├── Logging
   └── Infrastructure

After

FastAPI
   │
   ▼
lifespan.py
   │
   ▼
startup.py
   │
   ▼
Infrastructure Initializers
   │
   ▼
Application Ready
```

This architecture provides a scalable and maintainable startup framework that supports future infrastructure growth while keeping the application entry point focused solely on application composition.

---

## Implementation Status

| Component | Status |
|-----------|--------|
| FastAPI Lifespan | Complete |
| Startup Orchestration | Complete |
| Database Initialization | Complete |
| Infrastructure Separation | Complete |
| Application Composition | Complete |
| Logging Integration | Complete |
| AI Provider Initialization | Planned |
| Plugin Registration | Planned |
| Background Worker Registration | Planned |
| Production Ready | In Progress |