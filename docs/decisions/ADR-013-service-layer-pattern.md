# ADR-013: Service Layer Pattern

## Status

Accepted

## Context

As Cortex evolves beyond simple API endpoints, business logic will become increasingly complex.

Embedding orchestration logic directly inside route handlers would reduce maintainability and increase coupling.

## Decision

Introduce a dedicated service layer.

API endpoints will remain responsible for:

* Request validation
* Response serialization
* HTTP concerns

Business logic will reside within service classes.

## Consequences

### Positive

* Improved separation of concerns
* Easier testing
* Better maintainability
* Reduced API-layer complexity

### Negative

* Additional abstraction
* More files and classes
