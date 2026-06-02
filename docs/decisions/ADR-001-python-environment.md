# ADR-001: Python Environment Management

## Status

Accepted

## Context

Cortex requires a reproducible Python development environment that supports:

- Local development
- Dependency isolation
- Future AI libraries
- Production deployment

## Decision

Use uv as the primary Python package and environment manager.

## Consequences

### Positive

- Fast dependency resolution
- Reproducible environments
- Modern Python workflow
- Easy project onboarding

### Negative

- Additional tool installation
- Smaller ecosystem familiarity compared to pip