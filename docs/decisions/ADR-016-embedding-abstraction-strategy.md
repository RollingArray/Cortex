# ADR-016: Embedding Abstraction Strategy

## Status

Accepted

## Context

Embeddings form the foundation of semantic retrieval within Cortex.

Documents and document chunks must be transformed into numerical vector representations before they can be indexed, searched, and retrieved based on meaning rather than keyword matching.

Multiple embedding providers and models may be used throughout the lifecycle of the platform, including:

* Sentence Transformers
* Ollama Embeddings
* OpenAI Embeddings
* BGE Models
* Instructor Models
* Future enterprise-specific embedding models

Directly coupling application logic to a specific embedding implementation would increase maintenance complexity and create unnecessary vendor dependency.

A provider-independent embedding architecture is required.

## Decision

Introduce a dedicated embedding abstraction layer responsible for generating vector representations from text.

All embedding providers must implement a common `EmbeddingProvider` contract.

Application components will interact exclusively with the abstraction layer and will remain unaware of the underlying embedding implementation.

Embedding providers are responsible for:

* Model execution
* Vector generation
* Provider-specific configuration

The Cortex platform is responsible for:

* Embedding contracts
* Embedding services
* Knowledge ingestion workflows
* Retrieval orchestration

The initial implementation will use a mock embedding provider to establish the architecture and support development without requiring model downloads or external runtime dependencies.

## Architecture

```text
Document
    │
    ▼
Chunking Pipeline
    │
    ▼
Embedding Service
    │
    ▼
Embedding Provider
    │
    ▼
Embedding Vector
    │
    ▼
Vector Store
    │
    ▼
Retriever
```

## Design Principles

### Provider Independence

Embedding generation must remain independent of any specific model vendor or runtime.

Replacing an embedding provider should not require changes to:

* API endpoints
* Knowledge ingestion workflows
* Retrieval pipelines
* Vector storage implementations

### Separation of Concerns

Embedding providers are responsible only for generating embeddings.

Embedding providers are not responsible for:

* Chunking
* Vector storage
* Retrieval
* Ranking
* LLM interaction

### Extensibility

New providers should be introduced through the existing abstraction layer without affecting platform components.

Examples include:

* MockEmbeddingProvider
* OllamaEmbeddingProvider
* SentenceTransformerProvider
* OpenAIEmbeddingProvider

### Testability

Application logic should be testable without requiring external model runtimes.

Mock providers should be available for:

* Unit testing
* Local development
* CI/CD execution

## Consequences

### Positive

* Reduced vendor lock-in
* Simplified testing
* Consistent embedding interface
* Easier provider replacement
* Improved maintainability
* Clear separation between platform logic and model execution

### Negative

* Additional abstraction layer
* More implementation classes
* Slight increase in architectural complexity

## Future Considerations

Future enhancements may include:

* Configurable embedding providers
* Embedding model version management
* Embedding caching
* Batch embedding generation
* Hybrid embedding strategies
* Embedding quality evaluation
* Multi-model embedding support

These enhancements should remain compatible with the existing `EmbeddingProvider` contract.

## Related Decisions

* ADR-012: AI Service Abstraction Layer
* ADR-013: Service Layer Pattern
* ADR-014: Document Ingestion Architecture
* ADR-015: Document Chunking Strategy

The embedding abstraction layer continues the Cortex architectural principle of isolating provider-specific implementations behind stable platform-owned contracts.
