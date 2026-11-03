# CyberWolf Curriculum Catalog

The machine-readable curriculum manifest supports future content tooling while keeping the learning content readable as Markdown.

## Files
- [curriculum.json](curriculum.json) — module IDs, levels, prerequisites, learning outcomes and deliverables.
- [curriculum.schema.json](curriculum.schema.json) — JSON Schema contract for the manifest.
- [Advanced module index](../advanced/README.md) — detailed advanced content.
- [Advanced 30-day challenge](../advanced/30-day-challenge.md) — applied engineering sprint.

## Manifest contract
Every module should have:
- A stable, unique ID.
- A title and difficulty level.
- A repository-relative Markdown path.
- Estimated effort in hours.
- Prerequisites.
- Observable learning outcomes.
- A concrete deliverable.

## Versioning
Increment `format_version` only for breaking data-structure changes. Use the `edition` field for curriculum content releases. Preserve stable module IDs when improving the prose so downstream tools can continue to reference them.
