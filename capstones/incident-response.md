# Capstone: Enterprise Incident Response Tabletop

**Level:** Advanced · **Suggested effort:** 8–12 hours

## Scenario
A fictional organization reports unusual sign-in patterns, a service account with unexpected activity and a disruption to one non-critical internal service. The exercise is designed for discussion; there is no executable malware or live system action.

## Scope
Tabletop only. Use the synthetic data in [datasets](../datasets/README.md). No containment action is performed against a real system.

## Exercise injects
1. **Initial report:** synthetic authentication events show repeated failures followed by a successful session.
2. **New context:** the account belongs to a service owner whose normal schedule differs from the event timestamps.
3. **Business impact:** one internal service reports intermittent errors.
4. **Evidence question:** timestamps in two source files use different time zones.
5. **Recovery question:** the business owner asks whether the service can be restored from a known backup.

## Work packages
- Establish incident roles and decision authority.
- Build a timeline while preserving original timestamps.
- Record facts, hypotheses and evidence gaps separately.
- Evaluate containment choices and operational trade-offs.
- Prepare stakeholder updates and escalation decisions.
- Define recovery validation and communications.
- Run a post-incident review with assigned corrective actions.

## Required outputs
- Incident action plan.
- Timeline and evidence log.
- Decision log with rationale.
- Situation report for leadership.
- Recovery checklist.
- Lessons-learned register.

## Acceptance criteria
The team communicates clearly, preserves evidence, avoids unsupported attribution, considers privacy and business continuity, and assigns measurable follow-up actions.
