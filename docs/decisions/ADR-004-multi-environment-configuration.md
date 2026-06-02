# ADR-004: Multi-Environment Configuration Strategy

## Status

Accepted

## Context

Cortex will support multiple deployment environments including local development, shared development, staging, and production.

The platform requires environment-specific configuration without modifying application code.

## Decision

Introduce a dedicated configuration hierarchy:

configs/
├── environments/
├── logging/
├── models/
├── prompts/
└── retrieval/

Application configuration will be loaded through a centralized configuration layer using pydantic-settings.

## Consequences

### Positive

- Clear separation of application and configuration
- Environment-specific behavior without code changes
- Easier future deployment automation
- Supports infrastructure growth

### Negative

- Slightly more setup complexity