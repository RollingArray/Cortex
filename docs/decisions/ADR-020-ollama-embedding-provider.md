# ADR-020: Ollama Embedding Provider

## Status

Accepted

## Context

Cortex requires embeddings to support semantic retrieval and Retrieval-Augmented Generation (RAG).

The initial platform implementation used a mock embedding provider to establish architectural contracts and enable development without external dependencies.

As Cortex transitions from architectural scaffolding to real AI infrastructure, a production-capable embedding implementation is required.

Several embedding approaches were evaluated:

* Sentence Transformers
* OpenAI Embeddings
* Ollama Embeddings
* Hosted embedding APIs

The Cortex platform prioritizes:

* Local-first execution
* Minimal external dependencies
* Privacy-preserving inference
* Provider abstraction
* Developer-friendly setup

Ollama provides local model execution through a stable HTTP API and supports dedicated embedding models suitable for retrieval workloads.

## Decision

Adopt Ollama as the first production embedding provider implementation.

The platform will use:

```text
Model:
nomic-embed-text
```

through the Ollama runtime.

The Ollama embedding provider will implement the existing `EmbeddingProvider` contract.

Application components will continue interacting exclusively through the embedding abstraction layer.

No changes are required to:

* Retrieval services
* Knowledge indexing pipelines
* API endpoints
* Vector store implementations

## Architecture

```text
Document Chunk
      │
      ▼
Embedding Service
      │
      ▼
Embedding Provider
      │
      ▼
Ollama Runtime
      │
      ▼
nomic-embed-text
      │
      ▼
Embedding Vector
```

## Design Principles

### Local-First AI

Embedding generation should execute locally whenever possible.

Benefits include:

* Reduced operational cost
* No external API dependency
* Improved privacy
* Offline-capable workflows

### Provider Abstraction

Ollama is an implementation detail.

The Cortex platform remains dependent only on the `EmbeddingProvider` contract.

Future providers may include:

* OpenAI
* Azure OpenAI
* Sentence Transformers
* Enterprise-hosted models

### Infrastructure Isolation

Embedding model execution remains isolated from:

* Retrieval logic
* Vector storage
* API layers
* Knowledge pipelines

### Development Simplicity

Developers should be able to run the entire embedding stack locally with minimal configuration.

## Consequences

### Positive

* Real semantic embeddings
* Local execution
* Improved privacy
* Reduced vendor dependency
* Simple deployment model
* Consistent API-driven integration

### Negative

* Requires local model downloads
* Increased local resource consumption
* Ollama runtime dependency

## Future Considerations

Future enhancements may include:

* Multiple embedding models
* Dynamic provider selection
* Embedding caching
* Batch embedding generation
* Embedding quality evaluation
* Provider failover strategies

These enhancements should remain compatible with the existing embedding abstraction layer.

## Related Decisions

* ADR-012: AI Service Abstraction Layer
* ADR-016: Embedding Abstraction Strategy
* ADR-018: Knowledge Indexing Pipeline
* ADR-019: Retrieval Service Architecture

This decision marks the first production AI capability within Cortex and establishes the foundation for real semantic retrieval.
