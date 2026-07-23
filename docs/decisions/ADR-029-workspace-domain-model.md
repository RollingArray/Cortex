# ADR-029: Workspace Domain Model

**Status:** Accepted

**Date:** 2026-07-23

**Authors:** Ranjoy Sen

---

# Context

Cortex is an AI-powered knowledge platform that enables users to organize, ingest, search, and interact with enterprise documents.

As the platform evolves, it will support multiple AI capabilities including:

- Document ingestion
- Semantic search
- Retrieval-Augmented Generation (RAG)
- AI chat
- Knowledge management
- Agents
- Future collaborative workspaces

A clear domain model is required to organize these capabilities while maintaining ownership boundaries and lifecycle management.

The architecture therefore requires a logical aggregate that groups all user-owned resources.

---

# Decision

Cortex adopts **Workspace** as the primary aggregate root within the domain model.

Every document belongs to exactly one workspace.

All future AI resources will also be owned by a workspace.

The Workspace represents the primary boundary for:

- ownership
- lifecycle
- authorization
- storage
- indexing
- retrieval

---

# Domain Model

The initial domain model consists of two primary entities.

```
Workspace
    │
    ├── id
    ├── name
    ├── description
    ├── workspace_type
    ├── created_at
    └── updated_at
          │
          │ 1
          │
          ▼
        Documents
```

A workspace may contain zero or more documents.

Each document belongs to exactly one workspace.

```
Workspace (1)
      │
      │
      ├───────────────┐
      ▼               ▼
Document         Document
      │               │
      ▼               ▼
 Embeddings      Embeddings
```

The workspace owns the complete lifecycle of its documents.

---

# Aggregate Root

Workspace is treated as the aggregate root.

Business operations affecting child entities should be coordinated through the workspace boundary where appropriate.

Examples include:

- Workspace deletion
- Workspace export
- Workspace archival
- Workspace statistics

Deleting a workspace removes all owned resources.

---

# Document Ownership

Each document contains a mandatory workspace identifier.

```
Document

id

workspace_id

original_filename

storage_directory

storage_filename

status
```

Documents cannot exist independently of a workspace.

Moving a document between workspaces is considered an explicit business operation.

---

# Storage Organization

The filesystem mirrors the domain hierarchy.

```
Workspace
        │
        ▼
Filesystem

data/
└── workspaces/
    └── <workspace-id>/
            ├── document-1.pdf
            ├── document-2.docx
            └── ...
```

This alignment keeps the domain model and storage architecture consistent.

---

# Retrieval Scope

Retrieval operations are scoped by workspace.

Example:

```
User Question
        │
        ▼
Workspace
        │
        ▼
Retrieve Documents
        │
        ▼
Vector Search
        │
        ▼
LLM
```

This prevents unrelated documents from participating in retrieval unless explicitly requested.

Workspace boundaries therefore define the default knowledge scope for AI interactions.

---

# Future Domain Expansion

The Workspace aggregate is designed to evolve.

Future resources may include:

```
Workspace
│
├── Documents
├── Collections
├── Conversations
├── AI Agents
├── Prompt Libraries
├── Knowledge Graphs
├── Saved Searches
├── Tags
├── Shared Resources
└── User Permissions
```

These capabilities inherit the same ownership and lifecycle semantics.

---

# Lifecycle Management

Workspace creation provisions the logical container.

During its lifecycle, a workspace may:

- receive uploaded documents
- generate embeddings
- build vector indexes
- support AI conversations
- maintain metadata
- accumulate usage statistics

Deleting a workspace removes:

- document metadata
- physical files
- extracted text
- chunks
- embeddings
- vector entries
- AI artifacts
- future workspace-owned resources

The WorkspaceService coordinates these operations.

---

# Identity Strategy

Both workspaces and documents use UUID identifiers.

Benefits include:

- globally unique identifiers
- safe distributed generation
- storage independence
- cloud compatibility
- simplified synchronization

UUIDs remain stable throughout the lifetime of the entity.

---

# Service Responsibilities

The domain model is reflected in the service layer.

```
WorkspaceService
        │
        ├── WorkspaceRepository
        ├── DocumentService
        └── StorageService
```

WorkspaceService coordinates operations spanning multiple resources while delegating specialized behavior to dependent services.

---

# Benefits

The Workspace aggregate provides:

## Clear Ownership

Every resource has a single owner.

---

## Lifecycle Consistency

Deleting a workspace guarantees removal of all dependent resources.

---

## Authorization Boundary

Future security models can authorize access at the workspace level rather than individual resources.

---

## Retrieval Isolation

AI retrieval naturally remains within the intended knowledge boundary.

---

## Scalability

Additional domain entities can be introduced without changing the overall architectural model.

---

# Consequences

## Advantages

- Well-defined aggregate root
- Clean ownership model
- Consistent storage hierarchy
- Simplified lifecycle management
- Natural authorization boundary
- Future-ready domain structure
- Supports enterprise collaboration

## Trade-offs

- Cross-workspace operations require explicit orchestration.
- Resource migration between workspaces becomes a managed business process.
- Additional coordination is required for shared resources.

These trade-offs are acceptable because they preserve clear domain boundaries.

---

# Alternatives Considered

## Flat Document Model

Documents exist independently.

Rejected because:

- no ownership boundary
- difficult lifecycle management
- poor scalability
- weak authorization model

---

## Folder-Based Organization

Treat folders as the primary container.

Rejected because:

- folders represent storage concerns rather than business concepts
- does not naturally support AI conversations or future collaborative capabilities

---

## Project-Centric Model

Use Projects instead of Workspaces.

Rejected because:

- projects imply engineering-specific semantics
- workspace is a broader concept applicable to multiple enterprise use cases

Workspace better represents an isolated knowledge boundary.

---

# Future Considerations

The Workspace aggregate provides the foundation for future Cortex capabilities including:

- Multi-user collaboration
- Role-based access control
- Workspace sharing
- AI agents
- Conversation history
- Knowledge graphs
- Prompt libraries
- Background processing
- Workspace import/export
- Enterprise synchronization

By establishing Workspace as the aggregate root, Cortex maintains a consistent domain model that can evolve without requiring significant architectural changes.