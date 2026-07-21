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
ENVIRONMENT=local uv run uvicorn backend.main:app --reload
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
## Verify Service Endpoints

The following endpoints should be available after Cortex starts successfully.

Base URL:

```text
http://localhost:8000
```

---

### Root Endpoint

Open:

```text
http://localhost:8000/
```

Expected:

```json
{
  "message": "Welcome to Cortex"
}
```

---

### Health Endpoint

Open:

```text
http://localhost:8000/api/v1/health
```

Expected:

```json
{
  "success": true,
  "status": "healthy"
}
```

Purpose:

* Liveness checks
* Service monitoring
* Operational validation

---

### Readiness Endpoint

Open:

```text
http://localhost:8000/api/v1/ready
```

Expected:

```json
{
  "success": true,
  "status": "ready"
}
```

Purpose:

* Readiness validation
* Future dependency verification
* Deployment health checks

---

### Service Metadata Endpoint

Open:

```text
http://localhost:8000/api/v1/info
```

Expected:

```json
{
  "success": true,
  "application": "Cortex",
  "version": "0.1.0",
  "environment": "local"
}
```

Purpose:

* Environment verification
* Runtime metadata inspection

---

### Chat Endpoint

Open Swagger UI:

```text
http://localhost:8000/docs
```

Locate:

```text
POST /api/v1/chat
```

Example Request:

```json
{
  "prompt": "What is Cortex?"
}
```

Expected Response:

```json
{
  "success": true,
  "response": "Mock response for: What is Cortex?"
}
```

Purpose:

* Validate AI provider abstraction
* Verify chat service integration
* Confirm provider factory configuration

---

### Retrieval Endpoint

Open Swagger UI:

```text
http://localhost:8000/docs
```

Locate:

```text
POST /api/v1/retrieve
```

Example Request:

```json
{
  "query": "What is Cortex?"
}
```

Expected Response:

```json
{
  "success": true,
  "results": [
    "Cortex is an AI platform"
  ]
}
```

Purpose:

* Validate retrieval service
* Verify vector store integration
* Confirm knowledge retrieval workflow

Note:

Retrieval results depend on indexed content being available.

---

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI Specification:

```text
http://localhost:8000/openapi.json
```

Swagger should expose all currently registered endpoints.

Typical endpoints include:

```text
GET    /
GET    /api/v1/health
GET    /api/v1/ready
GET    /api/v1/info
POST   /api/v1/chat
POST   /api/v1/retrieve
```


## Install Ollama

Cortex uses Ollama for local AI model execution.

### Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify installation:

```bash
ollama --version
```

Expected:

```text
ollama version x.x.x
```

---

## Verify Ollama Service

Check that the Ollama runtime is available:

```bash
curl http://localhost:11434/api/tags
```

Expected response:

```json
{
  "models": []
}
```

or a list of installed models.

---

## Download Required Models

### Chat Model

```bash
ollama pull llama3.2
```

### Embedding Model

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

Expected:

```text
NAME
llama3.2
nomic-embed-text
```

---

## Environment Configuration

Verify:

```bash
cat configs/environments/local.env
```

Expected values:

```env
AI_PROVIDER=mock

EMBEDDING_PROVIDER=ollama

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

---

## Run Integration Tests

Execute:

```bash
pytest tests/integration -v
```

Expected:

```text
PASSED
```

for all Ollama integration tests.

---

## Verify Embedding Generation

Run:

```bash
pytest tests/integration/test_ollama_embeddings.py -v
```

Expected:

```text
PASSED
```

This confirms:

* Ollama runtime is available
* Embedding model is installed
* Cortex can generate real embeddings
* Configuration is valid
