# ADR-018: Knowledge Indexing Pipeline

## Status

Accepted

## Context

The Cortex knowledge platform consists of multiple independent components responsible for transforming raw documents into searchable knowledge.

Current platform capabilities include:

* Document loading
* Document chunking
* Embedding generation
* Vector storage

While each component is independently responsible for a specific stage of processing, a coordinated workflow is required to transform source documents into indexed knowledge.

Without orchestration, application components would be required to manually invoke each stage of the ingestion process, increasing coupling and implementation complexity.

A dedicated indexing pipeline is required to coordinate knowledge ingestion activities.

## Decision

Introduce a dedicated knowledge indexing pipeline responsible for orchestrating document ingestion workflows.

The indexing pipeline will coordinate existing platform services while maintaining separation of concerns between processing stages.

The pipeline is responsible for:

* Loading documents
* Chunking content
* Generating embeddings
* Persisting vector records
* Producing indexing results

Individual services remain responsible for their own specialized functions.

The indexing pipeline does not perform:

* Document parsing logic
* Chunking logic
* Embedding generation logic
* Vector storage implementation
* Retrieval logic

These responsibilities remain delegated to their respective services.

## Architecture

```text
Document Source
       │
       ▼
Document Loader
       │
       ▼
Document
       │
       ▼
Chunking Service
       │
       ▼
Document Chunks
       │
       ▼
Embedding Service
       │
       ▼
Embedding Vectors
       │
       ▼
Vector Store
       │
       ▼
Indexed Knowledge
```

## Design Principles

### Orchestration Over Implementation

Pipelines coordinate processing stages but do not implement processing logic.

Individual services remain responsible for execution.

```text
Pipeline
    ↓
Service
    ↓
Provider
```

### Separation of Concerns

The indexing pipeline must remain independent of:

* Specific embedding models
* Specific vector databases
* Specific chunking algorithms
* Specific document formats

Pipeline behavior should remain unchanged when infrastructure implementations evolve.

### Reusability

Individual services should remain reusable outside the indexing pipeline.

Examples include:

* Standalone document loading
* Independent chunking operations
* Direct embedding generation
* Custom retrieval workflows

### Extensibility

Future ingestion enhancements should integrate through the indexing pipeline without requiring modifications to downstream platform components.

Potential future enhancements include:

* Batch ingestion
* Parallel processing
* Metadata extraction
* Entity extraction
* Graph generation
* Ingestion validation
* Deduplication

## Consequences

### Positive

* Simplified document ingestion workflows
* Reduced application complexity
* Clear separation between orchestration and execution
* Improved maintainability
* Easier future pipeline expansion
* Consistent ingestion behavior

### Negative

* Additional orchestration layer
* Increased architectural complexity
* Additional testing requirements

## Future Considerations

Future versions of the indexing pipeline may support:

* Multiple document formats
* Concurrent ingestion processing
* Incremental indexing
* Knowledge graph enrichment
* Workflow monitoring
* Pipeline metrics
* Retry and recovery mechanisms
* Event-driven ingestion workflows

These enhancements should preserve the existing separation between orchestration responsibilities and service implementations.

## Related Decisions

* ADR-013: Service Layer Pattern
* ADR-014: Document Ingestion Architecture
* ADR-015: Document Chunking Strategy
* ADR-016: Embedding Abstraction Strategy
* ADR-017: Vector Store Abstraction

The knowledge indexing pipeline establishes the first end-to-end knowledge ingestion workflow within Cortex and introduces the architectural pattern that future retrieval, graph construction, and agent orchestration pipelines will follow.
