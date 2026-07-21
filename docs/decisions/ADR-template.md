# ADR-XXX: <Decision Title>

## Status

- Proposed
- Accepted
- Superseded
- Deprecated

Current Status:

Accepted

---

## Context

Describe the architectural problem that exists.

Answer questions such as:

- What problem are we trying to solve?
- Why does this matter?
- What constraints exist?
- What business or technical drivers influenced the decision?
- Why can't we continue with the current approach?

This section should explain **why** the decision is necessary.

---

## Decision

Describe the architectural decision.

Clearly state:

- What has been decided
- What will be adopted
- What will no longer be used
- Scope of the decision

This should be concise and unambiguous.

---

## Architecture

Illustrate the high-level architecture after the decision.

Example:

```text
Client
   │
   ▼
API
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
```

Multiple diagrams may be included if helpful.

---

## Responsibilities

Clearly define responsibilities for each major component.

### Component A

Responsible for:

- ...

Not responsible for:

- ...

---

### Component B

Responsible for:

- ...

Not responsible for:

- ...

Repeat for each architectural component.

---

## Design Principles

Describe the architectural principles established by this decision.

Examples:

### Separation of Concerns

...

---

### Provider Independence

...

---

### Scalability

...

---

### Security

...

---

### Extensibility

...

Only include principles relevant to this ADR.

---

## Consequences

### Positive

- ...
- ...
- ...

### Negative

- ...
- ...
- ...

Every architectural decision introduces trade-offs.

Document both.

---

## Alternatives Considered

Describe realistic alternatives that were evaluated.

### Alternative 1

Pros

- ...

Cons

- ...

---

### Alternative 2

Pros

- ...

Cons

- ...

Explain why they were not selected.

---

## Future Considerations

Describe expected future evolution.

Examples:

- Scalability
- Multi-region deployment
- Provider replacement
- Performance improvements
- Additional integrations

Avoid implementation details.

Focus on architectural direction.

---

## Related Decisions

Reference earlier ADRs that influence or depend on this decision.

Example

- ADR-012
- ADR-018
- ADR-021

---

## Outcome

Summarize the long-term impact.

Answer:

"What does Cortex gain after this decision?"

Example:

```text
Before

Client
   │
   ▼
Database

After

Client
   │
   ▼
API
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
```

Finish with a short paragraph explaining how this decision advances the overall Cortex architecture.