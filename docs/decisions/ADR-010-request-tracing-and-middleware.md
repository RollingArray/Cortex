# ADR-010: Request Tracing and Middleware Strategy

## Status

Accepted

## Context

As Cortex evolves into a platform containing retrieval systems, graph reasoning, memory systems, and agent orchestration, tracing individual requests becomes increasingly important.

Without request tracing, diagnosing performance issues and failures across multiple components becomes difficult.

## Decision

Introduce centralized HTTP middleware responsible for:

* Request identification
* Request timing
* Request logging
* Response header enrichment

Each request will receive a unique identifier.

The identifier will be included in application logs and returned to clients through the X-Request-ID response header.

## Consequences

### Positive

* Improved observability
* Easier troubleshooting
* Request-level tracing
* Foundation for distributed tracing

### Negative

* Slight request processing overhead
* Additional logging volume
