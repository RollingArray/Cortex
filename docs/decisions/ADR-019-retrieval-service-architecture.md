# ADR-019: Retrieval Service Architecture

## Status

Accepted

## Context

The primary purpose of the Cortex knowledge platform is to enable retrieval of relevant information from indexed knowledge sources.

Documents are transformed through the ingestion pipeline into searchable vector representations stored within the vector store layer.

A dedicated retrieval capability is required to:

* Accept user queries
* Generate query embeddings
* Execute similarity searches
* Return relevant knowledge to consuming services

Direct coupling between application components and vector store implementations would create unnecessary dependencies and increase maintenance complexity.

A dedicated retrieval service is required to coordinate knowledge discovery while remaining independent of storage and embedding implementations.

## Decision

Introduce a dedicated retrieval service responsible for orchestrating semantic search operations across the Cortex knowledge platform.

The retrieval service will coordinate:

* Query embedding generation
* Vector similarity search
* Retrieval result construction
* Search result delivery

The retrieval service will operate independently of:

* Specific embedding providers
* Specific vector stores
* LLM providers
* Prompt construction logic

Application components will interact with the retrieval service rather than directly accessing vector stores.

## Architecture

```text
User Query
     │
     ▼
Retrieval Service
     │
     ▼
Embedding Service
     │
     ▼
Query Embedding
     │
     ▼
Vector Store
     │
     ▼
Similarity Search
     │
     ▼
Retrieved Records
     │
     ▼
Retrieval Results
```

## Design Principles

### Retrieval Owns Search Orchestration

The retrieval service is responsible for coordinating search operations.

The retrieval service does not perform:

* Embedding generation
* Vector storage
* Similarity algorithm implementation
* LLM reasoning

These responsibilities remain delegated to specialized platform services.

### Provider Independence

Retrieval logic must remain independent of infrastructure implementations.

Replacing:

* Embedding providers
* Vector databases

must not require modifications to retrieval workflows.

### Separation of Concerns

The retrieval service should expose knowledge-focused results rather than storage-specific representations.

Application components should consume retrieval results without awareness of underlying vector store structures.

### Extensibility

Future retrieval strategies should integrate through the retrieval layer without impacting consumers.

Examples include:

* Semantic retrieval
* Hybrid retrieval
* Metadata-filtered retrieval
* Multi-stage retrieval
* Graph-enhanced retrieval
* Re-ranking workflows

### Testability

Retrieval workflows should be testable without external infrastructure.

Mock embedding providers and mock vector stores should support:

* Unit testing
* Local development
* Continuous integration execution

## Retrieval Workflow

The standard retrieval workflow consists of:

```text
Query
  ↓
Generate Query Embedding
  ↓
Perform Similarity Search
  ↓
Collect Candidate Results
  ↓
Return Retrieval Results
```

The retrieval service acts as the coordination layer between embedding generation and vector search.

## Consequences

### Positive

* Clear retrieval abstraction
* Reduced infrastructure coupling
* Consistent retrieval interface
* Easier testing
* Simplified future enhancements
* Foundation for Retrieval-Augmented Generation (RAG)

### Negative

* Additional service layer
* Increased architectural complexity
* Additional maintenance overhead

## Future Considerations

Future retrieval enhancements may include:

* Similarity score support
* Metadata filtering
* Collection-aware retrieval
* Hybrid keyword and vector search
* Re-ranking pipelines
* Query expansion
* Context compression
* Graph-enhanced retrieval
* Multi-hop retrieval
* Personalized retrieval

These enhancements should remain compatible with the retrieval service abstraction.

## Related Decisions

* ADR-013: Service Layer Pattern
* ADR-014: Document Ingestion Architecture
* ADR-015: Document Chunking Strategy
* ADR-016: Embedding Abstraction Strategy
* ADR-017: Vector Store Abstraction
* ADR-018: Knowledge Indexing Pipeline

The retrieval service establishes the first knowledge access layer within Cortex and serves as the foundation for future Retrieval-Augmented Generation (RAG), GraphRAG, agent orchestration, and knowledge reasoning capabilities.
