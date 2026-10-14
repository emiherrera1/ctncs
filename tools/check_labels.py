#!/usr/bin/env python3
"""Check the CTNCS codebook against its rules, and validate CTNCS IDs.

Rules checked:
- A Sub-Niche (Level 4) names a narrower subject within its Niche.
  It never names a format and never repeats its Niche's label.
- Every Sub-Niche lists 3 to 6 common formats, each an active Format code,
  with one example concept per format.
- A CTNCS ID matches the pattern, names a Sub-Niche in the codebook, and uses
  one of that Sub-Niche's common formats or a universal format (Commentary,
  Compilation, Highlight, Mashups, Reaction, Parody), which wraps any subject.

Usage:
  python3 tools/check_labels.py                    # check the codebook
  python3 tools/check_labels.py --id 01.01.001.001.41 [more IDs]
Exits non-zero and lists the problems if a rule is broken.
"""
import csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ID_RE = re.compile(r'^\d{2}\.\d{2}\.\d{3}\.\d{3}\.\d{2}(\.\d{3})?$')

FORMAT_WORDS = {'vlog', 'vlogs', 'tutorial', 'tutorials', 'review', 'reviews', 'highlight', 'highlights',
    'clip', 'clips', 'recap', 'recaps', 'tip', 'tips', 'guide', 'guides', 'explainer', 'explainers',
    'update', 'updates', 'diary', 'diaries', 'log', 'logs', 'stream', 'streams', 'playthrough',
    'playthroughs', 'gameplay', 'session', 'sessions', 'report', 'reports', 'compilation', 'montage',
    'reaction', 'reactions', 'haul', 'hauls', 'podcast', 'podcasts', 'breakdown', 'breakdowns',
    'unboxing', 'unboxings', 'challenge', 'challenges', 'routine', 'routines', 'commentary', 'picks'}

# Subject names that contain a format word as part of the subject itself.
# Add to this list only after review.
ALLOWED = {'Technical Analysis', 'Fundamental Analysis'}


def load(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    fmts = {r['code']: r for r in csv.DictReader(open(os.path.join(ROOT, 'CTNCS_Formats_v2.0.csv'), encoding='utf-8'))}
    return rows, fmts


def active(fmts):
    return {c for c, r in fmts.items() if r.get('status', 'active').lower() != 'retired'}


def universal(fmts):
    return {c for c, r in fmts.items() if r.get('universal', 'FALSE').upper() == 'TRUE'}


def check_codebook(rows, fmts):
    labels = {r['code']: r['label'] for r in rows}
    ok = active(fmts)
    problems = []
    for r in rows:
        if r['level'] != '4':
            continue
        c, lab = r['code'], r['label']
        if r['level_name'] != 'Sub-Niche':
            problems.append(f"{c} {lab}: level_name is {r['level_name']!r}, expected 'Sub-Niche'")
        words = {w.lower() for w in re.split(r'[\s/&,()-]+', lab) if w}
        hit = sorted(words & FORMAT_WORDS)
        if hit and lab not in ALLOWED:
            problems.append(f"{c} {lab}: names a format ({', '.join(hit)})")
        if lab == labels.get(r['parent_code']):
            problems.append(f"{c} {lab}: same label as its Niche")
        fs = [f for f in r['common_formats'].split(';') if f]
        ex = [e for e in r['example_concepts'].split(';') if e]
        if not 3 <= len(fs) <= 6:
            problems.append(f"{c} {lab}: {len(fs)} common formats (need 3 to 6)")
        if len(set(fs)) != len(fs):
            problems.append(f"{c} {lab}: repeated format code")
        for f in fs:
            if f not in ok:
                problems.append(f"{c} {lab}: format {f} is not an active Format code")
        if len(ex) != len(fs):
            problems.append(f"{c} {lab}: {len(ex)} example concepts for {len(fs)} formats")
    used = {f for r in rows if r['level'] == '4' for f in r['common_formats'].split(';') if f}
    for f in sorted(ok - used - universal(fmts)):
        problems.append(f"Format {f} {fmts[f]['label']}: active but on no Sub-Niche's list")
    return problems


def check_id(cid, rows, fmts=None):
    """Return a list of problems with one CTNCS ID (empty if valid)."""
    if fmts is None:
        fmts = load(os.path.join(ROOT, 'CTNCS_Codebook_v2.0.csv'))[1]
    if not ID_RE.match(cid):
        return [f"{cid}: does not match SS.CC.NNN.SSS.FF(.RRR)"]
    parts = cid.split('.')
    sub, fmt = '.'.join(parts[:4]), parts[4]
    node = next((r for r in rows if r['code'] == sub), None)
    if node is None or node['level'] != '4':
        return [f"{cid}: {sub} is not a Sub-Niche in the codebook"]
    allowed = node['common_formats'].split(';')
    if fmt not in allowed and fmt not in universal(fmts):
        return [f"{cid}: format {fmt} is not a common format of {sub} {node['label']} (allowed: {', '.join(allowed)}, or a universal format: {', '.join(sorted(universal(fmts)))})"]
    return []


def main(argv):
    path = os.path.join(ROOT, 'CTNCS_Codebook_v2.0.csv')
    rows, fmts = load(path)
    if argv[:1] == ['--id']:
        problems = [p for cid in argv[1:] for p in check_id(cid, rows, fmts)]
        if problems:
            print('\n'.join(problems)); sys.exit(1)
        print(f'{len(argv) - 1} ID(s): OK'); return
    if argv:
        path = argv[0]; rows, fmts = load(path)
    problems = check_codebook(rows, fmts)
    if problems:
        print('\n'.join(problems)); sys.exit(1)
    print('Codebook: OK (Sub-Niche labels and common formats)')


if __name__ == '__main__':
    main(sys.argv[1:])
