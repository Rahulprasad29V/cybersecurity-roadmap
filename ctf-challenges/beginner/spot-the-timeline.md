# Challenge: Spot the Timeline

- **Level:** Beginner
- **Category:** Log Analysis
- **Estimated effort:** 15–20 minutes

## Scenario
A fictional training service records the following events in UTC:

```text
2026-01-12T10:03:00Z LAB-USER-7 login_failed
2026-01-12T10:05:00Z LAB-USER-2 login_success
2026-01-12T10:04:00Z LAB-USER-7 login_failed
2026-01-12T10:08:00Z LAB-USER-7 password_reset_requested
```

## Objective
Put the records in chronological order and identify the account with repeated failures.

## Hints
1. Compare timestamps, not line order.
2. Keep account identifiers separate.

## Solution
Chronological order is 10:03, 10:04, 10:05, 10:08 UTC. The repeated failures belong to fictional account `LAB-USER-7`.

Flag: `CYBERWOLF{sort_by_timestamp}`

## Lesson
Log files may be aggregated from different systems. Normalize time zones and preserve the original records before drawing conclusions.
