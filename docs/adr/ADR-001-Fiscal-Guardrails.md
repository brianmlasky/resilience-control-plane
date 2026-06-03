# ADR-001: Implementing Fiscal Guardrails via Variable Validation

## Context
Our infrastructure must balance high availability with strict cost control. We evaluated using dynamic auto-scaling policies to manage compute costs versus enforcing deployment-time constraints.

## Decision
We chose to implement **variable validation** within our Terraform modules to enforce resource size constraints, rather than relying on dynamic auto-scaling logic.

## Consequences
- **Pros:** Eliminates the risk of "runaway" instance costs by failing the CI/CD pipeline if non-compliant sizes are requested; requires zero runtime overhead.
- **Cons:** Less flexible than dynamic scaling; developers must update module inputs to request larger instances.

## Status
Accepted
