# ADR-012: AI Service Abstraction Layer

## Status

Accepted

## Context

Cortex will eventually support multiple AI model providers including local and cloud-hosted runtimes.

Directly coupling application code to a specific provider creates vendor lock-in and increases maintenance complexity.

A provider abstraction layer is required.

## Decision

Introduce a dedicated AI service interface.

Application components will communicate exclusively through the abstraction layer.

Provider-specific implementations will be isolated behind the interface.

Initial implementation will use a mock provider for development and testing.

## Consequences

### Positive

* Provider independence
* Easier testing
* Simplified future integrations
* Reduced vendor lock-in

### Negative

* Additional abstraction layer
* Slight increase in implementation complexity
