#!/usr/bin/env python3
"""Customize the guimarketing GTM Leads 2025 template for a new client.

Usage:
  python3 customize_template.py \
    --client-name "Acme Corp" \
    --ga4-id "G-XXXXXXXXXX" \
    --meta-pixel "1234567890" \
    --gads-id "AW-1234567890" \
    --domain "acme.com.br" \
    --sgtm-url "https://data.acme.com.br" \
    --output "GTM-Web_Acme_Corp.json"

Optional:
  --gads-label "XXXXXXXXXXXXXX"   Google Ads conversion label
  --activate-standby              Remove paused state from Standby tags
"""

import argparse
import json
import os
import sys
import time


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, '..', 'templates',
                             'GTM-Web_Modelo_Leads_2025_guimarketing.json')

# Maps variable name -> (field to match, path to value)
CONSTANT_REPLACEMENTS = {
    'GA4': 'ga4_id',
    'Pixel Meta': 'meta_pixel',
    'Google ADs Tag guimarketing': 'gads_id',
    'URL de Transporte': 'sgtm_url',
    'Constante - Dom\u00ednio do Cliente': 'domain',
}


def load_template():
    """Load the base template JSON."""
    path = os.path.normpath(TEMPLATE_PATH)
    if not os.path.exists(path):
        print(f"[FAIL] Template not found: {path}")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def update_constants(cv, args_dict):
    """Update constant variables with client-specific values."""
    updated = []
    for var in cv.get('variable', []):
        var_name = var.get('name', '')
        if var_name in CONSTANT_REPLACEMENTS:
            arg_key = CONSTANT_REPLACEMENTS[var_name]
            new_value = args_dict.get(arg_key)
            if new_value:
                for p in var.get('parameter', []):
                    if p.get('key') == 'value':
                        old_value = p['value']
                        p['value'] = new_value
                        updated.append(f"  {var_name}: {old_value} -> {new_value}")
    return updated


def update_container_meta(data, client_name):
    """Update container name and related metadata."""
    cv = data['containerVersion']
    container = cv.get('container', {})

    old_name = container.get('name', '')
    container['name'] = f"{client_name} - Web"
    print(f"  Container name: {old_name} -> {container['name']}")


def update_gads_label(cv, label):
    """Update Google Ads conversion label in conversion tags."""
    count = 0
    for tag in cv.get('tag', []):
        if tag.get('type') == 'awct':
            for p in tag.get('parameter', []):
                if p.get('key') == 'conversionLabel':
                    p['value'] = label
                    count += 1
    return count


def activate_standby(cv):
    """Remove paused state from Standby folder tags."""
    standby_folder_id = None
    for folder in cv.get('folder', []):
        if 'Standby' in folder.get('name', ''):
            standby_folder_id = folder['folderId']
            break

    if not standby_folder_id:
        print("  [WARN] Standby folder not found")
        return 0

    count = 0
    for tag in cv.get('tag', []):
        if tag.get('parentFolderId') == standby_folder_id and tag.get('paused'):
            del tag['paused']
            count += 1
            print(f"  Activated: {tag['name']}")
    return count


def rename_gads_variable(cv, client_name):
    """Rename 'Google ADs Tag guimarketing' to use client name."""
    old_name = 'Google ADs Tag guimarketing'
    new_name = f'Google ADs Tag {client_name}'

    # Rename the variable itself
    for var in cv.get('variable', []):
        if var.get('name') == old_name:
            var['name'] = new_name
            break

    # Update all references {{old_name}} -> {{new_name}}
    text = json.dumps(cv, ensure_ascii=False)
    text = text.replace('{{' + old_name + '}}', '{{' + new_name + '}}')
    updated_cv = json.loads(text)

    # Replace containerVersion in-place
    for key in updated_cv:
        cv[key] = updated_cv[key]

    return new_name


def main():
    parser = argparse.ArgumentParser(
        description='Customize GTM template for a new client')
    parser.add_argument('--client-name', required=True,
                        help='Client name (used in container name)')
    parser.add_argument('--ga4-id', required=True,
                        help='GA4 Measurement ID (G-XXXXXXXXXX)')
    parser.add_argument('--meta-pixel', required=True,
                        help='Meta Pixel ID (numeric string)')
    parser.add_argument('--gads-id', required=True,
                        help='Google Ads ID (AW-XXXXXXXXX)')
    parser.add_argument('--domain', required=True,
                        help='Client domain (example.com.br)')
    parser.add_argument('--sgtm-url', required=True,
                        help='sGTM transport URL (https://data.example.com.br)')
    parser.add_argument('--output', default=None,
                        help='Output file path (default: GTM-Web_<client>.json)')
    parser.add_argument('--gads-label', default=None,
                        help='Google Ads conversion label')
    parser.add_argument('--activate-standby', action='store_true',
                        help='Activate all Standby tags')

    args = parser.parse_args()

    # Default output filename
    if not args.output:
        safe_name = args.client_name.replace(' ', '_')
        args.output = f'GTM-Web_{safe_name}.json'

    print(f"\n{'='*60}")
    print(f"Customizing GTM template for: {args.client_name}")
    print(f"{'='*60}\n")

    # Load template
    data = load_template()
    cv = data['containerVersion']

    # 1. Update container metadata
    print("[1/5] Updating container metadata...")
    update_container_meta(data, args.client_name)

    # 2. Update constants
    print("\n[2/5] Updating client-specific constants...")
    args_dict = {
        'ga4_id': args.ga4_id,
        'meta_pixel': args.meta_pixel,
        'gads_id': args.gads_id,
        'domain': args.domain,
        'sgtm_url': args.sgtm_url,
    }
    updates = update_constants(cv, args_dict)
    for u in updates:
        print(u)

    # 3. Rename Google Ads variable
    print("\n[3/5] Renaming Google Ads variable...")
    new_var_name = rename_gads_variable(cv, args.client_name)
    print(f"  Renamed to: {new_var_name}")

    # 4. Optional: Google Ads conversion label
    if args.gads_label:
        print("\n[4/5] Updating Google Ads conversion label...")
        count = update_gads_label(cv, args.gads_label)
        print(f"  Updated {count} conversion tag(s)")
    else:
        print("\n[4/5] Google Ads conversion label: SKIPPED (no --gads-label)")

    # 5. Optional: Activate standby tags
    if args.activate_standby:
        print("\n[5/5] Activating Standby tags...")
        count = activate_standby(cv)
        print(f"  Activated {count} tag(s)")
    else:
        print("\n[5/5] Standby activation: SKIPPED (no --activate-standby)")

    # Update export time
    data['exportTime'] = time.strftime('%Y-%m-%d %H:%M:%S')

    # Save (ALWAYS ensure_ascii=True for GTM compatibility)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=True, indent=4)

    print(f"\n{'='*60}")
    print(f"[OK] Saved: {args.output}")
    print(f"{'='*60}")
    print(f"\nNext steps:")
    print(f"  1. Validate: python3 ../gtm-expert/scripts/validate_gtm.py {args.output}")
    print(f"  2. Review the checklist in SKILL.md")
    print(f"  3. Import into GTM")


if __name__ == '__main__':
    main()
