# ADR-017: Vector Store Abstraction

## Status

Accepted

## Context

Embeddings generated from document chunks must be persisted in a searchable storage layer to support semantic retrieval.

As Cortex evolves, different vector storage technologies may be evaluated and adopted depending on performance, scale, deployment model, and operational requirements.

Potential vector storage implementations include:

* ChromaDB
* Qdrant
* Weaviate
* Pinecone
* Milvus
* FAISS
* PostgreSQL with pgvector

Directly coupling Cortex services to a specific vector database would increase maintenance complexity, reduce portability, and create unnecessary vendor dependency.

A provider-independent vector storage architecture is required.

## Decision

Introduce a dedicated vector store abstraction layer responsible for persisting and retrieving vectorized knowledge.

All vector store implementations must conform to a common `VectorStore` contract.

Application components will interact exclusively with the abstraction layer and will remain unaware of the underlying storage technology.

The vector store layer is responsible for:

* Persisting vector records
* Storing document metadata
* Performing similarity searches
* Returning retrieval candidates

The Cortex platform is responsible for:

* Document ingestion
* Chunk generation
* Embedding creation
* Indexing workflows
* Retrieval orchestration
* Knowledge management

The initial implementation will use a mock vector store to establish the architecture and support development without introducing external infrastructure dependencies.

## Architecture

```text
Document
    │
    ▼
Document Loader
    │
    ▼
Chunking Pipeline
    │
    ▼
Embedding Service
    │
    ▼
Vector Store
    │
    ▼
Similarity Search
    │
    ▼
Retriever
    │
    ▼
LLM
```

## Design Principles

### Provider Independence

The Cortex platform must remain independent of any specific vector database implementation.

Replacing a vector store should not require changes to:

* API endpoints
* Retrieval workflows
* Ingestion pipelines
* Embedding services

### Separation of Concerns

Vector stores are responsible only for persistence and retrieval of vectorized data.

Vector stores are not responsible for:

* Document parsing
* Chunking
* Embedding generation
* Prompt construction
* LLM interactions

### Extensibility

New vector store providers should be introduced through the existing abstraction layer.

Examples include:

* MockVectorStore
* ChromaVectorStore
* QdrantVectorStore
* WeaviateVectorStore
* PineconeVectorStore
* PgVectorStore

### Testability

Knowledge ingestion and retrieval workflows should be testable without requiring external databases.

Mock vector stores should support:

* Unit testing
* Local development
* CI/CD execution

## Canonical Data Model

All vector store implementations should operate on a common platform-owned representation.

A vector record should contain:

* Unique identifier
* Content
* Embedding vector
* Source metadata

Additional metadata fields may be introduced in future versions while preserving compatibility with the abstraction layer.

## Consequences

### Positive

* Reduced vendor lock-in
* Simplified testing
* Consistent storage interface
* Easier migration between vector databases
* Improved maintainability
* Clear separation between platform logic and storage implementation

### Negative

* Additional abstraction layer
* Increased implementation effort
* More classes and interfaces to maintain
* Slight increase in architectural complexity

## Future Considerations

Future enhancements may include:

* Metadata filtering
* Collection management
* Namespace isolation
* Multi-tenant indexing
* Hybrid search support
* Sparse and dense retrieval
* Vector compression
* Retrieval performance optimization

These enhancements should remain compatible with the existing `VectorStore` contract.

## Related Decisions

* ADR-012: AI Service Abstraction Layer
* ADR-013: Service Layer Pattern
* ADR-014: Document Ingestion Architecture
* ADR-015: Document Chunking Strategy
* ADR-016: Embedding Abstraction Strategy

The vector store abstraction continues the Cortex architectural principle of isolating infrastructure-specific implementations behind stable platform-owned contracts, ensuring long-term portability and maintainability of the knowledge platform.
