# Resilience Control Plane (RCP)

## Overview
The Resilience Control Plane (RCP) is a deterministic governance middleware designed to govern autonomous agentic AI workloads. It mitigates "reasoning drift" and runaway compute costs in high-stakes financial environments by shifting policy enforcement from the application layer to a hardened, infrastructure-level sidecar.

## Key Architecture
- **Deterministic Gating**: Policy-as-code (Rego/OPA) compiled to Wasm for sub-2ms evaluation.
- **Zero-Trust Identity**: Keyless architecture using Workload Identity Federation (WIF).
- **Fiscal SecOps**: Real-time token expenditure tracking with hard-limit circuit breakers.
- **Auditability**: Immutable decision lineage capturing reasoning chains and policy-version hashes for SOC2 compliance.

## Hardening Log (Post-Audit)
*The RCP architecture underwent an adversarial audit by a Principal Architect peer-review process (May 2026).*

- **Critical Hardening Completed:**
  - Migrated budget state from local in-process memory to an atomic, shared store (ADR-0005).
  - Implemented a formal "Fail-Closed" contract with pre-flight health checks to mitigate single-point-of-failure risks (ADR-0006).

- **Future Roadmap:**
  - Implementing WORM audit storage and SSRF network controls (Ref: Findings 2.1 & 1.2).

## Quick Start
```bash
# Deploy RCP infrastructure
cd infra/terraform
terraform init
terraform apply

## Documentation
- [Traceability Matrix](docs/adr/0000-traceability-matrix.md)
- [Architecture Decision Records](docs/adr/)
- [SRE Monitoring Dashboard](infra/monitoring/sre_dashboard.json)