# Cortex - Rebuild Database

Author: Ranjoy Sen

Purpose
-------
Recreate the Cortex development database from scratch.

Use this procedure whenever:
- The domain model changes significantly.
- Initial development is ongoing.
- Existing data does not need to be preserved.

---

## Step 1 - Stop the API

If the FastAPI server is running, stop it.

```
CTRL + C
```

---

## Step 2 - Remove Existing Database

### SQLite

```
rm cortex.db
```

If your SQLite database has a different name or location:

```
find . -name "*.db"
```

Delete the appropriate database.

---

## Step 3 - Remove Existing Alembic Migrations

Delete all migration versions.

```
rm -rf backend/migrations/versions/*
```

Verify:

```
ls backend/migrations/versions
```

The directory should now be empty.

---

## Step 4 - Generate a New Initial Migration

```
alembic -c backend/alembic.ini revision --autogenerate -m "Initial schema"
```

Verify the migration:

```
ls backend/migrations/versions
```

---

## Step 5 - Review the Generated Migration

Open the generated migration.

Confirm:

- All tables are present.
- All indexes are created.
- All foreign keys are correct.
- New columns exist.
- Removed columns no longer exist.

Example:

```
Document

✓ storage_directory
✓ storage_filename

✗ storage_path
```

---

## Step 6 - Create Database

```
alembic -c backend/alembic.ini upgrade head
```

---

## Step 7 - Verify Migration State

```
alembic -c backend/alembic.ini current
```

Expected:

```
<revision_id> (head)
```

---

## Step 8 - Start API

```
uvicorn backend.main:app --reload
```

---

## Step 9 - Verify API

Open

```
http://localhost:8000/docs
```

Verify Swagger loads successfully.

---

## Step 10 - Upload a Test Document

Upload a PDF using Swagger.

Verify:

### Database

Document table contains:

```
original_filename
storage_directory
storage_filename
checksum
status
```

Example

storage_directory

```
workspaces/128a5409-20b8-4935-ac59-a14e292e895f
```

storage_filename

```
6ab7e8d9-40e8-4805-b185-a4c4541c5f90.pdf
```

---

## Step 11 - Verify Filesystem

```
tree storage
```

Expected

```
storage
└── workspaces
    └── <workspace-id>
        └── <document-id>.pdf
```

---

## Step 12 - Verify Duplicate Detection

Upload the same file again.

Expected

HTTP

```
409 Conflict
```

Filesystem

```
No additional file created.
```

Database

```
No additional document row created.
```

---

## Step 13 - Verify Delete Document

Delete the uploaded document.

Verify

Database

```
Document removed
```

Filesystem

```
PDF removed
```

Workspace directory

```
Automatically removed if empty.
```

---

## Step 14 - Verify Delete Workspace

Delete the workspace.

Verify

Database

```
Workspace removed
Documents removed
```

Filesystem

```
Workspace directory removed
```

---

# Useful Alembic Commands

Create migration

```
alembic revision --autogenerate -m "Description"
```

Apply migrations

```
alembic upgrade head
```

Rollback one migration

```
alembic downgrade -1
```

Rollback to base

```
alembic downgrade base
```

Show current revision

```
alembic current
```

Show migration history

```
alembic history
```

Show SQL without executing

```
alembic upgrade head --sql
```

---

# Notes

During early development, rebuilding the database is preferred over writing
complex migrations.

Once Cortex reaches production readiness, schema evolution should always be
performed through Alembic migrations without rebuilding the database.