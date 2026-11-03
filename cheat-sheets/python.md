# Python Quick Reference

## Safe scripting habits
- Use a virtual environment for project dependencies.
- Pin and review dependencies for reproducibility.
- Validate inputs and handle expected exceptions.
- Use `pathlib` for filesystem paths.
- Use `with` blocks for files.
- Do not hard-code credentials; use an approved secret manager or environment configuration.
- Avoid unsafe deserialization of untrusted data.
- Add tests for normal, boundary and invalid input.

## Common patterns
```python
from pathlib import Path
import json

path = Path("sample.json")

try:
    data = json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    raise SystemExit(f"File not found: {path}")
except json.JSONDecodeError as exc:
    raise SystemExit(f"Invalid JSON: {exc}")

if not isinstance(data, dict):
    raise SystemExit("Expected a JSON object")

print("Top-level keys:", ", ".join(sorted(data.keys())))
```

## Useful standard library modules
- `pathlib`: paths and files
- `json`: JSON parsing and serialization
- `csv`: CSV reading and writing
- `hashlib`: hash functions
- `logging`: application logging
- `argparse`: command-line argument parsing
- `unittest`: basic test framework
