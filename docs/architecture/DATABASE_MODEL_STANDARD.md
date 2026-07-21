# Database Model Standard

**Project:** Cortex  
**Author:** Ranjoy Sen  
**Status:** Approved  
**Version:** 1.0

---

# Purpose

This document defines the database modelling standards for the Cortex
platform.

The objective is to ensure every database entity is:

- Consistent
- Maintainable
- Extensible
- Enterprise-ready
- Easy to review
- Easy to understand
- Safe to evolve

Every database model MUST conform to this standard.

---

# Design Principles

The Cortex data model follows these principles.

1. Database integrity is enforced by the database.
2. Business behaviour belongs in services, not models.
3. Models represent business entities.
4. Relationships are explicit.
5. Naming is predictable.
6. Every model should remain readable regardless of size.
7. Every entity should be extensible without requiring redesign.

---

# Model File Structure

Every model should follow the same structure.

```python
File Header

Imports

TYPE_CHECKING

Class Definition

    __tablename__

    __table_args__

    Identity

    Foreign Keys

    Business Fields

    Classification

    Processing

    Relationships

    Computed Properties

    Helper Methods
```

The ordering should never change.

---

# File Header

Every model must begin with the standard Cortex file header.

Example

```python
"""
Document Model

Author:
-------
Ranjoy Sen

Purpose:
--------
Defines the Document database entity.

Features:
---------
- Document identity
- Storage metadata
- Processing state
- Workspace ownership
"""
```

---

# Imports

Imports shall be grouped as follows.

```python
Standard Library

Third Party

Project Imports

TYPE_CHECKING Imports
```

Example

```python
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.models.entity import Entity

if TYPE_CHECKING:
    from backend.models.workspace import Workspace
```

---

# Base Class

Every persistent model MUST inherit from

```python
Entity
```

Never inherit directly from Base.

Entity provides

- UUID Primary Key
- Created Timestamp
- Updated Timestamp

---

# Table Name

Every model shall define

```python
__tablename__
```

Example

```python
__tablename__ = "documents"
```

Plural table names shall be used.

---

# Table Arguments

Every model should define

```python
__table_args__
```

Even if initially empty.

This section contains

- Indexes
- Constraints
- Unique Constraints
- Check Constraints

Example

```python
__table_args__ = (
    Index(
        "ix_documents_workspace_id",
        "workspace_id",
    ),
)
```

---

# Identity Section

The first section after table metadata.

```python
# -------------------------------------------------------------------------
# Identity
# -------------------------------------------------------------------------
```

Contains fields such as

- name
- title
- description

---

# Foreign Keys

All foreign keys shall appear together.

Example

```python
workspace_id = mapped_column(
    ForeignKey(
        "workspaces.id",
        name="fk_documents_workspaces",
        ondelete="CASCADE",
    ),
    nullable=False,
)
```

Rules

- Never store raw references without ForeignKey.
- Always define constraint names.
- Always define delete behaviour.

---

# Business Fields

Contains business information.

Examples

- filename
- checksum
- page_count
- mime_type
- size_bytes

No relationships belong here.

---

# Classification

Contains enums and classifications.

Examples

- status
- workspace_type
- security_level

Magic strings are prohibited.

---

# Processing Fields

Contains operational state.

Examples

- status
- processing_started_at
- processing_completed_at

This section should remain independent of business data.

---

# Relationships

Relationships must always be declared together.

Example

```python
workspace = relationship(
    "Workspace",
    back_populates="documents",
    lazy="selectin",
)
```

Rules

- Always use back_populates.
- Always specify loading strategy.
- Always use typed relationships.

---

# Computed Properties

Computed values only.

Example

```python
@property
def size_mb(self):
    ...
```

No database queries.

---

# Helper Methods

Small helper methods are permitted.

Example

```python
mark_ready()

mark_failed()
```

Business workflows belong in services.

---

# Naming Convention

Primary Keys

```
pk_<table>
```

Foreign Keys

```
fk_<table>_<referenced_table>
```

Indexes

```
ix_<table>_<column>
```

Unique Constraints

```
uq_<table>_<column>
```

Check Constraints

```
ck_<table>_<rule>
```

---

# Relationships

Every relationship should be bidirectional.

Example

```python
Workspace

↓

Documents

↓

Chunks

↓

Embeddings
```

Relationships should use

```python
back_populates
```

Never backref.

---

# Loading Strategy

Default

```python
lazy="selectin"
```

Other strategies require justification.

---

# Cascade Rules

Relationships should explicitly define cascade behaviour.

Preferred

```python
cascade="all, delete-orphan"
```

The default cascade behaviour should never be relied upon.

---

# Indexing Guidelines

Indexes should exist on

- Foreign Keys
- Frequently filtered columns
- Frequently sorted columns

Avoid unnecessary indexes.

Indexes increase write cost.

---

# Constraint Guidelines

Prefer database constraints over application validation.

Use

- Foreign Keys
- NOT NULL
- UNIQUE
- CHECK

Application validation is complementary, not a replacement.

---

# Enums

All enums belong under

```
backend/models/enums
```

Magic strings are prohibited.

---

# Soft Delete

Entities should prefer soft deletion where business rules require auditability.

Typical implementation

```text
deleted_at
deleted_by
```

Hard deletion should be reserved for data that has no audit requirements.

---

# Audit Fields

Every entity automatically contains

- id
- created_at
- updated_at

Additional audit fields may include

- created_by
- updated_by
- deleted_at
- deleted_by

---

# Lifecycle Documentation

Entities with processing stages should document their lifecycle.

Example

```
UPLOADED

↓

PROCESSING

↓

READY

↓

DELETED
```

This documentation should remain synchronized with the implementation.

---

# Things to Avoid

Do not

- Store duplicated information.
- Mix business logic into models.
- Store unrelated responsibilities.
- Create circular relationships.
- Use unnamed constraints.
- Use magic strings.
- Depend on implicit ORM behaviour.

---

# Review Checklist

Every model should satisfy the following.

- Standard file header
- Correct import ordering
- Inherits from Entity
- Uses plural table name
- Defines __table_args__
- Explicit constraint names
- Explicit foreign keys
- Typed relationships
- back_populates used
- Loading strategy defined
- Cascade defined
- Database constraints applied
- Indexes reviewed
- No business logic
- Lifecycle documented
- Follows Cortex naming conventions

Only after every item passes review should a model be merged.