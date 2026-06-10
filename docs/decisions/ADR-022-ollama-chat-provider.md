# ADR-022: Ollama Chat Provider

## Status

Accepted

## Context

Cortex requires a language model interface capable of generating natural language responses from user prompts.

The initial implementation utilized a mock AI provider to establish service contracts, API workflows, testing strategies, and provider abstractions without requiring a running language model.

As Cortex evolves from architectural scaffolding to a functional AI platform, a production-capable inference provider is required.

The platform must support:

* Local inference
* Provider abstraction
* Offline operation
* Minimal infrastructure complexity
* Future multi-model support

Several approaches were considered:

* OpenAI API
* Azure OpenAI
* Anthropic Claude
* Local Hugging Face Models
* Ollama

Cortex follows a Local First architecture philosophy where AI capabilities should execute locally whenever practical.

Ollama provides:

* Local model execution
* Simple HTTP API
* Model management
* Multi-model support
* Minimal operational overhead

The platform already utilizes Ollama for embedding generation through the `nomic-embed-text` model.

Extending Ollama to chat generation creates a unified local AI runtime architecture.

---

## Decision

Adopt Ollama as the primary chat inference provider for Cortex.

The initial chat model will be:

```text
llama3.2
```

The implementation will conform to the existing `AIProvider` abstraction.

Application services will continue interacting exclusively through:

```text
AIProvider
```

and will remain independent of Ollama-specific implementation details.

---

## Architecture

```text
User Prompt
     │
     ▼
Chat Service
     │
     ▼
AI Provider
     │
     ▼
Ollama Provider
     │
     ▼
llama3.2
     │
     ▼
Generated Response
```

---

## Design Principles

### Provider Abstraction

Business logic must not depend directly on Ollama APIs.

Application services interact exclusively through:

```text
AIProvider
```

This allows future providers to be introduced without modifying application workflows.

Potential future providers include:

* OpenAI
* Azure OpenAI
* Anthropic
* Local Hugging Face Models
* Enterprise-hosted LLMs

### Local-First Inference

Language model execution should occur locally whenever possible.

Benefits include:

* Improved privacy
* Reduced operational cost
* Reduced external dependencies
* Offline capability
* Faster experimentation

### Infrastructure Consistency

Cortex already utilizes Ollama for embeddings.

Using Ollama for both:

```text
Embeddings
Chat Inference
```

creates a consistent AI infrastructure layer.

### Separation of Concerns

The provider is responsible only for:

* Prompt submission
* Response generation

The provider is not responsible for:

* Retrieval
* Prompt construction
* Knowledge indexing
* Context management
* Agent orchestration

These responsibilities remain within dedicated services.

---

## Model Selection

The initial model selected is:

```text
llama3.2
```

Selection criteria:

* Strong general-purpose reasoning
* Lightweight local deployment
* Fast inference
* Stable Ollama support
* Suitable for development environments

Future models may include:

```text
llama3.3
mistral
deepseek-r1
qwen
codellama
```

The provider abstraction ensures model changes remain configuration-driven.

---

## Configuration Strategy

The active model is controlled through environment configuration.

Example:

```env
AI_PROVIDER=ollama

OLLAMA_HOST=http://localhost:11434

OLLAMA_MODEL=llama3.2
```

No application code changes are required when switching models.

---

## Consequences

### Positive

* Real language generation
* Local execution
* Reduced cloud dependency
* Consistent AI runtime architecture
* Simplified development workflow
* Privacy-preserving inference

### Negative

* Increased local resource consumption
* Model download requirements
* Dependency on local Ollama runtime availability

---

## Future Considerations

### Streaming Responses

Future implementations may support:

```text
Token Streaming
```

to improve user experience and reduce perceived latency.

### Multi-Model Routing

Future versions may dynamically select models based on:

* Query complexity
* Cost requirements
* Task type
* Latency requirements

### Conversation Memory

Future chat workflows may introduce:

* Session memory
* Context persistence
* Long-term memory integration

without modifying the provider contract.

### Agent Integration

Future agent workflows may invoke the chat provider as part of:

```text
Planning
Reasoning
Tool Usage
Reflection
```

pipelines.

### Evaluation Framework

Future releases may include:

* Prompt evaluation
* Response quality measurement
* Regression testing
* Benchmarking

for model governance and operational reliability.

---

## Alternatives Considered

### OpenAI API

Pros:

* Strong model performance
* Managed infrastructure

Cons:

* External dependency
* Usage costs
* Privacy considerations

### Azure OpenAI

Pros:

* Enterprise integration
* Governance capabilities

Cons:

* Cloud dependency
* Increased operational complexity

### Hugging Face Local Models

Pros:

* Full local control

Cons:

* Larger setup complexity
* Hardware compatibility challenges
* Model lifecycle management burden

### Anthropic Claude

Pros:

* Strong reasoning capabilities

Cons:

* Cloud dependency
* External API costs

---

## Related Decisions

* ADR-012: AI Service Abstraction Layer
* ADR-013: Service Layer Pattern
* ADR-020: Ollama Embedding Provider
* ADR-021: Qdrant Vector Store Provider

---

## Outcome

This decision removes the final major mock component from Cortex's AI stack.

After implementation, Cortex operates using:

```text
Ollama Embeddings
        +
Qdrant Retrieval
        +
Ollama Chat Generation
```

establishing the foundation for Retrieval-Augmented Generation (RAG), agent orchestration, memory systems, and future GraphRAG capabilities.
