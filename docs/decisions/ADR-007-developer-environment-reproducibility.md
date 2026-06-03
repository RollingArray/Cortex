# ADR-007: Developer Environment Reproducibility

## Status

Accepted

## Context

Cortex is expected to be developed across multiple developer workstations and deployment environments.

Inconsistent local environments can lead to:

* Dependency drift
* Runtime inconsistencies
* Setup friction
* Difficult onboarding

A reproducible development environment is required to ensure Cortex behaves consistently across machines.

## Decision

Adopt the following standards:

* Python version managed through `.python-version`
* Dependency management through UV
* Dependency locking through `uv.lock`
* Environment configuration through `configs/environments`
* Developer onboarding through `docs/setup-guide.md`

The setup guide must remain current with architectural changes.

## Consequences

### Positive

* Consistent developer experience
* Simplified onboarding
* Reduced environment-related defects
* Improved portability

### Negative

* Additional documentation maintenance
* Dependency updates require lock file management
