#!/usr/bin/env python3
"""
ESC Skills — Manifest Manager
Manages versioning, hashing, and integrity of all skills in the repository.

Usage:
    python3 scripts/update_manifest.py --init          # Generate manifest.json from scratch
    python3 scripts/update_manifest.py --verify        # Verify all hashes and headers
    python3 scripts/update_manifest.py --bump <skill> <MAJOR|MINOR|PATCH>  # Bump version
    python3 scripts/update_manifest.py --add-headers   # Add version/updated to all SKILL.md frontmatter
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

# Legacy HTML comment pattern (for backward compat during migration)
LEGACY_HEADER_PATTERN = re.compile(
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


def parse_yaml_frontmatter(filepath: Path) -> dict | None:
    """Parse version/updated from YAML frontmatter in a SKILL.md file.

    Supports both new format (version inside YAML frontmatter) and
    legacy format (HTML comment on line 1) for backward compatibility.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")

    # Check for legacy HTML comment format first (line 1)
    if lines and LEGACY_HEADER_PATTERN.match(lines[0]):
        match = LEGACY_HEADER_PATTERN.match(lines[0])
        return match.groupdict()

    # New format: YAML frontmatter with version: and updated: fields
    if not lines or lines[0].strip() != "---":
        return None

    # Find the closing ---
    closing_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_idx = i
            break

    if closing_idx is None:
        return None

    # Parse frontmatter fields
    frontmatter_lines = lines[1:closing_idx]
    result = {}

    for line in frontmatter_lines:
        # Match key: value (simple single-line YAML parsing)
        m = re.match(r'^(\w+):\s*"?([^"]*?)"?\s*$', line)
        if m:
            key, value = m.group(1), m.group(2)
            if key == "name":
                result["name"] = value
            elif key == "version":
                result["version"] = value
            elif key == "updated":
                result["date"] = value

    if "version" in result:
        return result
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


def update_frontmatter_field(filepath: Path, field: str, value: str):
    """Update a field in the YAML frontmatter, or insert it before closing ---."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Ensure file starts with ---
    if not lines or lines[0].strip() != "---":
        return False

    # Find closing ---
    closing_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_idx = i
            break

    if closing_idx is None:
        return False

    # Check if field already exists in frontmatter
    field_pattern = re.compile(rf'^{field}:\s')
    field_idx = None
    for i in range(1, closing_idx):
        if field_pattern.match(lines[i]):
            field_idx = i
            break

    new_line = f'{field}: "{value}"\n'

    if field_idx is not None:
        # Replace existing field
        lines[field_idx] = new_line
    else:
        # Insert before closing ---
        lines.insert(closing_idx, new_line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)

    return True


def update_header(filepath: Path, name: str, version: str, updated: str, status: str | None = None):
    """Update version and updated fields in YAML frontmatter.

    Handles both new format (YAML frontmatter) and legacy format (HTML comment).
    If file has legacy format, migrates to new format.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")

    # If file starts with legacy HTML comment, migrate it
    if lines and LEGACY_HEADER_PATTERN.match(lines[0]):
        # Remove the HTML comment line
        lines = lines[1:]
        content = "\n".join(lines)

        # If there's no frontmatter after removing comment, add one
        if not lines or lines[0].strip() != "---":
            lines.insert(0, "---")
            lines.insert(1, f'name: {name}')
            lines.insert(2, f'version: "{version}"')
            lines.insert(3, f'updated: "{updated}"')
            lines.insert(4, "---")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            return

        # Write the file without the HTML comment first
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # Now update fields in YAML frontmatter
    update_frontmatter_field(filepath, "version", version)
    update_frontmatter_field(filepath, "updated", updated)


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
        header = parse_yaml_frontmatter(skill_md)
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

        # Check header (supports both YAML frontmatter and legacy HTML comment)
        header = parse_yaml_frontmatter(skill_md)
        if not header:
            errors.append(f"❌ Missing version in frontmatter: {name}")
        elif header["version"] != entry["version"]:
            errors.append(f"❌ Version mismatch: {name} (frontmatter: {header['version']}, manifest: {entry['version']})")

    if errors:
        print(f"\n{'='*60}")
        print(f"VERIFICATION FAILED — {len(errors)} issue(s):\n")
        for e in errors:
            print(f"  {e}")
        print(f"\n{'='*60}")
        return 1
    else:
        print(f"✅ All {len(skills)} skills verified — hashes match, versions present")
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

    # Update SKILL.md frontmatter
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
    """Add version/updated fields to all SKILL.md frontmatter that don't have them."""
    skills = get_all_skills()
    added = 0
    skipped = 0

    for name, skill_md in skills:
        header = parse_yaml_frontmatter(skill_md)
        if header and "version" in header:
            skipped += 1
            continue

        # Add version and updated to frontmatter
        update_header(skill_md, name, "1.0.0", TODAY)
        added += 1
        print(f"  + {name}")

    print(f"\n✅ Headers added: {added} | Already had version: {skipped}")
    return 0


# ─── CLI ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="ESC Skills Manifest Manager")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="Generate manifest.json from all skills")
    group.add_argument("--verify", action="store_true", help="Verify manifest integrity")
    group.add_argument("--bump", nargs=2, metavar=("SKILL", "TYPE"), help="Bump version (MAJOR/MINOR/PATCH)")
    group.add_argument("--add-headers", action="store_true", help="Add version/updated to all SKILL.md frontmatter")

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
