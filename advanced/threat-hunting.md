# Advanced Module: Threat Hunting

**Level:** Advanced · **Suggested effort:** 6–10 hours

## Outcomes
- Form a testable hunt hypothesis from a risk or threat behavior.
- Identify required telemetry and its known blind spots.
- Perform structured analysis of synthetic or approved lab data.
- Document findings, confidence, alternative explanations and follow-up actions.

## Hunt workflow
1. Define the question and business context.
2. Map the hypothesis to behaviors and data sources.
3. Confirm data quality, coverage and time normalization.
4. Query only authorized telemetry.
5. Validate observations and test benign explanations.
6. Record findings and detection opportunities.
7. Close with coverage gaps and a repeatable query plan.

## Practical exercise
Use [the synthetic authentication events](../datasets/authentication-events.csv) and [asset inventory](../datasets/asset-inventory.csv). Explore unusual event sequences and discuss whether asset criticality changes investigation priority.

## Deliverable
A hunt brief containing hypothesis, scope, data sources, analysis, findings, confidence, limitations and recommended detection improvements.

## References
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CISA Joint Cyber Defense Collaborative](https://www.cisa.gov/jcdc)
- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
