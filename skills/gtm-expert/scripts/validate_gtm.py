#!/usr/bin/env python3
"""Validate a GTM container JSON file before import.

Usage: python3 validate_gtm.py <path_to_json>

Checks:
  1. JSON validity
  2. Encoding (no raw non-ASCII bytes)
  3. Unique IDs per object type
  4. Trigger references from tags exist
  5. Folder references exist
  6. ES5 compliance in Custom HTML tags
  7. Variable reference integrity
"""

import json
import re
import sys


def verify_es5(html_value, tag_name):
    """Check for ES6+ features in a Custom HTML tag value."""
    js = html_value.replace('<script>', '').replace('</script>', '')
    issues = []
    checks = {
        'const declaration': (r'\bconst\b', js),
        'let declaration': (r'\blet\b', js),
        'arrow function (=>)': (r'=>', js),
        'template literal (`)': (r'`', js),
        'Object.entries': (r'Object\.entries', js),
        'Object.values': (r'Object\.values', js),
        'optional chaining (?.)': (r'\?\.\w', js),
        'nullish coalescing (??)': (r'\?\?', js),
        'class declaration': (r'\bclass\s+\w', js),
        'async/await': (r'\basync\b|\bawait\b', js),
        'spread in array ([...])': (r'\[\.\.\.', js),
        'spread in object ({...})': (r'\{\.\.\.', js),
    }
    for name, (pattern, text) in checks.items():
        matches = re.findall(pattern, text)
        if matches:
            issues.append(f"    {name}: {len(matches)} occurrence(s)")
    return issues


def validate(path):
    errors = []
    warnings = []

    # 1. JSON validity
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("[OK] JSON is valid")
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"[FAIL] JSON invalid: {e}")
        return False

    # 2. Encoding check
    with open(path, 'rb') as f:
        raw = f.read()
    non_ascii = sum(1 for b in raw if b > 127)
    if non_ascii > 0:
        errors.append(f"Encoding: {non_ascii} non-ASCII bytes found. Use ensure_ascii=True")
    else:
        print("[OK] Encoding: pure ASCII")

    # 3. Structure check
    if 'containerVersion' not in data:
        errors.append("Missing 'containerVersion' key")
        print(f"\n{'='*50}")
        print(f"ERRORS: {len(errors)}")
        for e in errors:
            print(f"  - {e}")
        return False

    cv = data['containerVersion']

    # 4. Unique IDs
    for obj_type, id_key in [('tag', 'tagId'), ('trigger', 'triggerId'),
                              ('variable', 'variableId'), ('folder', 'folderId')]:
        items = cv.get(obj_type, [])
        ids = [item[id_key] for item in items]
        dupes = set(x for x in ids if ids.count(x) > 1)
        if dupes:
            errors.append(f"Duplicate {obj_type} IDs: {dupes}")
        else:
            print(f"[OK] {obj_type} IDs unique ({len(ids)} items)")

    # 5. Trigger references
    # GTM built-in trigger IDs (not exported in JSON)
    BUILTIN_TRIGGERS = {
        '2147479553',  # All Pages
        '2147479573',  # Initialization - All Pages
        '2147479572',  # Consent Initialization - All Pages
    }
    trigger_ids = {t['triggerId'] for t in cv.get('trigger', [])} | BUILTIN_TRIGGERS
    for tag in cv.get('tag', []):
        for tid in tag.get('firingTriggerId', []):
            if tid not in trigger_ids:
                errors.append(f"Tag '{tag['name']}' fires on missing trigger ID {tid}")
        for tid in tag.get('blockingTriggerId', []):
            if tid not in trigger_ids:
                errors.append(f"Tag '{tag['name']}' blocks on missing trigger ID {tid}")
    if not any('missing trigger' in e for e in errors):
        print("[OK] All trigger references valid")

    # 6. Folder references
    folder_ids = {f['folderId'] for f in cv.get('folder', [])}
    for obj_type in ['tag', 'trigger', 'variable']:
        for item in cv.get(obj_type, []):
            fid = item.get('parentFolderId')
            if fid and fid not in folder_ids:
                errors.append(f"{obj_type} '{item['name']}' references missing folder ID {fid}")
    if not any('missing folder' in e for e in errors):
        print("[OK] All folder references valid")

    # 7. ES5 compliance
    es5_issues = []
    for tag in cv.get('tag', []):
        if tag['type'] == 'html':
            for p in tag.get('parameter', []):
                if p.get('key') == 'html':
                    issues = verify_es5(p['value'], tag['name'])
                    if issues:
                        es5_issues.append(f"  Tag '{tag['name']}':")
                        es5_issues.extend(issues)
    if es5_issues:
        errors.append("ES6+ features in Custom HTML:\n" + "\n".join(es5_issues))
    else:
        html_count = sum(1 for t in cv.get('tag', []) if t['type'] == 'html')
        print(f"[OK] ES5 compliant ({html_count} Custom HTML tags checked)")

    # 8. Variable reference check (warning only)
    full = json.dumps(data, ensure_ascii=False)
    var_names = {v['name'] for v in cv.get('variable', [])}
    bi_names = {v['name'] for v in cv.get('builtInVariable', [])}
    all_names = var_names | bi_names | {'_event'}  # _event is always available
    refs = re.findall(r'\{\{([^}]+)\}\}', full)
    for ref in set(refs):
        if ref not in all_names:
            warnings.append(f"Variable reference '{{{{{ref}}}}}' not found in container variables")
    if not warnings:
        print(f"[OK] Variable references ({len(set(refs))} unique refs checked)")

    # Summary
    print(f"\n{'='*50}")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("✓ All checks passed — ready for GTM import")
    elif not errors:
        print("✓ No errors (warnings are non-blocking)")

    return len(errors) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_gtm_json>")
        sys.exit(1)
    ok = validate(sys.argv[1])
    sys.exit(0 if ok else 1)
