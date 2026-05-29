# Architectural Traceability Matrix: AFL Resilience Control Plane

| Business Problem (AFL) | Audit Finding (Claude) | ADR / Hardening |
| :--- | :--- | :--- |
| $250k Unauthorized Wire Transfer | 1.1 (SPOF) & 1.2 (Identity) | ADR-0001 (UDS IPC), ADR-0006 (Fail-Closed) |
| $4k Fiscal Token Loop | 1.3 (Circuit Breaker Race) | ADR-0005 (Atomic Fiscal State) |
| SOC2 Audit Failure | 2.1 (Audit Immutability) | ADR-0007 (WORM Storage Strategy) |
| Insider Threat / Policy Drift | 2.2 (Governance Access) | ADR-0008 (Signed Policy Bundles) |