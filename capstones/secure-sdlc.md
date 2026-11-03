# Capstone: Secure SDLC Transformation

**Level:** Advanced · **Suggested effort:** 12–18 hours

## Scenario
A fictional software team ships a web application through a source-control repository and automated CI/CD pipeline. Security checks are inconsistent and dependency ownership is unclear.

## Scope
Create a proposed delivery process using a demo repository and sample manifests only. Do not use production credentials or change a real organization's pipeline.

## Work packages
1. Map source, build, test, artifact and deployment stages.
2. Threat-model identities, secrets, runners, dependencies and release artifacts.
3. Define code review and branch protection expectations.
4. Design dependency inventory, vulnerability triage and exception expiry.
5. Specify secret detection and rotation responsibilities.
6. Define artifact integrity, provenance and release evidence requirements.
7. Create a developer-friendly remediation and escalation workflow.

## Required outputs
- Pipeline architecture.
- Software supply-chain threat model.
- Control matrix by pipeline stage.
- Example policy and exception record.
- Release evidence checklist.
- Adoption plan with measurable objectives.

## Acceptance criteria
Controls are assigned to owners, proportionate to risk, testable and designed to avoid leaking secrets or blocking releases without a documented exception path.
