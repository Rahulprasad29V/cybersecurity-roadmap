# Contributing to CyberWolf Cybersecurity Roadmap

Thank you for helping improve this learning resource. Contributions should be accurate, beginner-friendly, practical and safe.

## Ways to contribute
- Correct factual errors, spelling, broken links or unclear explanations.
- Add defensive examples, safe lab exercises, diagrams and study questions.
- Improve accessibility and navigation.
- Suggest projects with measurable outcomes.
- Add reputable, maintained learning resources.

## Requirements
1. Keep this edition in English.
2. Explain prerequisites and expected learning outcomes.
3. Cite authoritative documentation where appropriate.
4. Use harmless examples, synthetic data, local labs or explicitly authorized environments.
5. Never include real credentials, tokens, private keys, personal data or private target details.
6. Do not add instructions that enable unauthorized access, credential theft, stealth, destructive activity or data exfiltration.
7. Do not present scanner output as proof without validation and context.
8. Check resource links and respect source licenses.

## Pull request checklist
- [ ] The change has a clear learning purpose.
- [ ] Technical statements are accurate and sourced.
- [ ] Examples are safe and authorized.
- [ ] No secrets or personal information are included.
- [ ] Markdown headings and links render correctly.
- [ ] New exercises include expected outcomes or success criteria.

## Suggested workflow
Fork the repository, create a focused branch, make the change, preview Markdown, validate links where practical, and submit a pull request explaining the change and its validation.

By contributing, you agree that your contribution may be distributed under this repository's license.


## Automated repository checks
Every push to `main` and every pull request runs the repository quality workflow. It checks local Markdown links and confirms that the required roadmap and all 100 daily challenge files are present.

Run the same check locally before submitting a change:

```bash
python3 scripts/check_repo.py
```


## Structured learning content
- Store quizzes as JSON and follow [quiz.schema.json](quizzes/quiz.schema.json).
- Keep question IDs unique and stable; include a clear explanation and authoritative reference where useful.
- Add lab briefs using [lab-exercise-template.md](labs/lab-exercise-template.md).
- Keep CTF challenges self-contained, offline and safe; include the intended reasoning and learning takeaway.
- Achievements are manual learning milestones, not credentials or independently verified assessments.
- Keep personal progress in a local copy. Do not commit learner-identifying information.

## Automated checks
Pull requests run repository checks for local Markdown links, required 100-day challenge files, quiz structure, achievement identifiers and glossary data. Run locally:

```bash
python3 scripts/check_repo.py
python3 scripts/validate_learning_content.py
```
