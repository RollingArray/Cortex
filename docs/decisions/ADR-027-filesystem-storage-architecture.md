# ADR-027: Filesystem Storage Architecture

**Status:** Accepted

**Date:** 2026-07-23

**Authors:** Ranjoy Sen

---

# Context

Cortex is an AI-powered document intelligence platform where users upload engineering and enterprise documents for ingestion, indexing, retrieval, and AI-assisted analysis.

Uploaded documents are frequently large binary assets (PDF, DOCX, PPTX, images, spreadsheets, etc.) that require multiple downstream processing stages including:

- Metadata extraction
- OCR
- Text extraction
- Chunk generation
- Embedding creation
- Vector indexing
- AI retrieval

These files can easily exceed several megabytes in size and should not be stored directly inside the relational database.

The platform therefore requires a storage architecture that:

- Separates binary content from application metadata
- Supports efficient file I/O
- Allows future migration to cloud object storage
- Maintains transactional consistency between the database and filesystem
- Enables deterministic file organization

---

# Decision

Cortex will store document binaries on the filesystem while storing only document metadata inside the relational database.

Each uploaded document is represented by two independent concepts:

- Document metadata (database)
- Document binary (filesystem)

The document entity stores only the information necessary to locate the binary file.

```
Document
│
├── id
├── workspace_id
├── original_filename
├── storage_directory
├── storage_filename
├── checksum
├── size
├── mime_type
└── status
```

---

# Storage Layout

Each workspace owns an isolated directory.

```
data/
└── workspaces/
    ├── 7b84d2d6-4ab2-4f60-b4b4-a68c8f01c2b1/
    │   ├── 5c21e5d8-8fd0-4a55-b07f-ff0e50d6c92e.pdf
    │   ├── 90dd3ce2-acde-4df5-8d7f-f1f5c41717db.docx
    │   └── ...
    │
    └── c41e22bb-3f02-4b95-a73d-0f7bc0f9a777/
```

Each uploaded file receives a UUID-based storage filename while preserving the original filename within the database.

Example:

```
original_filename = Aircraft Design Review.pdf

storage_directory = workspaces/7b84d2d6-4ab2-4f60-b4b4-a68c8f01c2b1

storage_filename = 5c21e5d8-8fd0-4a55-b07f-ff0e50d6c92e.pdf
```

---

# Rationale

Separating storage location into two independent fields provides several advantages.

## Stable Storage Location

Directories and filenames evolve independently.

Future layouts such as:

```
archive/
parsed/
thumbnails/
chunks/
```

can be introduced without modifying database semantics.

---

## Original Filename Preservation

Users continue to see:

```
Aircraft Design Review.pdf
```

while Cortex internally stores

```
5c21e5d8-8fd0-4a55-b07f-ff0e50d6c92e.pdf
```

This avoids collisions between documents having identical filenames.

---

## Cloud Storage Migration

The storage abstraction intentionally avoids exposing filesystem paths.

Future implementations may replace the local filesystem with:

- Amazon S3
- Azure Blob Storage
- Google Cloud Storage
- Enterprise NAS
- Object Storage

without impacting business services.

---

# Storage Service Responsibilities

Filesystem operations are centralized within the StorageService.

Business services never manipulate filesystem paths directly.

StorageService provides:

- Workspace directory creation
- Storage filename generation
- Absolute path resolution
- File persistence
- File deletion
- Workspace cleanup
- File existence checks

This establishes StorageService as the single filesystem abstraction for Cortex.

---

# Transaction Model

Document uploads follow the sequence below.

```
Client
   │
   ▼
DocumentService
   │
   ├── Generate storage location
   ├── Save binary file
   ├── Persist metadata
   └── Commit transaction
```

If database persistence fails after writing the file, the uploaded binary is immediately removed to maintain consistency.

Likewise, document deletion removes both:

- Database record
- Physical file

---

# Workspace Cleanup

Workspace directories are created lazily during the first document upload.

When the final document belonging to a workspace is deleted:

- remaining files are removed
- empty directories are deleted

Deleting a workspace recursively removes the associated storage hierarchy.

---

# Consequences

## Advantages

- Small relational database
- Fast filesystem I/O
- Clean separation of metadata and binary content
- Cloud storage ready
- Deterministic directory layout
- Simple backup strategy
- UUID collision avoidance
- Centralized storage abstraction

## Trade-offs

- Filesystem must remain synchronized with the database.
- Storage operations require rollback logic during failures.
- Additional service abstraction is required compared to storing files directly in the database.

---

# Alternatives Considered

## Store binary files inside the database

Rejected because:

- Increased database size
- Poor backup performance
- Slower binary retrieval
- Limited scalability

---

## Store a single storage_path field

Example:

```
workspaces/123/document.pdf
```

Rejected because:

- Combines directory and filename into one value
- Harder to refactor storage layout
- Less flexible for future storage providers

The adopted design stores:

- storage_directory
- storage_filename

independently.

---

# Future Considerations

The StorageService abstraction enables future enhancements including:

- Cloud object storage
- File versioning
- Archived document storage
- Thumbnail generation
- OCR artifact storage
- Parsed text persistence
- Chunk cache storage
- Encryption at rest
- Storage lifecycle management

without requiring changes to the service layer or domain model.