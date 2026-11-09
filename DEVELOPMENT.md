# Development

## Prerequisites

- Python 3.12+

## Testing

Test configuration lives in `pyproject.toml` (`pythonpath = ["scripts"]`), so from
the repo root:

```bash
pytest
```

Tests cover secret redaction, config collection, ZIP packaging, file exclusion, and
the API client's renewal-URL trust check. They run in CI on every push and pull
request (see `.github/workflows/test.yml`).

## Source of truth

This repository is the canonical source for `SKILL.md`, `scripts/`, and `tests/`.
It is archived: the skill is deprecated and version 2.0.0 is the final release.
Earlier releases were published to ClawHub from a mirror in Trent's monorepo;
that mirror has been removed. The 2.0.0 tombstone is published from this repo with
`clawhub publish`.
