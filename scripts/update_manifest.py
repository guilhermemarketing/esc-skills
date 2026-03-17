#!/usr/bin/env python3
"""
ESC Skills — Manifest Manager
Manages versioning, hashing, and integrity of all skills in the repository.

Usage:
    python3 scripts/update_manifest.py --init          # Generate manifest.json from scratch
    python3 scripts/update_manifest.py --verify        # Verify all hashes and headers
    python3 scripts/update_manifest.py --bump <skill> <MAJOR|MINOR|PATCH>  # Bump version
    python3 scripts/update_manifest.py --add-headers   # Add version headers to all SKILL.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

# Resolve paths relative to the repo root (parent of scripts/)
REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
MANIFEST_PATH = REPO_ROOT / "manifest.json"

TODAY = date.today().isoformat()

HEADER_PATTERN = re.compile(
    r"^<!--\s*skill:\s*(?P<name>[^\|]+?)\s*\|\s*version:\s*(?P<version>\d+\.\d+\.\d+)\s*\|\s*updated:\s*(?P<date>\d{4}-\d{2}-\d{2})(?:\s*\|\s*status:\s*(?P<status>\w+))?\s*-->"
)


def sha256_file(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def get_all_skills() -> list[tuple[str, Path]]:
    """Return sorted list of (skill_name, skill_md_path) tuples."""
    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("."):
            continue
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            skills.append((skill_dir.name, skill_md))
    return skills


def parse_header(filepath: Path) -> dict | None:
    """Parse the version header from a SKILL.md file."""
    with open(filepath, "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
    match = HEADER_PATTERN.match(first_line)
    if match:
        return match.groupdict()
    return None


def bump_version(current: str, bump_type: str) -> str:
    """Apply semantic version bump."""
    major, minor, patch = map(int, current.split("."))
    if bump_type == "MAJOR":
        return f"{major + 1}.0.0"
    elif bump_type == "MINOR":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "PATCH":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid bump type: {bump_type}. Use MAJOR, MINOR, or PATCH.")


def update_header(filepath: Path, name: str, version: str, updated: str, status: str | None = None):
    """Update or insert the version header in a SKILL.md file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    status_part = f" | status: {status}" if status else ""
    new_header = f"<!-- skill: {name} | version: {version} | updated: {updated}{status_part} -->"

    lines = content.split("\n")
    if HEADER_PATTERN.match(lines[0]):
        lines[0] = new_header
    else:
        lines.insert(0, new_header)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ─── Commands ───────────────────────────────────────────────────────────

def cmd_init():
    """Generate manifest.json from all skills."""
    skills = get_all_skills()
    manifest = {
        "manifest_version": "1.0",
        "updated_at": TODAY,
        "skills": {}
    }

    for name, skill_md in skills:
        header = parse_header(skill_md)
        version = header["version"] if header else "1.0.0"

        manifest["skills"][name] = {
            "version": version,
            "path": f"skills/{name}/SKILL.md",
            "hash": sha256_file(skill_md),
            "breaking": False
        }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"✅ manifest.json generated with {len(skills)} skills")
    return 0


def cmd_verify():
    """Verify manifest integrity: hashes and headers."""
    if not MANIFEST_PATH.exists():
        print("❌ manifest.json not found. Run --init first.")
        return 1

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    errors = []
    skills = get_all_skills()
    skill_names_on_disk = {name for name, _ in skills}
    skill_names_in_manifest = set(manifest["skills"].keys())

    # Check for missing/extra entries
    missing = skill_names_on_disk - skill_names_in_manifest
    extra = skill_names_in_manifest - skill_names_on_disk
    for name in sorted(missing):
        errors.append(f"⚠️  Skill '{name}' exists on disk but NOT in manifest")
    for name in sorted(extra):
        errors.append(f"⚠️  Skill '{name}' in manifest but NOT on disk")

    # Verify each skill
    for name, skill_md in skills:
        entry = manifest["skills"].get(name)
        if not entry:
            continue

        # Check hash
        actual_hash = sha256_file(skill_md)
        if actual_hash != entry["hash"]:
            errors.append(f"❌ Hash mismatch: {name} (manifest: {entry['hash'][:12]}... actual: {actual_hash[:12]}...)")

        # Check header
        header = parse_header(skill_md)
        if not header:
            errors.append(f"❌ Missing version header: {name}")
        elif header["version"] != entry["version"]:
            errors.append(f"❌ Version mismatch: {name} (header: {header['version']}, manifest: {entry['version']})")

    if errors:
        print(f"\n{'='*60}")
        print(f"VERIFICATION FAILED — {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  {e}")
        print(f"\n{'='*60}")
        return 1
    else:
        print(f"✅ All {len(skills)} skills verified — hashes match, headers present")
        return 0


def cmd_bump(skill_name: str, bump_type: str):
    """Bump version for a specific skill."""
    bump_type = bump_type.upper()
    if bump_type not in ("MAJOR", "MINOR", "PATCH"):
        print(f"❌ Invalid bump type: {bump_type}. Use MAJOR, MINOR, or PATCH.")
        return 1

    skill_md = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Skill not found: {skill_name}")
        return 1

    if not MANIFEST_PATH.exists():
        print("❌ manifest.json not found. Run --init first.")
        return 1

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    entry = manifest["skills"].get(skill_name)
    if not entry:
        print(f"❌ Skill '{skill_name}' not found in manifest. Run --init.")
        return 1

    old_version = entry["version"]
    new_version = bump_version(old_version, bump_type)

    # Update SKILL.md header
    update_header(skill_md, skill_name, new_version, TODAY)

    # Update manifest
    new_hash = sha256_file(skill_md)
    entry["version"] = new_version
    entry["hash"] = new_hash
    entry["breaking"] = bump_type == "MAJOR"
    manifest["updated_at"] = TODAY

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"✅ {skill_name}: {old_version} → {new_version} ({bump_type})")
    if bump_type == "MAJOR":
        print(f"⚠️  Breaking change flagged — update CHANGELOG.md")
    return 0


def cmd_add_headers():
    """Add version headers to all SKILL.md files that don't have one."""
    skills = get_all_skills()
    added = 0
    skipped = 0

    for name, skill_md in skills:
        header = parse_header(skill_md)
        if header:
            skipped += 1
            continue

        update_header(skill_md, name, "1.0.0", TODAY)
        added += 1
        print(f"  + {name}")

    print(f"\n✅ Headers added: {added} | Already had header: {skipped}")
    return 0


# ─── CLI ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="ESC Skills Manifest Manager")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="Generate manifest.json from all skills")
    group.add_argument("--verify", action="store_true", help="Verify manifest integrity")
    group.add_argument("--bump", nargs=2, metavar=("SKILL", "TYPE"), help="Bump version (MAJOR/MINOR/PATCH)")
    group.add_argument("--add-headers", action="store_true", help="Add version headers to all SKILL.md")

    args = parser.parse_args()

    if args.init:
        return cmd_init()
    elif args.verify:
        return cmd_verify()
    elif args.bump:
        return cmd_bump(args.bump[0], args.bump[1])
    elif args.add_headers:
        return cmd_add_headers()


if __name__ == "__main__":
    sys.exit(main() or 0)
