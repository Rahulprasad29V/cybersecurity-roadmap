# Lab: Synthetic Authentication Log Triage

**Level:** Beginner · **Effort:** 45–60 minutes

## Objective
Build a timeline from synthetic authentication records and write a cautious triage note.

## Dataset
Create a small CSV with fictional timestamps, fictional user IDs, source labels such as `LAB-NET-A`, event types, outcomes and device labels. Do not use real personal or account data.

## Activity
1. Check timestamp format and time zone assumptions.
2. Group events by fictional account and time window.
3. Identify unusual patterns such as repeated failures followed by a success.
4. List benign explanations that should be checked.
5. Recommend proportionate next steps for the fictional system owner.

## Evidence
- Sanitized timeline.
- Triage note with observations, hypotheses, confidence and information gaps.
- One possible detection idea and its false-positive risks.

## Success criteria
Do not claim compromise or attribution from a single pattern. Distinguish facts from assumptions.
