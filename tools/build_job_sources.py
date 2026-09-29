"""Render employer cards and search shortcuts from data/job-sources.json.

Use --write after editing sources, then --check before publishing.
No network requests or job-posting collection are performed.
"""
import argparse
from datetime import date
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- job-employers:start -->'
END = '<!-- job-employers:end -->'
TYPES = {'oem_manufacturer': 'OEM / Manufacturer', 'iso_htm_provider': 'ISO / HTM Provider', 'dialysis': 'Dialysis'}
ROLES = {'bmet','clinical_engineering','imaging','field_service','management','other','unknown'}


def validate_sources(data):
    if not isinstance(data, dict) or data.get('schema_version') != 1 or not isinstance(data.get('sources'), list):
        raise ValueError('Expected schema_version 1 and a sources array')
    seen = set()
    for source in data['sources']:
        required = {'id','name','url','source_type','employer_type','role_types','search_terms','last_reviewed','review_status','notes'}
        if not isinstance(source, dict) or set(source) != required:
            raise ValueError('Source fields do not match the directory contract')
        sid = source['id']
        if not isinstance(sid,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',sid) or sid in seen:
            raise ValueError(f'Invalid or duplicate source ID: {sid}')
        seen.add(sid)
        for key in ('name','url','notes'):
            if not isinstance(source[key],str) or not source[key].strip():
                raise ValueError(f'{sid}: {key} must be text')
        url = urlsplit(source['url'])
        if url.scheme != 'https' or not url.hostname or url.username or url.password or any(c.isspace() for c in source['url']):
            raise ValueError(f'{sid}: requires a public HTTPS URL')
        if source['source_type'] not in ('employer_careers','job_board_search'):
            raise ValueError(f'{sid}: invalid source type')
        if source['source_type'] == 'employer_careers' and source['employer_type'] not in TYPES:
            raise ValueError(f'{sid}: unsupported employer type; extend the directory filters when adding coverage')
        if source['source_type'] == 'job_board_search' and source['employer_type'] is not None:
            raise ValueError(f'{sid}: a job board is not an employer')
        for key in ('role_types','search_terms'):
            if not isinstance(source[key],list) or not source[key] or any(not isinstance(v,str) or not v.strip() for v in source[key]):
                raise ValueError(f'{sid}: {key} must be a non-empty text array')
        if not set(source['role_types']) <= ROLES:
            raise ValueError(f'{sid}: invalid role type')
        if source['review_status'] not in ('content_verified','javascript_required','unverified'):
            raise ValueError(f'{sid}: invalid review status')
        if source['last_reviewed'] is not None:
            if date.fromisoformat(source['last_reviewed']).isoformat() != source['last_reviewed']:
                raise ValueError(f'{sid}: use YYYY-MM-DD for last_reviewed')
        if source['review_status'] == 'content_verified' and source['last_reviewed'] is None:
            raise ValueError(f'{sid}: a verified source needs its review date')
    return data['sources']


def render(sources):
    lines = ['<div class="jobs-employer-grid">']
    for source in sources:
        if source['source_type'] != 'employer_careers':
            continue
        text = ' '.join([source['name'], *source['search_terms']]).lower()
        lines.extend([
            f'  <article class="jobs-employer-card" data-employer-type="{escape(source["employer_type"],quote=True)}" data-search="{escape(text,quote=True)}">',
            f'    <span class="jobs-card-type">{escape(TYPES[source["employer_type"]])}</span>',
            f'    <h3><a href="{escape(source["url"],quote=True)}" target="_blank" rel="noopener">{escape(source["name"])}</a></h3>',
            f'    <p>Search: {escape(", ".join(source["search_terms"]))}</p>',
            '  </article>',
        ])
    lines.append('</div>')
    return '\n'.join('    '+line for line in lines)


def render_searches(sources, board):
    links = [s for s in sources if s['source_type'] == 'job_board_search' and s['id'].startswith(board+'-search-')]
    return '\n'.join(f'      <a href="{escape(s["url"],quote=True)}" target="_blank" rel="noopener">{escape(s["name"])}</a>' for s in links)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--check',action='store_true')
    args = parser.parse_args()
    sources = validate_sources(json.loads((ROOT/'data/job-sources.json').read_text(encoding='utf-8')))
    page = ROOT/'biomed-jobs.html'
    old = page.read_bytes().decode('utf-8')
    if old.count(START) != 1 or old.count(END) != 1:
        raise ValueError('Expected one pair of job-employers markers')
    newline = '\r\n' if '\r\n' in old else '\n'
    content = newline + render(sources).replace('\n',newline) + newline + '    '
    new = re.sub(re.escape(START)+r'.*?'+re.escape(END),lambda _:START+content+END,old,flags=re.S)
    for board in ('indeed','linkedin','google'):
        start, end = f'<!-- job-{board}:start -->', f'<!-- job-{board}:end -->'
        if new.count(start) != 1 or new.count(end) != 1:
            raise ValueError(f'Expected one pair of {board} search markers')
        content = newline + render_searches(sources,board).replace('\n',newline) + newline + '    '
        new = re.sub(re.escape(start)+r'.*?'+re.escape(end),lambda _:start+content+end,new,flags=re.S)
    if args.write:
        page.write_bytes(new.encode('utf-8'))
    elif old != new:
        print('Employer directory is stale. Run tools/build_job_sources.py --write.')
        return 1
    print(f'{len(sources)} source records valid; employer directory {"written" if args.write else "matches"}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
