#!/usr/bin/env python3
"""Validate guide metadata, local links, sitemap coverage, and page structure."""
from __future__ import annotations

import json, re, sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://jaketroubleshoots.com"
REQ = {"title", "description", "assetType", "manufacturer", "model", "url", "dateAdded", "steps"}
GUIDE_HEADINGS = ["Asset Type", "Manufacturer", "Model", "What This Guide Helps With", "Step-by-Step Troubleshooting"]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.headings=[]; self.title=""
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if "id" in d: self.ids.add(d["id"])
        if tag in {"a","link"} and d.get("href"): self.links.append((tag,d["href"]))
        if tag in {"img","script"} and d.get("src"): self.links.append((tag,d["src"]))
        self._tag=tag
    def handle_data(self, data):
        if getattr(self,'_tag',None) in {"h2","h3","h4","title"}:
            txt=" ".join(data.split())
            if txt:
                if self._tag=="title": self.title += txt
                else: self.headings.append(txt)
    def handle_endtag(self, tag):
        self._tag=None

def html_files(): return sorted(p for p in ROOT.rglob('*.html') if '.git' not in p.parts)
def data_files(): return sorted((ROOT/'data').glob('guides-*.json'))
def norm_url(u): return u[:-5] if u.endswith('.html') else u

def load_records(errors):
    records=[]; listed=[]
    try: listed=json.load(open(ROOT/'data/guides.json'))
    except Exception as e: errors.append(f"data/guides.json invalid JSON: {e}")
    for rel in listed:
        p=ROOT/rel
        if not p.exists(): errors.append(f"data/guides.json references missing file: {rel}"); continue
        try: data=json.load(open(p))
        except Exception as e: errors.append(f"{rel} invalid JSON: {e}"); continue
        if not isinstance(data,list): errors.append(f"{rel} is not a list"); continue
        for i,r in enumerate(data): records.append((rel,i,r))
    unlisted=sorted(p.relative_to(ROOT).as_posix() for p in data_files() if p.relative_to(ROOT).as_posix() not in set(listed))
    for u in unlisted: errors.append(f"Guide data file not listed in data/guides.json: {u}")
    return records

def validate_records(records, errors, warnings):
    urls=[]; by_model=defaultdict(set); by_mfr=defaultdict(set)
    for rel,i,r in records:
        where=f"{rel}[{i}]"
        if not isinstance(r,dict): errors.append(f"{where} is not an object"); continue
        miss=REQ-set(r); extra=set(r)-REQ
        if miss: errors.append(f"{where} missing fields: {', '.join(sorted(miss))}")
        if extra: warnings.append(f"{where} extra fields: {', '.join(sorted(extra))}")
        for k in REQ-{"steps"}:
            if k in r and (not isinstance(r[k],str) or not r[k].strip()): errors.append(f"{where}.{k} must be a non-empty string")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r.get('dateAdded',''))): errors.append(f"{where}.dateAdded is not YYYY-MM-DD")
        if 'url' in r:
            urls.append((r['url'],where)); path=ROOT/r['url']
            if not path.exists(): errors.append(f"{where}.url target missing: {r['url']}")
            if not str(r['url']).endswith('.html'): warnings.append(f"{where}.url does not end in .html: {r['url']}")
        steps=r.get('steps')
        if not isinstance(steps,list) or not steps: errors.append(f"{where}.steps must be a non-empty list")
        else:
            for j,s in enumerate(steps):
                if not isinstance(s,dict) or set(s)!={"title","instructions"}: errors.append(f"{where}.steps[{j}] must contain only title and instructions")
        if r.get('model'): by_model[r['model'].lower()].add(r['model'])
        if r.get('manufacturer'): by_mfr[r['manufacturer'].lower()].add(r['manufacturer'])
    for url,c in Counter(u for u,_ in urls).items():
        if c>1: errors.append(f"Duplicate guide URL: {url}")
    for key,vals in sorted({**by_model, **by_mfr}.items()):
        if len(vals)>1: warnings.append(f"Case-only naming variation: {sorted(vals)}")

def local_target(src, href):
    p=urlparse(href)
    if p.scheme or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('//'): return None
    path=unquote(p.path)
    if not path: return (src, p.fragment)
    target=(ROOT/path.lstrip('/')).resolve() if path.startswith('/') else (src.parent/path).resolve()
    return (target, p.fragment)

def validate_links(errors):
    for f in html_files():
        lp=LinkParser(); lp.feed(f.read_text(errors='ignore'))
        for tag,href in lp.links:
            t=local_target(f,href)
            if not t: continue
            target,frag=t
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): errors.append(f"Broken local {tag} link in {f.relative_to(ROOT)}: {href}")
            elif frag and target.suffix=='.html':
                lp2=LinkParser(); lp2.feed(target.read_text(errors='ignore'))
                if frag not in lp2.ids: errors.append(f"Broken fragment in {f.relative_to(ROOT)}: {href}")

def validate_sitemap(records, errors, warnings):
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    locs={e.text for e in ET.parse(ROOT/'sitemap.xml').findall('.//s:loc',ns)}
    expected={BASE_URL+'/'+p.relative_to(ROOT).as_posix().replace('index.html','').rstrip('/') for p in html_files()}
    expected.discard(BASE_URL)
    expected.add(BASE_URL + "/")
    guide_expected={BASE_URL+'/'+r['url'][:-5] for _,_,r in records if isinstance(r,dict) and 'url' in r}
    for u in sorted(expected-locs): errors.append(f"Missing sitemap entry: {u}")
    for u in sorted(locs-expected-guide_expected-{BASE_URL}): warnings.append(f"Sitemap entry has no matching HTML file: {u}")

def validate_templates(records, warnings):
    record_paths={ROOT/r['url'] for _,_,r in records if isinstance(r,dict) and 'url' in r}
    for f in sorted(record_paths):
        if not f.exists(): continue
        lp=LinkParser(); lp.feed(f.read_text(errors='ignore'))
        missing=[h for h in GUIDE_HEADINGS if h not in lp.headings]
        if missing: warnings.append(f"Guide template deviation in {f.relative_to(ROOT)}: missing headings {missing}")

def main():
    errors=[]; warnings=[]
    records=load_records(errors); validate_records(records, errors, warnings); validate_links(errors); validate_sitemap(records, errors, warnings); validate_templates(records, warnings)
    print(f"Guide records checked: {len(records)}")
    print(f"HTML files checked: {len(html_files())}")
    print(f"Errors: {len(errors)}")
    for e in errors[:200]: print('ERROR:',e)
    if len(errors)>200: print(f"ERROR: ... {len(errors)-200} more")
    print(f"Warnings: {len(warnings)}")
    for w in warnings[:200]: print('WARN:',w)
    if len(warnings)>200: print(f"WARN: ... {len(warnings)-200} more")
    return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
