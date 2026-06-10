# ADR-023: Retrieval-Augmented Generation Pipeline

## Status

Accepted

## Context

Cortex has established the foundational components required for semantic retrieval:

* Document ingestion
* Document chunking
* Embedding generation
* Vector storage
* Similarity search
* Language model inference

Prior to this decision, retrieval and generation existed as independent workflows.

Retrieval workflow:

```text
Question
    ↓
Embedding
    ↓
Vector Search
    ↓
Relevant Chunks
```

Generation workflow:

```text
Prompt
    ↓
Language Model
    ↓
Response
```

While both capabilities functioned independently, the language model had no awareness of retrieved knowledge and therefore could not generate grounded responses based on indexed content.

Cortex requires a mechanism to combine retrieval and generation into a unified workflow capable of answering questions using organizational knowledge.

This pattern is commonly referred to as Retrieval-Augmented Generation (RAG).

---

## Decision

Adopt a Retrieval-Augmented Generation pipeline as the primary question-answering workflow within Cortex.

The pipeline will:

1. Receive a user question
2. Generate a query embedding
3. Retrieve relevant knowledge from Qdrant
4. Construct a contextualized prompt
5. Invoke the language model
6. Generate a grounded response

The RAG workflow will be implemented as a dedicated service layer and exposed through a dedicated API endpoint.

---

## Architecture

```text
User Question
      │
      ▼
Embedding Provider
      │
      ▼
Query Embedding
      │
      ▼
Qdrant Retrieval
      │
      ▼
Relevant Context
      │
      ▼
Prompt Construction
      │
      ▼
Ollama Provider
      │
      ▼
Generated Answer
```

---

## Service Responsibilities

### Embedding Provider

Responsible for:

* Query embedding generation

Not responsible for:

* Retrieval
* Prompt construction
* Response generation

---

### Vector Store

Responsible for:

* Similarity search
* Knowledge retrieval

Not responsible for:

* Embedding generation
* Response generation

---

### AI Provider

Responsible for:

* Language model interaction
* Text generation

Not responsible for:

* Knowledge retrieval
* Prompt engineering
* Context assembly

---

### RAG Service

Responsible for:

* Retrieval orchestration
* Context assembly
* Prompt construction
* End-to-end answer generation

The RAG service becomes the coordination layer connecting retrieval and generation.

---

## Prompt Strategy

The initial implementation uses a grounded-answer prompt.

Example:

```text
Use the provided context to answer the question.

If the answer cannot be found in the context,
say so clearly.

Context:
{retrieved_context}

Question:
{question}

Answer:
```

This approach encourages:

* Grounded responses
* Reduced hallucinations
* Traceable reasoning

---

## API Strategy

A dedicated endpoint is introduced:

```text
POST /api/v1/ask
```

Request:

```json
{
  "question": "What is Cortex?"
}
```

Response:

```json
{
  "answer": "Cortex is an AI-powered knowledge and reasoning platform.",
  "retrieved_chunks": [
    "Cortex is an AI-powered knowledge and reasoning platform."
  ]
}
```

This endpoint becomes the primary interaction point for retrieval-augmented question answering.

---

## Design Principles

### Retrieval First

Knowledge should be retrieved before generation whenever possible.

The language model should reason over retrieved information rather than rely solely on model parameters.

---

### Grounded Responses

Answers should be based on retrieved context.

When relevant information cannot be located, the system should explicitly indicate that the answer is unavailable.

---

### Separation of Concerns

Retrieval, generation, and orchestration remain independent services.

This allows individual components to evolve without affecting the overall architecture.

---

### Provider Independence

The RAG workflow remains independent of:

* Embedding provider implementation
* Vector store implementation
* Language model implementation

Future provider replacements should require only configuration changes.

---

## Consequences

### Positive

* Grounded answer generation
* Reduced hallucination risk
* Better utilization of organizational knowledge
* Provider-independent architecture
* Clear separation of responsibilities
* Foundation for future GraphRAG workflows

### Negative

* Increased request latency
* Additional orchestration complexity
* Prompt construction overhead
* Dependency on retrieval quality

---

## Future Considerations

### Source Attribution

Future responses should include:

* Source documents
* Chunk references
* Similarity scores

Example:

```json
{
  "answer": "...",
  "sources": [
    {
      "source": "cortex.txt",
      "score": 0.95
    }
  ]
}
```

---

### Citation-Aware Generation

Future prompts may require the model to reference retrieved sources directly within generated answers.

---

### Conversation Memory

Future workflows may combine:

* Retrieval
* Short-term memory
* Long-term memory

to support multi-turn conversations.

---

### GraphRAG

Future versions may augment retrieval with:

* Neo4j knowledge graphs
* Relationship traversal
* Multi-hop reasoning

without changing the external API contract.

---

### Hybrid Retrieval

Future implementations may combine:

* Vector similarity
* Keyword search
* Metadata filtering

within a unified retrieval workflow.

---

## Alternatives Considered

### Retrieval-Only

Pros:

* Simpler implementation

Cons:

* No natural language answer generation

---

### Generation-Only

Pros:

* Simpler user experience

Cons:

* No access to indexed knowledge
* Higher hallucination risk

---

### Agent-Based Retrieval

Pros:

* Flexible orchestration

Cons:

* Unnecessary complexity for current requirements

---

## Related Decisions

* ADR-018: Knowledge Indexing Pipeline
* ADR-019: Retrieval Service Architecture
* ADR-020: Ollama Embedding Provider
* ADR-021: Qdrant Vector Store Provider
* ADR-022: Ollama Chat Provider

---

## Outcome

This decision establishes the first complete Retrieval-Augmented Generation workflow within Cortex.

After implementation, Cortex is capable of:

```text
Question
    ↓
Knowledge Retrieval
    ↓
Context Assembly
    ↓
Language Model Generation
    ↓
Grounded Answer
```

This marks the completion of the initial Retrieval Platform architecture and provides the foundation for source attribution, memory systems, agent orchestration, and future GraphRAG capabilities.
