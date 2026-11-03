# Challenge: Hash Detective

- **Level:** Beginner
- **Category:** Integrity
- **Estimated effort:** 10–15 minutes

## Scenario
A fictional release note says the trusted SHA-256 digest for a training file is:

`a1`

The two sample files are described as:
- Sample A: digest `a1`
- Sample B: digest `b2`

## Objective
Which sample matches the supplied trusted digest?

## Hints
1. Compare the values exactly.
2. A matching digest is evidence of matching content under the assumed hash algorithm; it is not proof of publisher identity by itself.

## Solution
Sample A matches the provided digest.

Flag: `CYBERWOLF{sample_a}`

## Lesson
Real SHA-256 digests are 64 hexadecimal characters. The short values in this puzzle are illustrative placeholders, not real verification data.
