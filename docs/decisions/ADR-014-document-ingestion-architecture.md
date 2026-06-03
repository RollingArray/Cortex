# ADR-014: Document Ingestion Architecture

## Status

Accepted

## Context

Cortex is intended to evolve into a knowledge and reasoning platform capable of retrieving information from a variety of data sources.

Future knowledge sources may include:

* Plain text documents
* PDF files
* Microsoft Word documents
* Markdown files
* HTML pages
* CSV datasets
* Structured enterprise content

Each document format requires different extraction logic, but the downstream retrieval pipeline should operate on a common representation of content.

Coupling ingestion logic directly to specific file formats would increase complexity and make future extensions difficult.

A standardized document ingestion architecture is required.

## Decision

Introduce a dedicated document ingestion layer responsible for loading and normalizing source content.

All document loaders must implement a common interface through a shared `DocumentLoader` contract.

Document loaders are responsible only for:

* Accessing source content
* Extracting raw text
* Producing a standardized document representation

Document loaders are not responsible for:

* Chunking
* Embedding generation
* Vector storage
* Retrieval
* LLM interactions

The initial implementation will support plain text documents through a `TextLoader`.

Future loaders will extend the same contract without requiring changes to downstream components.

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
Chunking Pipeline
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

## Consequences

### Positive

* Clear separation of concerns
* Extensible ingestion framework
* Consistent document representation
* Simplified testing
* Reduced coupling between ingestion and retrieval components
* Easier support for additional document formats

### Negative

* Additional abstraction layer
* More implementation classes as supported formats increase
* Slight increase in architectural complexity

## Future Considerations

Potential future loader implementations include:

* PDFLoader
* DocxLoader
* MarkdownLoader
* HtmlLoader
* CsvLoader
* JsonLoader

These implementations should adhere to the same `DocumentLoader` contract and produce the same standardized document representation.
