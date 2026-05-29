# Stakeholder Communication Log
## Project: Resilience Control Plane (RCP)

### Thread: The CISO's "Blocker" (May 19, 2026)
**From:** Sarah Jenkins (CISO)  
**To:** Marcus Vance (CTO), Brian Lasky (Architect)  
**Subject:** RE: Settlement Agent Production Rollout

*Sarah:* "Brian, I've reviewed the design for the RCP. While the local sidecar/Wasm approach is technically sound, I'm concerned about the 'Fail-Open' risk. If the policy sidecar crashes, what prevents the agent from running 'unsupervised'?"

*Brian (Your response):* "Sarah, good catch. We’ve updated the design to 'Fail-Closed.' If the sidecar isn't responsive, the client library will throw a hard exception, and the Workload Identity token will be revoked immediately by the RCP service. I've documented this in ADR-0001 (Fail-Closed Topology). Can we review the test plan for this 'Fail-Closed' scenario on Thursday?"

*Sarah:* "If you can prove that in a load test, I'll clear the path for the staging environment."