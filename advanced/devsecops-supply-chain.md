# Advanced Module: DevSecOps and Software Supply Chain Security

**Level:** Advanced · **Suggested effort:** 8–12 hours

## Outcomes
- Map the software delivery pipeline and its trust relationships.
- Identify risks in source control, build systems, dependencies, artifacts and deployment.
- Design proportionate controls for secrets, dependencies, provenance and release integrity.
- Integrate security checks without treating a green pipeline as proof of secure software.

## Core topics
1. Secure SDLC and threat modeling for build and release systems.
2. Dependency inventories, vulnerability triage and update policy.
3. Secret detection, rotation and least-privilege CI identities.
4. Build isolation, protected branches and review controls.
5. Artifact integrity, attestations, provenance and SBOM concepts.
6. Container image lifecycle and deployment policy.
7. Exceptions, compensating controls and audit evidence.

## Practical exercise
Use a demo repository with no production credentials. Create a pipeline control map covering source, build, artifact and deploy stages. Review a sample dependency manifest and document how you would prioritize fixes.

## Deliverable
- Software supply-chain threat model.
- CI/CD control matrix.
- Dependency review and exception workflow.
- Evidence checklist for a release.
- Residual-risk statement.

## References
- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP Software Component Verification Standard](https://owasp.org/www-project-software-component-verification-standard/)
- [SLSA](https://slsa.dev/)
