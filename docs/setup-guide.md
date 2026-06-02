# Cortex Developer Setup Guide

## Overview

This guide explains how to set up Cortex on a new machine from scratch.

Current technology stack:

* Python 3.11
* UV
* FastAPI
* Uvicorn
* Pydantic Settings
* YAML-based Logging
* Git

---

## Prerequisites

### Install Git

Verify installation:

```bash
git --version
```

---

### Install Python 3.11

Verify installation:

```bash
python3 --version
```

Expected:

```text
Python 3.11.x
```

Cortex currently targets Python 3.11 and above.

---

### Install UV

Install UV:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reload shell:

```bash
source ~/.zshrc
```

Verify installation:

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

Check project runtime:

```bash
cat .python-version
```

Expected:

```text
3.11
```

Verify UV runtime:

```bash
uv run python --version
```

Expected:

```text
Python 3.11.x
```

---

## Create Virtual Environment

Create virtual environment:

```bash
uv venv
```

Activate environment:

```bash
source .venv/bin/activate
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.11.x
```

---

## Install Dependencies

Install all project dependencies:

```bash
uv sync
```

Dependencies are managed through:

* pyproject.toml
* uv.lock

---

## Verify Repository Structure

Run:

```bash
tree -L 2
```

Expected structure:

```text
.
├── app
├── configs
├── docs
├── logs
├── scripts
├── tests
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Verify Environment Configuration

Run:

```bash
ls configs/environments
```

Expected:

```text
local.env
dev.env
staging.env
prod.env
```

---

## Start Cortex

Run Cortex in local environment:

```bash
ENVIRONMENT=local uv run uvicorn app.main:app --reload
```

Expected:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Verify Service Endpoints

### Health Endpoint

Open:

```text
http://localhost:8000/api/v1/health
```

Expected:

```json
{
  "status": "healthy"
}
```

---

### Readiness Endpoint

Open:

```text
http://localhost:8000/api/v1/ready
```

Expected:

```json
{
  "status": "ready"
}
```

---

### Service Metadata Endpoint

Open:

```text
http://localhost:8000/api/v1/info
```

Expected:

```json
{
  "application": "Cortex",
  "version": "0.1.0",
  "environment": "local"
}
```

---

## Verify API Documentation

Open:

```text
http://localhost:8000/docs
```

Swagger UI should load successfully.

---

## Verify Logging

Invoke the health endpoint:

```text
http://localhost:8000/api/v1/health
```

Verify logs:

```bash
cat logs/cortex.log
```

Expected output should contain entries similar to:

```text
Cortex application started
Health endpoint invoked
```

Error logs are written to:

```text
logs/cortex-error.log
```

---

## Verify Environment Loading

Edit:

```text
configs/environments/local.env
```

Temporarily change:

```bash
APP_NAME=Cortex
```

to:

```bash
APP_NAME=Cortex-Local
```

Restart Cortex.

Verify:

```text
http://localhost:8000/api/v1/info
```

Expected:

```json
{
  "application": "Cortex-Local"
}
```

Revert the change after validation.

---

## Common Development Commands

### Activate Virtual Environment

```bash
source .venv/bin/activate
```

### Install New Dependency

```bash
uv add <package-name>
```

### Synchronize Dependencies

```bash
uv sync
```

### Run Cortex

```bash
ENVIRONMENT=local uv run uvicorn app.main:app --reload
```

### View Application Logs

```bash
tail -f logs/cortex.log
```

### View Error Logs

```bash
tail -f logs/cortex-error.log
```

### Run Tests

```bash
pytest
```

### Git Status

```bash
git status
```

---

## Current Repository Layout

```text
cortex/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── configs/
│   ├── environments/
│   ├── logging/
│   ├── models/
│   ├── prompts/
│   └── retrieval/
│
├── docs/
│   └── decisions/
│
├── logs/
├── scripts/
├── tests/
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Troubleshooting

### Incorrect Python Version

Verify:

```bash
cat .python-version
```

Update if necessary:

```bash
uv python pin 3.11
```

Verify:

```bash
uv run python --version
```

---

### Rebuild Virtual Environment

Remove environment:

```bash
rm -rf .venv
```

Create environment:

```bash
uv venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

---

### Logging Not Working

Verify logging configuration:

```bash
ls configs/logging
```

Expected:

```text
local.yaml
dev.yaml
staging.yaml
prod.yaml
```

Check application logs:

```bash
tail -f logs/cortex.log
```

Verify application starts successfully before testing endpoints.

```
```
