# ADR-003: API First Architecture

## Status

Accepted

## Context

Cortex will evolve into a platform containing retrieval, graph reasoning, memory systems, agent orchestration, and observability capabilities.

These capabilities may eventually be consumed by:

* Web applications
* Mobile applications
* CLI tools
* External integrations
* Other services

## Decision

Expose Cortex capabilities through a well-defined API layer.

Business logic will remain inside services.

Endpoints will act as thin orchestration layers.

## Consequences

### Positive

* Separation of concerns
* Easier testing
* Easier frontend integration
* Future service decomposition becomes simpler

### Negative

* Slightly more structure initially
