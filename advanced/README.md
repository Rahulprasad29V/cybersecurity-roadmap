# CyberWolf Advanced Security Curriculum

This curriculum is for learners who already understand networking, operating systems, scripting and security fundamentals. It focuses on architecture decisions, defensive engineering, measurable control effectiveness and evidence-based risk management.

## Entry requirements
- Explain TCP/IP, DNS, HTTP/S and common operating-system concepts.
- Work comfortably in Linux and Windows lab environments.
- Read and write basic Python or another scripting language.
- Explain authentication, authorization, cryptography and the security risk lifecycle.
- Produce a clear lab report with scope, evidence and limitations.

## Advanced modules

| Module | Focus | Practical outcome |
|---|---|---|
| [Security architecture and threat modeling](security-architecture.md) | Trust boundaries, abuse cases, design reviews | Architecture threat model |
| [Detection engineering](detection-engineering.md) | Telemetry, hypotheses, tests and tuning | Tested detection specification |
| [DevSecOps and software supply chain](devsecops-supply-chain.md) | CI/CD trust, dependencies, provenance and secrets | Secure delivery control plan |
| [Cloud-native security](cloud-native-security.md) | Workload identity, containers, Kubernetes and cloud posture | Cloud-native review |
| [Enterprise identity security](enterprise-identity.md) | Federation, privileged access and lifecycle | Identity control assessment |
| [Threat hunting](threat-hunting.md) | Hypothesis-driven investigation and telemetry gaps | Hunt report |
| [Vulnerability management](vulnerability-management.md) | Exposure, prioritization, remediation and validation | Risk-based remediation plan |
| [Incident command and resilience](incident-command.md) | Decision-making, communications and recovery | Incident command tabletop |

## Advanced learning method
For each module:
1. Read the learning outcomes and primary references.
2. Define an approved lab or use the synthetic datasets in [datasets](../datasets/README.md).
3. Record hypotheses and expected evidence before testing.
4. Conduct the activity without exceeding its scope.
5. Evaluate false positives, blind spots and operational impact.
6. Produce a reviewed artifact using the [assessment rubrics](../assessments/README.md).

## Recommended capstones
See [Advanced capstones](../capstones/README.md). Select one primary capstone and complete the technical report, evidence pack and oral-defense checklist.

**Important:** Advanced learning does not require testing live third-party targets. These modules prioritize defensive engineering, safe validation and controlled training environments.
