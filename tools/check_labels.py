#!/usr/bin/env python3
"""Check the CTNCS codebook against its naming rules.

Rule: a Content Style (Level 4) names an angle or community within its Niche.
It never names a format and is never broader than its Niche.

Usage: python3 tools/check_labels.py [CTNCS_Codebook_v2.0.csv]
Exits non-zero and lists offending labels if the rule is broken.
"""
import csv, re, sys

FORMAT_WORDS = {'vlog', 'vlogs', 'tutorial', 'tutorials', 'review', 'reviews', 'highlight', 'highlights',
    'clip', 'clips', 'recap', 'recaps', 'tip', 'tips', 'guide', 'guides', 'explainer', 'explainers',
    'update', 'updates', 'diary', 'diaries', 'log', 'logs', 'stream', 'streams', 'playthrough',
    'playthroughs', 'gameplay', 'session', 'sessions', 'report', 'reports', 'compilation', 'montage',
    'reaction', 'reactions', 'haul', 'hauls', 'podcast', 'podcasts', 'breakdown', 'breakdowns'}

# Genre names whose format word is the community's own name for the subject.
# Add to this list only after review.
ALLOWED = {'Taste Tests', 'Fast Food Challenges', 'Toy Unboxings', 'Follow-Along Workouts',
    'Skincare Routines', 'Birth Chart Readings', 'Test Drives', 'Hot Takes & Debate Shows',
    'Sports Betting Picks', 'Apartment & Home Tours', 'Technical Analysis', 'Fundamental Analysis',
    'Restaurant & Product Reviews', 'Skincare Reviews & Dupes', 'Comic Reviews & Recommendations',
    'Firearm & Gear Reviews', 'Cannabis Product Reviews', 'Alcohol Reviews & Culture', 'Story Guides',
    'First-Time Buyer Guides', 'Sports Podcasts', 'Life Updates', 'Kid Reviews & Play Vlogs',
    'Body Image Commentary'}

def main(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    labels = {r['code']: r['label'] for r in rows}
    problems = []
    for r in rows:
        if r['level'] != '4':
            continue
        words = {w.lower() for w in re.split(r'[\s/&,()-]+', r['label']) if w}
        hit = sorted(words & FORMAT_WORDS)
        if hit and r['label'] not in ALLOWED:
            problems.append(f"{r['code']} {r['label']}: names a format ({', '.join(hit)})")
        if r['label'] == labels.get(r['parent_code']):
            problems.append(f"{r['code']} {r['label']}: same label as its Niche")
    if problems:
        print('\n'.join(problems))
        sys.exit(1)
    print('Content Style labels: OK')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'CTNCS_Codebook_v2.0.csv')
