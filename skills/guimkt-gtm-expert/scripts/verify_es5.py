#!/usr/bin/env python3
"""Verify ES5 compliance for JavaScript in GTM Custom HTML tags.

Usage:
  python3 verify_es5.py <path_to_gtm_json>          # Check all HTML tags
  python3 verify_es5.py <path_to_js_file> --raw      # Check a raw JS file

GTM's compiler runs in ECMASCRIPT3/5 mode. This script detects:
  const, let, arrow functions, template literals, destructuring,
  spread operators, optional chaining, nullish coalescing,
  Object.entries/values/assign, for...of, async/await, class
"""

import json
import re
import sys


ES6_CHECKS = {
    'const': r'\bconst\b',
    'let': r'\blet\b',
    'arrow function': r'=>',
    'template literal': r'`',
    'destructuring [...]': r'\[\.\.\.', 
    'spread {...}': r'\{\.\.\.', 
    'optional chaining ?.': r'\?\.\w',
    'nullish coalescing ??': r'\?\?',
    'Object.entries': r'Object\.entries',
    'Object.values': r'Object\.values',
    'Object.fromEntries': r'Object\.fromEntries',
    'Array.from': r'Array\.from',
    'class declaration': r'\bclass\s+\w',
    'async/await': r'\basync\b|\bawait\b',
    'for...of': r'\bfor\s*\(\s*(?:const|let|var)\s+\w+\s+of\b',
    'Promise': r'\bnew\s+Promise\b',
    'Symbol': r'\bSymbol\b',
    'Map/Set': r'\bnew\s+(?:Map|Set|WeakMap|WeakSet)\b',
}


def check_es5(js_code, label=""):
    """Check JS code for ES6+ features. Returns list of (feature, count) tuples."""
    # Strip HTML wrapper
    js = js_code.replace('<script>', '').replace('</script>', '')
    
    issues = []
    for name, pattern in ES6_CHECKS.items():
        matches = re.findall(pattern, js)
        if matches:
            issues.append((name, len(matches)))
    return issues


def check_gtm_json(path):
    """Check all Custom HTML tags in a GTM JSON file."""
    with open(path, 'r') as f:
        data = json.load(f)

    cv = data['containerVersion']
    all_clean = True

    for tag in cv.get('tag', []):
        if tag['type'] != 'html':
            continue
        for p in tag.get('parameter', []):
            if p.get('key') != 'html':
                continue
            issues = check_es5(p['value'], tag['name'])
            if issues:
                all_clean = False
                print(f"\n✗ Tag: {tag['name']} (ID: {tag['tagId']})")
                for feat, count in issues:
                    print(f"    {feat}: {count}x")
            else:
                print(f"✓ Tag: {tag['name']} — ES5 OK")

    if all_clean:
        print("\n✓ All Custom HTML tags are ES5 compliant")
    else:
        print("\n✗ ES6+ features detected — fix before importing to GTM")
    return all_clean


def check_raw_file(path):
    """Check a raw JS file for ES5 compliance."""
    with open(path, 'r') as f:
        code = f.read()

    issues = check_es5(code)
    if issues:
        print(f"✗ ES6+ features in {path}:")
        for feat, count in issues:
            print(f"    {feat}: {count}x")
        return False
    else:
        print(f"✓ {path} — ES5 compliant")
        return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path> [--raw]")
        sys.exit(1)

    path = sys.argv[1]
    raw = '--raw' in sys.argv

    if raw:
        ok = check_raw_file(path)
    else:
        ok = check_gtm_json(path)

    sys.exit(0 if ok else 1)
