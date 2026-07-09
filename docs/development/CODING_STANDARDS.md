# Cortex Coding Standards

Version: 1.0  
Last Updated: July 2026

---

# 1. Introduction

This document defines the coding standards, engineering principles and best
practices followed throughout the Cortex platform.

These standards apply to both the Angular frontend and Python backend to ensure
consistency, readability and maintainability across the entire codebase.

---

# 2. Engineering Principles

Cortex follows a small set of engineering principles.

- Keep code simple.
- Prefer readability over cleverness.
- Design for maintainability.
- Follow the Single Responsibility Principle.
- Build abstractions only when needed.
- Prefer composition over inheritance.
- Keep files focused on one purpose.
- Write code that explains itself.
- Optimize for long-term maintainability.

---

# 3. Architecture by Discovery

Cortex intentionally avoids speculative architecture.

Instead of building abstractions before they are needed, abstractions should
emerge naturally from repeated implementation patterns.

Preferred approach:

Build

↓

Repeat

↓

Recognize Pattern

↓

Abstract

↓

Reuse

Avoid creating:

- Components
- Services
- Models
- Enums
- Utilities

until there is a demonstrated need.

---

# 4. Project Structure

## Frontend

```
src/

├── core/
├── shared/
├── layout/
├── features/
├── environments/
└── theme/
```

### Core

Contains application infrastructure.

Examples:

- API services
- Configuration
- Guards
- Interceptors

### Shared

Contains reusable application assets.

Examples:

- Components
- Interfaces
- Models
- Constants
- Enums
- Pipes
- Utilities

### Layout

Contains application layout components.

Examples:

- Sidebar
- Topbar
- Status Bar
- Page Layout

### Features

Contains feature-specific implementation.

Examples:

- Dashboard
- Chat
- Documents
- Search
- Settings

---

## Backend

```
backend/

├── api/
├── core/
├── models/
├── services/
├── repositories/
├── utilities/
└── tests/
```

---

# 5. File Headers

Every source file must begin with a descriptive header.

---

## TypeScript

```typescript
/**
 * Dashboard Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides the Cortex dashboard.
 *
 * Features:
 * ---------
 * - Backend health
 * - Platform metrics
 * - Recent activity
 */
```

---

## HTML

```html
<!--
/**
 * Dashboard Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides the HTML template for the Cortex dashboard.
 *
 * Features:
 * ---------
 * - Dashboard layout
 * - Dashboard content
 */
-->
```

---

## SCSS

```scss
/**
 * Dashboard Component
 *
 * Author:
 * -------
 * Ranjoy Sen
 *
 * Purpose:
 * --------
 * Provides the styles for the Cortex dashboard.
 *
 * Features:
 * ---------
 * - Dashboard layout
 * - Dashboard styling
 */
```

---

## Python

```python
"""
Dataset Upload Component

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides dataset upload, validation,
preview and registration workflow.

Features:
---------
- Dataset type selection
- Excel upload
- Schema validation
- Dataset preview
- Dataset registration
"""
```

---

# 6. Import Organization

## Python

```python
# ==============================================================================
# Standard Library
# ==============================================================================

import os
import json

# ==============================================================================
# Third Party
# ==============================================================================

import pandas as pd

# ==============================================================================
# Project
# ==============================================================================

from app.services...
```

---

## TypeScript

```typescript
/*------------------------------------------------------------------------------
 * Angular
 *----------------------------------------------------------------------------*/

...

/*------------------------------------------------------------------------------
 * Third Party
 *----------------------------------------------------------------------------*/

...

/*------------------------------------------------------------------------------
 * Shared
 *----------------------------------------------------------------------------*/

...

/*------------------------------------------------------------------------------
 * Core
 *----------------------------------------------------------------------------*/

...

/*------------------------------------------------------------------------------
 * Feature
 *----------------------------------------------------------------------------*/

...
```

Imports should always be grouped and ordered.

---

# 7. Naming Conventions

## Components

```
DashboardComponent
StatusIndicatorComponent
TopbarComponent
```

---

## Services

```
ApiService
HealthService
DocumentService
ChatService
```

---

## Interfaces

```
HealthStatus
NavigationItem
DocumentSummary
```

Avoid prefixes such as:

```
IHealthStatus
IDocument
```

---

## Constants

```
NAVIGATION
DEFAULT_PAGE_SIZE
```

---

## Enums

```
StatusType
DocumentState
```

---

# 8. Angular Standards

## Components

Each component should contain:

```
component.ts
component.html
component.scss
component.spec.ts
```

---

Components should follow this structure:

- Dependencies
- Properties
- Constructor
- Lifecycle
- Public Methods
- Protected Methods
- Private Methods

---

Components should remain focused on presentation.

Business logic belongs in services.

---

# 9. Python Standards

Python classes should have a single responsibility.

Avoid large utility modules containing unrelated functions.

Prefer:

```
pdf_service.py

excel_service.py

validation_service.py
```

instead of

```
utils.py
```

---

Functions should be:

- Small
- Focused
- Testable

---

# 10. HTML Standards

HTML should contain presentation only.

Avoid business logic inside templates.

Avoid inline styles.

Prefer reusable components.

---

# 11. SCSS Standards

Every SCSS file should follow this order.

```
Header

Host

Layout

Components

States

Responsive
```

---

Avoid deeply nested selectors.

Prefer component-local styles.

---

# 12. Services

Services own business logic.

Components consume services.

Services should never depend on UI components.

---

# 13. Shared Components

A component should move into Shared only when:

- Used by multiple features

OR

- Represents an application-level concept

Examples:

- Sidebar
- Topbar
- Status Bar
- Status Indicator

---

# 14. Error Handling

Never silently ignore errors.

Display meaningful user messages.

Log unexpected errors.

---

# 15. Logging

Backend logging should use structured logging.

Avoid print statements.

Frontend logging should use a centralized logging service.

---

# 16. Git Standards

Commit messages follow Conventional Commits.

Examples:

```
feat(chat): add streaming responses

fix(api): handle timeout exception

refactor(layout): simplify page layout

docs: update coding standards
```

Every architectural milestone should be tagged.

Example:

```
v0.1.0
```

---

# 17. Documentation

Every public class should document:

- Purpose
- Responsibilities
- Features

Documentation should explain **why**, not simply **what**.

---

# 18. AI Assisted Development

AI-generated code must follow the same standards as manually written code.

Generated code should:

- Be production quality
- Follow naming conventions
- Include file headers
- Follow folder organization
- Include documentation
- Remain readable and maintainable

AI should assist engineering, not replace engineering judgement.

---

# 19. Engineering Philosophy

Cortex is designed for long-term maintainability.

Every contribution should make the codebase easier to understand.

When in doubt:

- Keep it simple.
- Keep it readable.
- Keep it maintainable.
- Build only what is needed today.
- Let abstractions emerge naturally.

Readable code is the highest form of documentation.