# Capstone: Detection Engineering Program

**Level:** Advanced · **Suggested effort:** 12–18 hours

## Scenario
A fictional SaaS organization wants to improve identity and endpoint monitoring. It has synthetic authentication logs, endpoint event summaries and an inventory of business-critical assets.

## Scope
Use only the synthetic datasets in [datasets](../datasets/README.md). Do not connect to real identity providers, endpoints or production SIEMs.

## Work packages
1. Define detection priorities from business and threat context.
2. Map required fields, event sources, time zones and data-quality assumptions.
3. Write three detection specifications in platform-neutral language.
4. Build test matrices with expected-positive and benign counterexamples.
5. Evaluate coverage gaps, false-positive drivers and operational cost.
6. Write analyst triage instructions and escalation criteria.
7. Propose a review cadence and retirement process.

## Required outputs
- Detection priority matrix.
- Three analytic specifications.
- Telemetry source/field map.
- Synthetic test cases.
- Triage runbooks.
- Measurement plan and limitations.

## Acceptance criteria
A reviewer can understand why each detection exists, what evidence triggers it, what benign activity may look similar, and what the analyst should do next.
