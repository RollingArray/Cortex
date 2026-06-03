# ADR-008: API Contracts and Response Schemas

## Status

Accepted

## Context

As Cortex evolves into a platform with multiple services and integrations, API consistency becomes increasingly important.

Endpoints should expose strongly typed request and response models to:

* Improve API documentation
* Enable validation
* Ensure consistency across services
* Support future client integrations

## Decision

Adopt Pydantic models as the canonical definition of API contracts.

All public API endpoints should define request and response schemas through dedicated models under:

app/schemas/

## Consequences

### Positive

* Consistent API design
* Improved OpenAPI documentation
* Automatic validation
* Easier client integration

### Negative

* Additional schema maintenance
* More files to manage as APIs grow
