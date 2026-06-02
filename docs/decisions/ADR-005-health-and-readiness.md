# ADR-005: Health, Readiness and Service Metadata Endpoints

## Status

Accepted

## Context

Cortex is being developed as a platform that will eventually integrate multiple infrastructure components, including:

* FastAPI
* Ollama
* Vector Databases
* Graph Databases
* Agent Orchestration
* Observability Services

As the platform grows, operators and automated systems need a standardized mechanism to determine:

* Whether the application process is running
* Whether the application is capable of serving requests
* Which version of Cortex is deployed
* Which environment is currently active

Without dedicated endpoints, deployment automation, monitoring systems, and operational troubleshooting become more difficult.

## Decision

Introduce dedicated service endpoints:

* `/health`
* `/ready`
* `/info`

Endpoint responsibilities:

### Health Endpoint

Determines whether the Cortex application process is running.

### Readiness Endpoint

Determines whether Cortex is ready to accept requests.

Initially, readiness will return a static response.

Future implementations will validate dependencies such as:

* Ollama
* Neo4j
* Qdrant
* Redis

### Information Endpoint

Provides service metadata including:

* Application name
* Application version
* Deployment environment

## Consequences

### Positive

* Establishes a production-oriented service pattern
* Simplifies future deployment automation
* Supports infrastructure monitoring
* Supports Kubernetes readiness and liveness concepts
* Provides deployment visibility through metadata endpoints
* Enables future dependency health validation

### Negative

* Introduces additional endpoint maintenance
* Readiness endpoint may initially appear redundant until external dependencies are introduced
