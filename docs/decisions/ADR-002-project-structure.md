# ADR-002: Project Structure

## Status

Accepted

## Context

Cortex is expected to evolve into a modular AI platform containing retrieval, graph reasoning, memory systems, agent orchestration, and observability capabilities.

The structure must support incremental architectural evolution.

## Decision

Use a layered application structure:

app/
api/
services/
schemas/
core/
models/
utils/

## Consequences

### Positive

- Clear separation of concerns
- Easier testing
- Supports future expansion
- Encourages modular design

### Negative

- Slightly more verbose structure initially