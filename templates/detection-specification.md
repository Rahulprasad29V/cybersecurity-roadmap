# Detection Specification Template

## Detection metadata
- Detection ID:
- Name:
- Owner:
- Version:
- Status: draft / test / production / retired
- Review date:

## Detection hypothesis
Describe the behavior or risk the analytic is intended to identify.

## Threat context
- Relevant business risk:
- ATT&CK mapping, if justified:
- Known limitations:

## Telemetry requirements
| Source | Required fields | Time standard | Coverage / gaps |
|---|---|---|---|
| | | | |

## Analytic logic
Write the logic in vendor-neutral language before translating it to a platform query.

## Test plan
| Test case | Expected alert? | Evidence | Result |
|---|---|---|---|
| Representative suspicious case | Yes | Synthetic or authorized event | |
| Benign counterexample | No / contextual | Synthetic or authorized event | |
| Missing telemetry | Unknown / no conclusion | Data-gap evidence | |

## Tuning and operations
- False-positive drivers:
- Suppression rationale and risk:
- Severity rationale:
- Triage instructions:
- Escalation criteria:
- Data retention requirements:
- Owner and review cadence:

## Metrics
Record only metrics that have a defined denominator and reliable ground truth. Include coverage, false-positive volume, analyst usefulness and known blind spots.

## Change history
| Date | Version | Change | Reviewer |
|---|---|---|---|
| | | | |
