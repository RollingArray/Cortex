# ADR-011: Testing Strategy

## Status

Accepted

## Context

As Cortex evolves into a platform supporting retrieval systems, graph reasoning, agent orchestration, and memory management, maintaining reliability becomes increasingly important.

Manual testing alone is insufficient to prevent regressions.

An automated testing strategy is required.

## Decision

Adopt Pytest as the primary testing framework.

Tests will be organized into:

* API tests
* Service tests
* Integration tests

All new functionality should include automated tests where appropriate.

## Consequences

### Positive

* Reduced regressions
* Faster refactoring
* Improved confidence in changes
* Better onboarding for contributors

### Negative

* Increased maintenance effort
* Additional execution time during development
