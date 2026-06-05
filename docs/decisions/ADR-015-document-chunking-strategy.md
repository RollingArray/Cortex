# ADR-015: Document Chunking Strategy

## Status

Accepted

## Context

As Cortex evolves into a retrieval-augmented knowledge platform, documents must be transformed into smaller retrieval units before they can be embedded, indexed, and searched effectively.

Large documents cannot be directly used for retrieval because:

* Embedding models have input size limitations
* Retrieval quality decreases when indexing large blocks of text
* Relevant information is often contained within small sections of a document
* Smaller retrieval units improve context precision

Chunking is therefore a fundamental stage within the knowledge ingestion pipeline.

A standardized chunking strategy is required to ensure consistency across future embedding models, vector stores, and retrieval mechanisms.

## Decision

Introduce a dedicated chunking layer within the document ingestion pipeline.

Chunking will be implemented through a common `Chunker` contract that transforms a document into one or more document chunks.

The chunking layer will remain independent of:

* Embedding models
* Vector databases
* Retrieval systems
* LLM providers

The initial implementation will use a character-based chunking strategy to establish the framework and validate the ingestion pipeline.

Future chunking strategies may be introduced without requiring changes to downstream components.

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
Chunker
       │
       ▼
Document Chunks
       │
       ▼
Embedding Pipeline
       │
       ▼
Vector Store
       │
       ▼
Retriever
       │
       ▼
LLM
```

## Chunking Principles

### Separation of Concerns

Chunking is responsible only for transforming documents into retrieval units.

It is not responsible for:

* Embedding generation
* Vector indexing
* Similarity search
* LLM prompting

### Extensibility

Multiple chunking strategies should be supported through a common contract.

Examples include:

* Character-based chunking
* Sentence-based chunking
* Paragraph-based chunking
* Semantic chunking
* Markdown-aware chunking
* Source-code chunking

### Retrieval Optimization

Chunks should be designed to maximize retrieval accuracy while maintaining sufficient contextual information.

Chunking decisions should prioritize retrieval effectiveness rather than document storage convenience.

## Consequences

### Positive

* Clear separation between ingestion and retrieval concerns
* Improved retrieval quality
* Support for multiple chunking strategies
* Simplified testing
* Independent evolution of chunking algorithms
* Foundation for future semantic retrieval enhancements

### Negative

* Additional processing stage within the ingestion pipeline
* Increased architectural complexity
* Requires careful tuning of chunk sizes and overlap strategies

## Future Considerations

Future enhancements may include:

* Configurable chunk sizes
* Chunk overlap support
* Semantic chunk boundaries
* Metadata enrichment
* Hierarchical chunking
* Source-aware chunking strategies

These enhancements should remain compatible with the common `Chunker` contract and should not require modifications to downstream embedding or retrieval components.
