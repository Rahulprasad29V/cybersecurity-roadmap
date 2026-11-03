# Advanced Module: Cloud-Native Security

**Level:** Advanced · **Suggested effort:** 8–12 hours

## Outcomes
- Model identity and network boundaries in cloud-native systems.
- Evaluate workload identity, container supply chain and runtime controls.
- Review Kubernetes authorization, secrets, admission and network policies.
- Prioritize cloud posture findings using exposure, impact and compensating controls.

## Core topics
1. Shared responsibility, account structure and landing-zone principles.
2. Human, workload and service identity.
3. Private networking, ingress/egress, segmentation and service communication.
4. Container image provenance, minimal images and runtime permissions.
5. Kubernetes RBAC, secrets, admission controls and network policies.
6. Cloud audit logging, detection and incident readiness.
7. Infrastructure-as-code review and drift management.

## Practical exercise
Use a sample architecture or a sandbox account that you control. Review the fictional configuration records in [cloud-posture-findings.csv](../datasets/cloud-posture-findings.csv). Identify excessive permission, public exposure and missing telemetry. Do not create resources without understanding billing and cleanup.

## Deliverable
- Cloud-native context diagram.
- IAM and network review.
- Prioritized findings with evidence and limitations.
- Remediation plan and validation steps.

## References
- [CISA Cloud Security Technical Reference Architecture](https://www.cisa.gov/resources-tools/resources/cloud-security-technical-reference-architecture)
- [Kubernetes Security](https://kubernetes.io/docs/concepts/security/)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
