# Resilience Control Plane (RCP)

The Resilience Control Plane (RCP) is a deterministic governance middleware designed to govern autonomous agentic AI workloads. It mitigates "reasoning drift" and runaway compute costs in high-stakes financial environments by shifting policy enforcement from the application layer to a hardened, infrastructure-level sidecar.

## 🛡️ Pre-Deployment Governance
RCP includes an automated **Security & Fiscal Gate** that runs in the CI/CD pipeline to ensure infrastructure compliance before provisioning.

### How it works:
1. **Terraform Plan Analysis**: Parses `main.tf` and `variables.tf` via `hcl2`.
2. **Policy-as-Code Evaluation**: Validates infrastructure against OPA (Open Policy Agent) policies written in Rego.
3. **Fail-Closed Enforcement**: Blocks non-compliant deployments (e.g., AI token runaway, insecure public bucket ACLs).

### Quick Start: Governance Audit
```bash
python3 infra/governance/auditor.py infra/terraform/main.tf

Key Architecture
Deterministic Gating: Policy-as-code (Rego/OPA) optimized for high-assurance evaluation.

Zero-Trust Identity: Keyless architecture using Workload Identity Federation (WIF).

Fiscal SecOps: Real-time token expenditure tracking with hard-limit circuit breakers.

Auditability: Immutable decision lineage capturing reasoning chains and policy-version hashes for SOC2 compliance.

🛠 Hardening Log (Post-Audit)
The RCP architecture underwent an adversarial audit by a Principal Architect peer-review process (May 2026).

Governance Gate Integration (June 2026): Shifted policy enforcement from reactive auditing to proactive, deterministic pre-deployment gates.

Budget State Management: Migrated budget state from local in-process memory to an atomic, shared store (ADR-0005).

Fail-Closed Contract: Implemented a formal contract with pre-flight health checks to mitigate single-point-of-failure risks (ADR-0006).

Future Roadmap
Implementing WORM audit storage and SSRF network controls (Ref: Findings 2.1 & 1.2).

📑 Documentation
Traceability Matrix

Architecture Decision Records

SRE Monitoring Dashboard