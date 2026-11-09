#!/usr/bin/env python3
# Copyright 2025-2026 Trent AI
# SPDX-License-Identifier: Apache-2.0

"""Publish the trentclaw skill to ClawHub.

Stages only SKILL.md, scripts/openclaw_trent/, LICENSE and NOTICE into a temp
directory and publishes that. Tests, tools and docs are never sent.

Usage:
    python tools/publish_to_clawhub.py --dry-run    # preview the bundle
    python tools/publish_to_clawhub.py              # publish

Prerequisites:
    npm i -g clawhub
    clawhub login        # as the skill owner, trent-ai-release
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_SRC = REPO_ROOT / "SKILL.md"
SCRIPTS_SRC = REPO_ROOT / "scripts"
LICENSE_FILES = ("LICENSE", "NOTICE")

SLUG = "trentclaw"
DISPLAY_NAME = "Trent OpenClaw Security Assessment"
TAGS = "latest,trentai,trent,trentclaw,security,assessment,threat-modeling,deprecated"

SKIP = {"__pycache__", ".pytest_cache", ".ruff_cache"}


def _copy_scripts(dest: Path) -> int:
    count = 0
    for src_file in SCRIPTS_SRC.rglob("*"):
        if not src_file.is_file() or src_file.suffix == ".pyc":
            continue
        rel = src_file.relative_to(SCRIPTS_SRC)
        if any(part in SKIP or part.startswith(".") for part in rel.parts):
            continue
        target = dest / "scripts" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, target)
        count += 1
    return count


def _read_version() -> str:
    for line in SKILL_SRC.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("version:"):
            return stripped.split(":", 1)[1].strip()
    print("Error: no version: field in SKILL.md frontmatter", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish the trentclaw skill to ClawHub.")
    parser.add_argument("--dry-run", action="store_true", help="Preview the bundle only")
    parser.add_argument("--changelog", default="", help="Changelog text for this version")
    args = parser.parse_args()

    for required in (SKILL_SRC, SCRIPTS_SRC, *(REPO_ROOT / f for f in LICENSE_FILES)):
        if not required.exists():
            print(f"Error: {required} not found", file=sys.stderr)
            sys.exit(1)

    clawhub_bin = shutil.which("clawhub")
    if not clawhub_bin and not args.dry_run:
        print("Error: clawhub CLI not found. Install: npm i -g clawhub", file=sys.stderr)
        sys.exit(1)

    version = _read_version()

    with tempfile.TemporaryDirectory(prefix="trent-skill-") as tmp_dir:
        staging = Path(tmp_dir)
        shutil.copy2(SKILL_SRC, staging / "SKILL.md")
        file_count = _copy_scripts(staging)
        for lic_name in LICENSE_FILES:
            shutil.copy2(REPO_ROOT / lic_name, staging / lic_name)

        print(f"Publishing {SLUG} v{version} to ClawHub")
        print(f"  SKILL.md:  {SKILL_SRC}")
        print(f"  scripts/:  {SCRIPTS_SRC} ({file_count} files)")
        print(f"  license:   {', '.join(LICENSE_FILES)}")
        print(f"  tags:      {TAGS}\n")

        if args.dry_run:
            print("Dry run. Bundle contents:\n")
            for f in sorted(staging.rglob("*")):
                if f.is_file():
                    print(f"  {f.relative_to(staging)}  ({f.stat().st_size:,} bytes)")
            return

        cmd = [
            clawhub_bin,
            "publish",
            str(staging),
            "--slug",
            SLUG,
            "--version",
            version,
            "--name",
            DISPLAY_NAME,
            "--tags",
            TAGS,
        ]
        if args.changelog:
            cmd += ["--changelog", args.changelog]

        result = subprocess.run(cmd, capture_output=False)
        if result.returncode != 0:
            print("\nPublish failed. Check login with: clawhub whoami", file=sys.stderr)
            sys.exit(result.returncode)

        print(f"\nPublished {SLUG} v{version}.")


if __name__ == "__main__":
    main()
