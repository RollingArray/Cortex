# Cortex Developer Setup Guide

## Overview

This guide explains how to set up Cortex on a new machine from scratch.

Current technology stack:

* Python 3.11
* UV
* FastAPI
* Uvicorn
* Git

---

## Prerequisites

### Install Git

Verify:

```bash
git --version
```

---

### Install Python 3.11

Verify:

```bash
python3 --version
```

Expected:

```text
Python 3.11.x
```

Important:

Cortex currently targets Python 3.11 and above.

---

### Install UV

Install:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reload shell:

```bash
source ~/.zshrc
```

Verify:

```bash
uv --version
```

---

## Clone Repository

```bash
git clone <repository-url>
cd cortex
```

---

## Verify Python Version

Check:

```bash
cat .python-version
```

Expected:

```text
3.11.3
```

Verify UV runtime:

```bash
uv run python --version
```

Expected:

```text
Python 3.11.3
```

---

## Create Virtual Environment

```bash
uv venv --python /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
```

Activate:

```bash
source .venv/bin/activate
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.11.3
```

---

## Install Dependencies

```bash
uv sync
```

This installs all dependencies defined in:

* pyproject.toml
* uv.lock

---

## Start Cortex

```bash
uv run uvicorn app.main:app --reload
```

Expected:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Verify Service

Open:

http://localhost:8000

Expected response:

```json
{
  "application": "cortex",
  "version": "0.1.0",
  "status": "running"
}
```

---

## API Documentation

Open:

http://localhost:8000/docs

Swagger UI should load successfully.

---

## Troubleshooting

### UV uses wrong Python version

Check:

```bash
cat .python-version
```

Update:

```bash
uv python pin 3.11.3
```

Verify:

```bash
uv run python --version
```

---

### Rebuild Environment

Remove environment:

```bash
rm -rf .venv
```

Recreate:

```bash
uv venv --python /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```
