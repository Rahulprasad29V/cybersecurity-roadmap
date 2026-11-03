# CyberWolf Quiz Bank

The quiz bank uses versioned JSON files so questions can be reviewed, reused and later imported into a learning application.

## Available quizzes
| Quiz | Level | Topics | File |
|---|---|---|---|
| Foundations Check | Beginner | Networking, operating systems, security principles | [foundations.json](foundations.json) |
| Web Security Check | Beginner / Intermediate | HTTP, access control, secure coding | [web-security.json](web-security.json) |
| Blue Team Check | Beginner / Intermediate | Logs, triage, incident response | [blue-team.json](blue-team.json) |

## Question format
Each question has a stable ID, prompt, topic, difficulty, answer options, a correct option ID and an explanation. The correct answer is intentionally present in the source JSON: these are public self-study resources, not a secure exam system.

## Study workflow
1. Attempt each question before reading its options or explanation.
2. Record uncertain topics.
3. Review the linked guide.
4. Repeat the quiz after practice.
5. Track progress locally; do not publish personal assessment data without consent.

## Maintainer guidance
Validate files against [quiz.schema.json](quiz.schema.json). Questions should test understanding, not tool memorization. Include only one unambiguous correct option unless a future schema explicitly supports multi-select questions.
