# CyberWolf Synthetic Training Datasets

This directory contains small, fictional datasets for defensive learning, detection engineering, cloud review and risk prioritization.

## Dataset inventory
| File | Use | Safety |
|---|---|---|
| [authentication-events.csv](authentication-events.csv) | Log timeline and detection analysis | Synthetic users, reserved TEST-NET addresses |
| [asset-inventory.csv](asset-inventory.csv) | Asset criticality and ownership exercise | Fictional lab assets |
| [cloud-posture-findings.csv](cloud-posture-findings.csv) | Cloud configuration triage | Fictional resource identifiers |
| [identity-access-matrix.csv](identity-access-matrix.csv) | Entitlement review | Fictional roles and permissions |
| [vulnerability-backlog.csv](vulnerability-backlog.csv) | Risk-based remediation | Fictional findings and assets |

## Dataset handling
- These records are synthetic and must not be interpreted as real threat intelligence or production evidence.
- Reserved TEST-NET address ranges are used where IP-like values are helpful.
- Do not add real user data, credentials, tokens, private addresses or incident artifacts.
- Preserve source values and note any transformations in analysis.
- Do not infer identity, intent or compromise from a single record.

## Suggested exercises
- [Detection engineering](../advanced/detection-engineering.md)
- [Threat hunting](../advanced/threat-hunting.md)
- [Cloud posture capstone](../capstones/cloud-posture.md)
- [Incident response capstone](../capstones/incident-response.md)
