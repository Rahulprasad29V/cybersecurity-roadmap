# Advanced Module: Detection Engineering

**Level:** Advanced · **Suggested effort:** 8–12 hours

## Outcomes
- Translate a threat hypothesis into observable telemetry requirements.
- Write vendor-neutral detection logic before implementing it in a SIEM.
- Build test cases for expected, benign and edge-case activity.
- Measure precision, false positives, data coverage and operational cost.
- Document triage and response guidance.

## Engineering lifecycle
1. **Hypothesis:** Define the behavior or risk to detect.
2. **Telemetry:** Identify required event sources, fields, time quality and retention.
3. **Logic:** Write the analytic in plain language, then translate to a platform-specific query.
4. **Testing:** Use synthetic or approved lab events, including benign counterexamples.
5. **Tuning:** Reduce noise without suppressing meaningful behavior.
6. **Operations:** Add severity rationale, owner, triage steps and review date.
7. **Retirement:** Disable obsolete logic and document the reason.

## Practical exercise
Use [the synthetic authentication dataset](../datasets/authentication-events.csv). Propose a detection for repeated authentication failures followed by a success. Define grouping, time window, threshold rationale and limitations. Avoid attributing activity to a person based on synthetic events.

## Required deliverable
- Detection specification.
- Data-source and field mapping.
- Test matrix with positive and benign cases.
- False-positive analysis.
- Triage runbook and version history.

## Quality metrics
Track true-positive rate where ground truth exists, false-positive volume, data-source coverage, time-to-triage and alert usefulness. Do not invent accuracy percentages from a tiny sample.

## References
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Sigma HQ](https://github.com/SigmaHQ/sigma)
- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
