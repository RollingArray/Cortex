# ADR-021: Qdrant Vector Store Provider

## Status

Accepted

## Context

Cortex requires a vector storage layer to support semantic retrieval and Retrieval-Augmented Generation (RAG).

The initial implementation utilized a mock vector store to establish architectural contracts and enable development without external infrastructure dependencies.

As Cortex transitions to real semantic retrieval, a production-capable vector database is required to:

* Store embedding vectors
* Perform similarity searches
* Support metadata storage
* Enable retrieval workflows
* Scale with increasing knowledge volume

Several vector database options were evaluated:

* ChromaDB
* Qdrant
* Weaviate
* Milvus
* PostgreSQL with pgvector
* Neo4j Vector Indexes

The Cortex platform prioritizes:

* Local-first development
* Provider abstraction
* Minimal operational complexity
* Future production scalability
* Strong Python ecosystem support

During implementation, ChromaDB introduced platform compatibility challenges on Intel macOS environments due to dependency requirements.

Qdrant provided a lightweight and reliable alternative with strong local development support and a clear migration path to production deployments.

## Decision

Adopt Qdrant as the primary vector store implementation for Cortex.

The initial implementation will use:

```text
Qdrant In-Memory Mode
```

for local development and integration testing.

The vector store implementation will remain behind the existing `VectorStore` abstraction.

Application components will continue interacting exclusively through the vector store contract.

No changes are required to:

* Knowledge indexing pipelines
* Retrieval services
* Embedding providers
* API endpoints

## Architecture

```text
Document
    │
    ▼
Chunking
    │
    ▼
Embedding Service
    │
    ▼
Ollama Embeddings
    │
    ▼
Qdrant Vector Store
    │
    ▼
Similarity Search
    │
    ▼
Retrieved Knowledge
```

## Design Principles

### Vector Store Abstraction

The application must remain independent of vector database implementations.

Consumers interact only with:

```text
VectorStore
```

and not directly with Qdrant APIs.

Future migrations should not require changes to:

* Retrieval logic
* Knowledge pipelines
* API layers

### Local Development Simplicity

Developers should be able to run Cortex without:

* Docker
* Kubernetes
* External services

Qdrant In-Memory mode provides:

* Fast startup
* Minimal configuration
* Repeatable testing

### Production Readiness

The selected vector database must support future deployment requirements including:

* Persistence
* Metadata filtering
* Large collections
* Horizontal scalability

Qdrant provides a migration path from:

```text
QdrantClient(":memory:")
```

to:

```text
Qdrant Server
```

without significant code changes.

### Metadata-Aware Retrieval

Knowledge records should support metadata alongside embeddings.

Examples include:

* Source document
* Collection
* Knowledge type
* Tags
* Ownership information

This enables future retrieval enhancements without schema redesign.

## Retrieval Workflow

The standard retrieval workflow is:

```text
Document
    ↓
Chunk
    ↓
Generate Embedding
    ↓
Store Vector
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Return Relevant Records
```

Qdrant becomes the system of record for vector-based knowledge retrieval.

## Consequences

### Positive

* Real vector similarity search
* Local-first development experience
* No external infrastructure requirements
* Production-ready architecture
* Strong Python ecosystem support
* Seamless future scalability
* Metadata support

### Negative

* Additional dependency
* Vector storage management complexity
* Future migration considerations for persistence

## Future Considerations

Future enhancements may include:

### Persistent Qdrant Storage

Move from:

```text
In-Memory Collections
```

to:

```text
Persistent Local Storage
```

### Dedicated Qdrant Server

Move from:

```text
Embedded Client
```

to:

```text
Standalone Qdrant Deployment
```

### Hybrid Retrieval

Support:

* Vector similarity
* Keyword search
* Metadata filtering

within a single retrieval workflow.

### Multi-Collection Architecture

Potential future collections:

```text
knowledge
memory
documents
agents
evaluations
```

### GraphRAG Integration

Qdrant may eventually operate alongside:

```text
Neo4j
```

where:

```text
Qdrant
    → Semantic Similarity

Neo4j
    → Relationship Traversal
```

forming the foundation of a GraphRAG architecture.

## Alternatives Considered

### ChromaDB

Pros:

* Simple setup
* Popular in RAG prototypes

Cons:

* Dependency compatibility issues on Intel macOS
* Reduced operational flexibility

### Neo4j

Pros:

* Graph-native retrieval
* GraphRAG support

Cons:

* Overly complex for current retrieval requirements
* Graph capabilities not yet required

### PostgreSQL + pgvector

Pros:

* Mature ecosystem
* Strong persistence

Cons:

* Additional infrastructure requirements
* More operational overhead

## Related Decisions

* ADR-013: Service Layer Pattern
* ADR-016: Embedding Abstraction Strategy
* ADR-017: Vector Store Abstraction
* ADR-018: Knowledge Indexing Pipeline
* ADR-019: Retrieval Service Architecture
* ADR-020: Ollama Embedding Provider

This decision establishes the first production vector retrieval capability within Cortex and completes the transition from mock retrieval infrastructure to real semantic search.
