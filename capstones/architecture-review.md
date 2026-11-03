# Capstone: Enterprise Architecture Security Review

**Level:** Advanced · **Suggested effort:** 12–18 hours

## Scenario
A fictional education company operates a learner portal, instructor console, content API, identity provider, payment integration and cloud object storage. Different user roles access different functions. The organization wants a security architecture review before a major release.

## Scope
This is a design-only exercise. Use the fictional architecture described here or create your own synthetic diagram. No real system testing is authorized or required.

## Work packages
1. Define system purpose, data types, users and business-critical assets.
2. Draw a context diagram and a logical data-flow diagram.
3. Mark trust boundaries and privileged operations.
4. Create abuse cases for account recovery, role changes, content publishing and file uploads.
5. Map threats to preventive, detective and recovery controls.
6. Evaluate logging, backup, access review and incident readiness.
7. Prioritize residual risks and document design decisions.

## Required outputs
- Architecture and data-flow diagrams.
- Asset and identity inventory.
- Threat register with assumptions and impact.
- Control matrix with owner and verification evidence.
- Three architecture decision records.
- Executive summary for a non-specialist audience.

## Acceptance criteria
- Each critical data flow has an identified trust boundary.
- Every privileged operation has an explicit authorization decision point.
- Risks include realistic impact and evidence requirements.
- Recommendations identify an owner, priority and validation method.
- Assumptions and out-of-scope areas are visible.

## Suggested reviewers
Security engineer, application owner, platform engineer and business risk owner.
