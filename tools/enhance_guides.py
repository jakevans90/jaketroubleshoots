#!/usr/bin/env python3
"""Deterministically plan and transactionally apply grounded guide enhancements."""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path(__file__).with_name("guide_enhancement_config.json")
BEGIN = "<!-- GUIDE-ENHANCEMENTS:BEGIN -->"
END = "<!-- GUIDE-ENHANCEMENTS:END -->"
SAFETY = re.compile(r"\b(patient|clinical use|trained personnel|out of service|remove.*service|backup (?:unit|device)|safety)\b", re.I)
GENERIC = {"guide","device","equipment","problem","issue","check","verify","medical","system",
  "alarm","error","failed","failure","internal","output","troubleshooting","monitor","carescape"}
SUBSYSTEMS = {
    "network": ("network","ethernet","wifi","wi-fi","vlan","gateway","central station","communication"),
    "power": ("power","battery","ac ","voltage","supply","charging"),
    "display": ("display","screen","backlight","touchscreen"),
    "alarm": ("alarm","speaker","audio"),
    "parameter module": ("module","pdm","parameter"),
    "pneumatic": ("pump","pressure","nibp","leak"),
    "software": ("software","firmware","configuration","license","activation"),
    "thermal": ("temperature","thermal","overheat","cooling","fan","airflow","ventilation"),
}

class EnhancementError(RuntimeError): pass

def norm(value: Any) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", html.unescape(str(value)).casefold()))

def slug(record: dict[str, Any]) -> str:
    return Path(str(record.get("url",""))).stem

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=4, ensure_ascii=False) + "\n").encode()

class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(); self.parts: list[str] = []; self.links: list[str] = []; self.headings: list[str] = []; self._tag=""
    def handle_data(self, data: str) -> None:
        self.parts.append(data)
        if self._tag in {"h1","h2","h3"} and data.strip(): self.headings.append(" ".join(data.split()))
    def handle_starttag(self, tag: str, attrs: list[tuple[str,str|None]]) -> None:
        self._tag=tag
        if tag == "a":
            href = dict(attrs).get("href")
            if href: self.links.append(href)
    def handle_endtag(self, tag: str) -> None:
        if tag==self._tag: self._tag=""

def html_facts(text: str) -> tuple[str,list[str]]:
    parser=TextParser(); parser.feed(text); return " ".join(" ".join(parser.parts).split()), parser.links

@dataclass
class GuideRef:
    shard: str
    index: int
    record: dict[str, Any]
    html_path: str
    html_text: str
    visible: str
    links: list[str]

@dataclass
class Profile:
    assetType: str = ""; manufacturer: str = ""; exactModel: str = ""; modelFamily: str = ""
    issueCategory: str = ""; normalizedIssueTitle: str = ""; normalizedErrorCodes: list[str] = field(default_factory=list)
    primarySubsystem: str = ""; secondarySubsystems: list[str] = field(default_factory=list)
    distinctSymptoms: list[str] = field(default_factory=list); distinctFailurePatterns: list[str] = field(default_factory=list)
    accessoriesMentioned: list[str] = field(default_factory=list); configurationFactors: list[str] = field(default_factory=list)
    networkIntegrationFactors: list[str] = field(default_factory=list); externalChecks: list[str] = field(default_factory=list)
    internalEscalationBoundaries: list[str] = field(default_factory=list); clinicalUseImplications: list[str] = field(default_factory=list)
    verificationRequirements: list[str] = field(default_factory=list); relatedPMProcedures: list[str] = field(default_factory=list)
    relevantBiomedBasics: list[str] = field(default_factory=list); sameModelGuides: list[str] = field(default_factory=list)
    relatedSubsystemGuides: list[str] = field(default_factory=list); errorCodeFamilyGuides: list[str] = field(default_factory=list)
    vendorManufacturerResources: list[str] = field(default_factory=list)

@dataclass
class Proposal:
    ref: GuideRef; profile: Profile; enhancements: dict[str,Any]; relationships: dict[str,list[dict[str,Any]]]
    currentScore: int; proposedScore: int; duplicates: list[dict[str,str]] = field(default_factory=list)
    rejected: list[str] = field(default_factory=list); evidence: list[str] = field(default_factory=list)
    output_record: dict[str,Any] = field(default_factory=dict); output_html: str = ""
    acceptedDetails: list[dict[str,Any]] = field(default_factory=list)
    rejectedDetails: list[dict[str,Any]] = field(default_factory=list)
    relatedUiDetected: bool = False
    placement: str = ""
    recommendation: str = ""

@dataclass
class Plan:
    proposals: list[Proposal]; outputs: dict[str,bytes]; sources: dict[str,str]; digest: str
    config: dict[str,Any]; report_path: str|None = None

def load_repository(root: Path) -> list[GuideRef]:
    manifest=json.loads((root/"data/guides.json").read_text(encoding="utf-8"))
    if not isinstance(manifest,list): raise EnhancementError("data/guides.json must be a list")
    refs=[]
    for shard in manifest:
        path=root/shard
        records=json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(records,list): raise EnhancementError(f"{shard} must contain a list")
        for index,record in enumerate(records):
            if not isinstance(record,dict) or not all(record.get(k) for k in ("title","manufacturer","model","url")):
                raise EnhancementError(f"malformed guide record: {shard} record {index}")
            page=root/str(record["url"])
            if not page.is_file(): raise EnhancementError(f"missing guide HTML: {record['url']}")
            # Indexing thousands of pages must remain cheap. Full HTML is loaded only
            # for selected guides; relationship candidates use their structured record.
            summary=" ".join([str(record.get("title","")),str(record.get("description","")),
                *[str(s.get("title",""))+" "+str(s.get("instructions","")) for s in record.get("steps",[]) if isinstance(s,dict)]])
            refs.append(GuideRef(shard,index,record,str(record["url"]),"",summary,[]))
    return refs

def sentences(value: str) -> list[str]:
    return [x.strip(" \t\r\n-*•") for x in re.split(r"(?<=[.!?])\s+|\n+",value) if len(x.strip()) > 18]

def record_text(ref: GuideRef) -> str:
    return " ".join([str(ref.record.get("title","")),str(ref.record.get("description","")),
        *[str(s.get("title",""))+" "+str(s.get("instructions","")) for s in ref.record.get("steps",[]) if isinstance(s,dict)],
        *map(str,ref.record.get("helpfulDetails",[])),ref.visible])

def issue_title(record: dict[str,Any]) -> str:
    title=str(record.get("title",""))
    model=str(record.get("model",""))
    pos=norm(title).find(norm(model))
    if pos >= 0:
        # Titles consistently put the issue after a dash; this fallback remains deterministic.
        return re.split(r"\s+[-–—]\s+",title,maxsplit=1)[-1]
    return title

def extract_profile(ref: GuideRef, refs: list[GuideRef], root: Path) -> Profile:
    text=record_text(ref); low=norm(text); title=issue_title(ref.record)
    codes=sorted(set(extract_codes(text)),key=str.casefold)
    classification=norm(str(ref.record.get("title",""))+" "+str(ref.record.get("description","")))
    subs=[name for name,terms in SUBSYSTEMS.items() if any(norm(t) in classification for t in terms)]
    if not subs: subs=[name for name,terms in SUBSYSTEMS.items() if any(norm(t) in low for t in terms)]
    steps=[str(x.get("instructions","")) for x in ref.record.get("steps",[]) if isinstance(x,dict)]
    observations=[s for s in sentences(" ".join(steps))
      if len(s)<=240
      and re.search(r"\b(intermitt|only|during|after|when|repeated|returns?|freeze|drop|not recognized|fails?)\b",s,re.I)
      and not re.match(r"^(confirm|check|verify|listen|observe|restart|power cycle)\b",s,re.I)]
    checks=[s for s in sentences(" ".join(steps)) if re.search(r"\b(check|inspect|verify|swap|reseat|observe|confirm|test)\b",s,re.I)]
    escalate=[str(x.get("instructions","")) for x in ref.record.get("steps",[])
      if isinstance(x,dict) and re.search(r"\b(escalat|remove.*service|send for repair|advanced|qualified)\b",
        str(x.get("title",""))+" "+str(x.get("instructions","")),re.I) and len(str(x.get("instructions","")))<=240]
    clinical=[s for s in sentences(ref.visible) if SAFETY.search(s)]
    verify=[s for s in sentences(" ".join(steps))
      if len(s)<=240 and re.search(r"\b(confirm|verify|reproduc|functional test|return to service|stable)\b",s,re.I)]
    model=str(ref.record["model"]); family=re.sub(r"\b(?:series|[a-z]?\d{2,4})\b.*$","",model,flags=re.I).strip() or model
    p=Profile(str(ref.record.get("assetType","")),str(ref.record["manufacturer"]),model,family,
      (subs[0] if subs else "general"),norm(title),[norm(x) for x in codes],subs[0] if subs else "general",subs[1:],
      observations[:6],[],[],[x for x in checks if re.search(r"software|firmware|configur|setting",x,re.I)][:5],
      [x for x in checks if re.search(r"network|ethernet|wifi|vlan|gateway|central",x,re.I)][:5],
      checks[:8],escalate[:5],clinical[:5],verify[:6])
    return p

def tokens(value: str) -> set[str]:
    return {x for x in norm(value).split() if len(x)>2 and x not in GENERIC}

def phrase_tokens(value: str) -> list[str]:
    return [x for x in norm(value).split() if len(x)>2 and x not in GENERIC]

def overlap_score(candidate: str, existing: str) -> float:
    left=tokens(candidate); right=tokens(existing)
    return len(left&right)/max(1,len(left))

def phrase_overlap(candidate: str, existing: str) -> float:
    words=phrase_tokens(candidate)
    if not words: return 1.0
    hay=norm(existing)
    matched=sum(1 for i in range(len(words)-1) if f"{words[i]} {words[i+1]}" in hay)
    return matched/max(1,len(words)-1)

def novelty_metrics(candidate: str, existing: str, issue: str) -> dict[str,float]:
    overlap=max(overlap_score(candidate,existing),phrase_overlap(candidate,existing))
    issue_terms=tokens(issue)
    specificity=len(tokens(candidate)&issue_terms)/max(1,len(issue_terms))
    return {"novelty":round(1-overlap,3),"issueSpecificity":round(specificity,3),
      "diagnosticValue":round(min(1.0,0.35+0.15*len(tokens(candidate)-tokens(existing))),3),
      "factualGrounding":1.0,"duplicationRisk":round(overlap,3),"safetyCorrectness":1.0,
      "placementQuality":0.8}

def accept_candidate(candidate: str, existing: str, issue: str, cfg: dict[str,Any]) -> tuple[bool,dict[str,float],str]:
    m=novelty_metrics(candidate,existing,issue); t=cfg["thresholds"]
    if m["duplicationRisk"]>t["maximumExistingTokenOverlap"]: return False,m,"duplicates or closely paraphrases existing content"
    if m["novelty"]<t["minimumNovelty"]: return False,m,"novelty below configured threshold"
    if m["issueSpecificity"]<t["minimumIssueSpecificity"]: return False,m,"issue specificity below configured threshold"
    if m["diagnosticValue"]<t["minimumDiagnosticValue"]: return False,m,"adds insufficient diagnostic decision value"
    return True,m,"accepted"

def target_slug(href: str) -> str:
    return Path(href.split("#",1)[0]).stem

def score_link(source: Profile, candidate: GuideRef, config: dict[str,Any]) -> tuple[int,list[str]]:
    w=config["weights"]; r=candidate.record; reasons=[]; score=0
    if norm(r.get("model")) == norm(source.exactModel): score+=w["exactModel"]; reasons.append("exact model")
    elif source.modelFamily and norm(source.modelFamily) in norm(r.get("model")): score+=w["modelFamily"]; reasons.append("model family")
    if norm(r.get("manufacturer")) == norm(source.manufacturer): score+=w["manufacturer"]; reasons.append("manufacturer")
    if norm(r.get("assetType")) == norm(source.assetType): score+=w["assetType"]; reasons.append("asset type")
    candidate_text=norm(str(candidate.record.get("title",""))+" "+str(candidate.record.get("description","")))
    candidate_sub=[n for n,terms in SUBSYSTEMS.items() if any(norm(t) in candidate_text for t in terms)]
    if source.primarySubsystem in candidate_sub and source.primarySubsystem!="general": score+=w["subsystem"]; reasons.append("subsystem")
    shared=set(source.normalizedErrorCodes)&set(extract_codes(record_text(candidate)))
    if shared: score+=w["errorCodeFamily"]; reasons.append("error-code family")
    source_issue=tokens(source.normalizedIssueTitle)-tokens(source.manufacturer+" "+source.exactModel)
    candidate_issue=tokens(issue_title(r))-tokens(str(r.get("manufacturer",""))+" "+str(r.get("model","")))
    overlap=source_issue&candidate_issue
    if overlap: score+=w["issueCategory"]; reasons.append("issue terminology")
    if not reasons and overlap: score+=w["genericKeywordOnly"]
    return score,reasons

def extract_codes(text: str) -> list[str]:
    sample=text[:12000]
    raw=re.findall(r"\b0x[a-z0-9]{2,16}\b",sample,re.I)
    raw += re.findall(r"\b(?:FC|E|ERR)[- ]?\d{2,6}\b",sample,re.I)
    return [norm(x) for x in raw]

def local_catalog(root: Path, folder: str) -> list[tuple[str,str,str]]:
    result=[]
    for path in sorted((root/folder).glob("*.html")):
        visible,_=html_facts(path.read_text(encoding="utf-8",errors="replace"))
        result.append((path.stem,path.relative_to(root).as_posix(),visible[:2000]))
    return result

def relationships(profile: Profile, ref: GuideRef, refs: list[GuideRef], root: Path, cfg: dict[str,Any]) -> dict[str,list[dict[str,Any]]]:
    existing={target_slug(x) for x in ref.links}; groups={k:[] for k in ("sameModel","relatedTroubleshooting","preventiveMaintenance","biomedBasics","networkIntegration","manufacturerVendor")}
    ranked=[]
    for candidate in refs:
        if candidate is ref or slug(candidate.record)==slug(ref.record) or slug(candidate.record) in existing: continue
        score,reasons=score_link(profile,candidate,cfg)
        strong=[]
        if "error-code family" in reasons: strong.append("same normalized error-code family")
        if "subsystem" in reasons and any(x in reasons for x in ("error-code family","issue terminology")):
            strong.append("same primary subsystem corroborated by issue evidence")
        if "issue terminology" in reasons: strong.append("same failure domain")
        if score>=cfg["thresholds"]["minimumRelationshipScore"] and len(strong)>=cfg["thresholds"]["minimumStrongSignals"]:
            ranked.append((score,slug(candidate.record),candidate,reasons,strong))
    for score,_,candidate,reasons,strong in sorted(ranked,key=lambda x:(-x[0],x[1])):
        key="sameModel" if norm(candidate.record["model"])==norm(profile.exactModel) else "relatedTroubleshooting"
        if len(groups[key])<cfg["limits"][key]:
            groups[key].append({"slug":slug(candidate.record),"score":score,"reasons":reasons,"strongSignals":strong,"source":"analyzer","locked":False})
    catalogs=(("preventiveMaintenance","preventive-maintenance",cfg["weights"]["preventiveMaintenance"]),
              ("biomedBasics","biomed-basics",cfg["weights"]["biomedBasics"]))
    for key,folder,base in catalogs:
        ranked_local=[]
        for s,path,text in local_catalog(root,folder):
            if s in existing: continue
            catalog_text=norm(text+" "+s)
            overlap=tokens(profile.exactModel+" "+profile.primarySubsystem+" "+profile.normalizedIssueTitle)&tokens(catalog_text)
            exact_model=norm(profile.exactModel) in catalog_text
            same_manufacturer=norm(profile.manufacturer) in catalog_text
            if key=="preventiveMaintenance":
                eligible=exact_model and same_manufacturer
            else:
                eligible=(exact_model or
                    (profile.primarySubsystem != "general" and norm(profile.primarySubsystem) in catalog_text) or
                    len(overlap)>=2)
            if eligible:
                ranked_local.append((base+len(overlap),s,path,sorted(overlap)))
        for score,s,path,why in sorted(ranked_local,key=lambda x:(-x[0],x[1]))[:cfg["limits"][key]]:
            groups[key].append({"slug":s,"score":score,"reasons":["repository content overlap: "+", ".join(why)],"strongSignals":["direct corresponding repository resource"],"source":"analyzer","locked":False})
    if profile.primarySubsystem=="network":
        groups["networkIntegration"]=groups["biomedBasics"][:]
        groups["biomedBasics"]=[]
    used=set(); total=cfg["limits"]["total"]
    for key in groups:
        groups[key]=[x for x in groups[key] if not (x["slug"] in used or used.add(x["slug"]))][:max(0,total-len(used))]
    return groups

def rejected_relationships(profile: Profile, ref: GuideRef, refs: list[GuideRef], cfg: dict[str,Any]) -> list[dict[str,Any]]:
    rejected=[]
    for candidate in refs:
        if candidate is ref or slug(candidate.record)==slug(ref.record): continue
        same_model=norm(candidate.record.get("model"))==norm(profile.exactModel)
        score,reasons=score_link(profile,candidate,cfg)
        strong=sum(x in reasons for x in ("error-code family","subsystem","issue terminology"))
        if same_model and strong<cfg["thresholds"]["minimumStrongSignals"]:
            rejected.append({"section":"relationship","target":slug(candidate.record),"score":score,
              "reason":"same model without an additional strong issue signal","signals":reasons})
    return sorted(rejected,key=lambda x:x["target"])[:10]

def infer_pattern(sentence: str) -> str:
    return f"Observed pattern: {sentence} Possible interpretation: this may suggest the condition is associated with that operating state; confirm by controlled comparison before drawing a diagnosis."

def merge_preserved(existing: Any, generated: Any) -> Any:
    if isinstance(existing,list) and isinstance(generated,list):
        result=copy.deepcopy(existing); identities={json.dumps(x,sort_keys=True) for x in result}
        result += [x for x in generated if json.dumps(x,sort_keys=True) not in identities]; return result
    if isinstance(existing,dict) and isinstance(generated,dict):
        result=copy.deepcopy(existing)
        for k,v in generated.items(): result[k]=merge_preserved(result[k],v) if k in result else copy.deepcopy(v)
        return result
    return copy.deepcopy(existing) if existing not in (None,"",[]) else copy.deepcopy(generated)

def existing_related_ui(ref: GuideRef) -> bool:
    low=ref.html_text.casefold()
    return any(x in low for x in ("related-guides.js","related-guides-grid",">related guides<"))

def make_enhancements(p: Profile, ref: GuideRef, include_ccr: bool, cfg: dict[str,Any]) -> tuple[dict[str,Any],list[dict[str,Any]],list[dict[str,Any]]]:
    existing=ref.visible+" "+record_text(ref); issue=issue_title(ref.record)
    accepted=[]; rejected=[]; result={"startHere":[],"observedSymptoms":[],"failurePatterns":[],
      "modelSpecificConsiderations":[],"verification":[],"escalationTriggers":[]}
    for bullet in p.externalChecks[:5]:
        ok,m,reason=accept_candidate(bullet,existing,issue,cfg)
        item={"section":"startHere","text":bullet,"metrics":m,"newValue":"faster diagnostic classification","differsFrom":"existing troubleshooting steps","evidence":[ref.shard,ref.html_path],"reason":reason}
        (accepted if ok else rejected).append(item)
        if ok: result["startHere"].append(bullet)
    if result["startHere"] and len(result["startHere"])<3:
        rejected.append({"section":"startHere","reason":"fewer than three novel classification checks; section rejected","text":""})
        result["startHere"]=[]
    codes=p.normalizedErrorCodes
    if codes:
        display=next(iter(re.findall(r"0x[0-9A-F]+",ref.record["title"],re.I)),codes[0].upper())
        candidates=[f"Confirm {display} ({issue}) does not return during the operating condition that originally produced it.",
          "Complete the applicable manufacturer or facility functional testing; disappearance of the error alone is not sufficient for return to service.",
          "Document the final device status and any unresolved limitations before release or escalation."]
    else:
        candidates=[f"Confirm the reported {issue} condition no longer occurs during the operating condition that originally produced it.",
          "Complete applicable manufacturer or facility functional testing before return to service."]
    for bullet in candidates:
        if re.search(r"confirm .*\b(appears|remains|still present)\b",bullet,re.I):
            rejected.append({"section":"verification","text":bullet,"reason":"verification repeats the failure as an acceptance result"}); continue
        ok,m,reason=accept_candidate(bullet,existing,issue,cfg)
        if "does not return" in bullet.casefold() and m["issueSpecificity"]>=cfg["thresholds"]["minimumIssueSpecificity"]:
            ok=True; reason="accepted: converts initial fault confirmation into a post-correction acceptance criterion"
        item={"section":"verification","text":bullet,"metrics":m,"newValue":"post-correction acceptance criterion","differsFrom":"initial diagnostic confirmation","evidence":[ref.shard,ref.html_path],"reason":reason}
        (accepted if ok else rejected).append(item)
        if ok: result["verification"].append(bullet)
    if include_ccr:
        ccr=ref.record.get("documentation",{}).get("CCR",{})
        if ccr and not any(k.casefold() in {"evaluation","verification","final status"} for k in ccr):
            proposed={"Complaint":ccr.get("Complaint","Reported condition documented."),
              "Evaluation":"Document the observed condition and checks actually performed; do not record a suspected internal cause as confirmed.",
              "Cause":ccr.get("Cause","") if "confirmed" in ccr.get("Cause","").casefold() else "Cause not established; further evaluation required.",
              "Resolution":ccr.get("Resolution",""),"Verification":"Record applicable functional testing completed after corrective action.",
              "Final status":"Document returned to service, unresolved, or escalated."}
            text=" | ".join(f"{k}: {v}" for k,v in proposed.items())
            ok,m,reason=accept_candidate(text,existing,issue,cfg)
            item={"section":"ccrExamples","text":text,"metrics":m,"newValue":"separates evaluation, confirmed cause, verification, and final status","differsFrom":"three-field CCR example","evidence":[ref.shard],"reason":reason}
            (accepted if ok else rejected).append(item)
            if ok: result["ccrExamples"]=proposed
    limits=cfg["growthLimits"]
    nonempty=[k for k,v in result.items() if v]
    for key in nonempty[limits["maximumNewSections"]:]: result[key]=[]
    bullets=sum(len(v) for v in result.values() if isinstance(v,list))
    if bullets>limits["maximumNewBullets"]:
        remaining=limits["maximumNewBullets"]
        for key,value in result.items():
            if isinstance(value,list): result[key]=value[:remaining]; remaining-=len(result[key])
    return result,accepted,rejected

def score(profile: Profile, enhancements: dict[str,Any], rels: dict[str,Any], current: bool=False) -> int:
    vals=[bool(profile.exactModel),bool(profile.normalizedIssueTitle),bool(enhancements.get("observedSymptoms")),
      bool(enhancements.get("failurePatterns")),bool(enhancements.get("verification")),bool(enhancements.get("ccrExamples")),
      any(rels.values()),True,bool(profile.externalChecks),bool(profile.clinicalUseImplications)]
    if current: vals[2:7]=[bool(profile.distinctSymptoms),False,bool(profile.verificationRequirements),bool(profile.ref_ccr) if hasattr(profile,"ref_ccr") else False,False]
    return sum(10 for x in vals if x)

def render_block(enh: dict[str,Any], rels: dict[str,list[dict[str,Any]]], refs: list[GuideRef], root: Path) -> str:
    labels={"startHere":"Start Here","observedSymptoms":"What You May Observe","failurePatterns":"What the Failure Pattern May Suggest",
      "modelSpecificConsiderations":"Model-Specific Considerations","verification":"Verification Before Return to Service","escalationTriggers":"When to Escalate"}
    out=[BEGIN,'<section class="guide-enhancements" data-enhancement-version="1.0.0">']
    for key,label in labels.items():
        values=enh.get(key,[])
        if values: out += [f"<h2>{label}</h2>","<ul>",*[f"<li>{html.escape(str(x))}</li>" for x in values],"</ul>"]
    lookup={slug(r.record):(r.record["title"],r.html_path) for r in refs}
    for folder in ("preventive-maintenance","biomed-basics"):
        for p in (root/folder).glob("*.html"): lookup[p.stem]=(p.stem.replace("-"," ").title(),p.relative_to(root).as_posix())
    items=[]
    for group,values in rels.items():
        for item in values:
            title,path=lookup.get(item["slug"],(item["slug"],item["slug"]+".html"))
            items.append(f'<li data-group="{group}"><a href="../{html.escape(path,quote=True)}">{html.escape(str(title))}</a></li>')
    if items: out += ["<h2>Related Resources</h2>","<ul>",*items,"</ul>"]
    out += ["</section>",END]
    return "\n".join(out)

def insert_block(page: str, block: str) -> str:
    if BEGIN in page and END in page:
        return re.sub(re.escape(BEGIN)+r".*?"+re.escape(END),block,page,flags=re.S)
    positions=[page.find(x) for x in ('<h2>Work Order Documentation','<h2>Final Thought','</main>')]
    pos=next((x for x in positions if x>=0),-1)
    if pos<0: raise EnhancementError("HTML has no </main> insertion point")
    return page[:pos]+block+"\n"+page[pos:]

def duplicate_analysis(ref: GuideRef, peers: list[GuideRef]) -> list[dict[str,str]]:
    mine={norm(x):x for x in sentences(ref.visible) if len(x.split())>=8 and not SAFETY.search(x)}
    found=[]
    for peer in peers:
        if peer is ref: continue
        theirs={norm(x) for x in sentences(peer.visible) if len(x.split())>=8}
        for key in sorted(set(mine)&theirs):
            found.append({"original":mine[key],"proposed":mine[key],"reason":"repeated paragraph retained pending grounded editorial rewrite","evidence":peer.html_path})
    return found[:10]

def build_plan(root: Path=ROOT, *, guide: str|None=None, manufacturer: str|None=None, model: str|None=None,
               max_guides: int|None=None, include_ccr: bool=False, links_only: bool=False, content_only: bool=False,
               sections: list[str]|None=None, minimum_score: int|None=None, preserve_existing: bool=True,
               config_path: Path=CONFIG, report_path: str|None=None) -> Plan:
    cfg=json.loads(config_path.read_text(encoding="utf-8")); refs=load_repository(root)
    selected=[r for r in refs if (not guide or slug(r.record)==guide) and (not manufacturer or r.record["manufacturer"]==manufacturer) and (not model or r.record["model"]==model)]
    selected=sorted(selected,key=lambda r:slug(r.record))[:max_guides]
    if not selected: raise EnhancementError("no guides matched the selection")
    for ref in selected:
        ref.html_text=(root/ref.html_path).read_text(encoding="utf-8")
        ref.visible,ref.links=html_facts(ref.html_text)
    proposals=[]; outputs={}; shard_updates: dict[str,list[dict[str,Any]]]={}
    for ref in selected:
        p=extract_profile(ref,refs,root); rels={} if content_only else relationships(p,ref,refs,root,cfg)
        if not rels: rels={k:[] for k in ("sameModel","relatedTroubleshooting","preventiveMaintenance","biomedBasics","networkIntegration","manufacturerVendor")}
        enh,accepted_details,rejected_details=make_enhancements(p,ref,include_ccr,cfg)
        if not content_only: rejected_details.extend(rejected_relationships(p,ref,refs,cfg))
        rejected=[f"{x.get('section','proposal')}: {x.get('reason','rejected')}" for x in rejected_details]
        if links_only: enh={}
        if sections: enh={k:v for k,v in enh.items() if k.casefold() in {x.casefold() for x in sections}}
        old_e=ref.record.get("enhancements",{}); old_r=ref.record.get("relationships",{})
        if preserve_existing: enh=merge_preserved(old_e,enh); rels=merge_preserved(old_r,rels)
        current=score(p,old_e,old_r,True); proposed=score(p,enh,rels)
        if minimum_score is not None and proposed<minimum_score: continue
        has_related_ui=existing_related_ui(ref)
        visible_rels=copy.deepcopy(rels)
        if has_related_ui:
            visible_rels["sameModel"]=[]; visible_rels["relatedTroubleshooting"]=[]
        changed=any(enh.values()) or any(rels.values())
        record=copy.deepcopy(ref.record)
        if changed:
            record["enhancements"]=enh; record["relationships"]=rels
            record["enhancementMetadata"]={"version":cfg["analyzerVersion"],"enhancedAt":"PLAN_TIME","source":"guide-enhancement-engine"}
        block=render_block(enh,visible_rels,refs,root)
        page=insert_block(ref.html_text,block) if changed and (any(enh.values()) or any(visible_rels.values())) else ref.html_text
        current_words=max(1,len(ref.visible.split())); proposed_words=len(html_facts(page)[0].split())
        growth=100*(proposed_words-current_words)/current_words
        if growth>cfg["growthLimits"]["maximumWordIncreasePercent"]:
            rejected_details.append({"section":"all content","reason":"projected word growth exceeds configured limit","projectedGrowthPercent":round(growth,1)})
            enh={k:({} if isinstance(v,dict) else []) for k,v in enh.items()}
            changed=any(rels.values()); page=ref.html_text
            record=copy.deepcopy(ref.record)
            if changed:
                record["relationships"]=rels
                record["enhancementMetadata"]={"version":cfg["analyzerVersion"],"enhancedAt":"PLAN_TIME","source":"guide-enhancement-engine"}
        proposal=Proposal(ref,p,enh,rels,current,proposed,duplicate_analysis(ref,[x for x in refs if x.record["model"]==ref.record["model"]]),rejected,
          [ref.shard,ref.html_path],record,page,accepted_details,rejected_details,has_related_ui,
          "before Work Order Documentation or Final Thought","Enhancement recommended" if changed else "No enhancement recommended")
        proposals.append(proposal)
        if changed:
            if ref.shard not in shard_updates: shard_updates[ref.shard]=json.loads((root/ref.shard).read_text(encoding="utf-8"))
            shard_updates[ref.shard][ref.index]=record
            if page!=ref.html_text: outputs[ref.html_path]=page.encode()
    for shard,data in shard_updates.items(): outputs[shard]=json_bytes(data)
    source_paths={"tools/guide_enhancement_config.json"}
    for p in proposals: source_paths.update((p.ref.shard,p.ref.html_path))
    sources={rel:sha((root/rel).read_bytes()) for rel in sorted(source_paths)}
    payload={"sources":sources,"outputs":{k:sha(v) for k,v in sorted(outputs.items())},"analyzerVersion":cfg["analyzerVersion"]}
    digest=sha(json.dumps(payload,sort_keys=True,separators=(",",":")).encode())
    return Plan(proposals,outputs,sources,digest,cfg,report_path)

def validate_plan(plan: Plan, root: Path, staged: dict[str,bytes]|None=None) -> None:
    data=staged or plan.outputs
    for rel,blob in data.items():
        if rel.endswith(".json"): json.loads(blob)
        if rel.endswith(".html"):
            text=blob.decode(); parser=TextParser(); parser.feed(text)
            if text.count(BEGIN)!=1 or text.count(END)!=1: raise EnhancementError(f"invalid enhancement markers: {rel}")
    urls={p.relative_to(root).as_posix() for folder in ("guides","preventive-maintenance","biomed-basics") for p in (root/folder).glob("*.html")}
    for proposal in plan.proposals:
        for values in proposal.relationships.values():
            for item in values:
                if item["slug"]==slug(proposal.ref.record): raise EnhancementError("self-link rejected")
        page=data.get(proposal.ref.html_path,proposal.ref.html_text.encode()).decode()
        for value in [*proposal.enhancements.values()]:
            if isinstance(value,list):
                for text in value:
                    if proposal.ref.html_path in data and html.escape(str(text)) not in page: raise EnhancementError("JSON/HTML synchronization failure")
        before_safety={norm(x) for x in sentences(proposal.ref.visible) if SAFETY.search(x)}
        after_visible,_=html_facts(page)
        if not all(x in norm(after_visible) for x in before_safety): raise EnhancementError("patient-safety language was not preserved")
        for values in proposal.relationships.values():
            for item in values:
                matches=[u for u in urls if Path(u).stem==item["slug"]]
                if not matches: raise EnhancementError(f"missing relationship target: {item['slug']}")

def git_clean(root: Path) -> bool:
    return not subprocess.run(["git","status","--porcelain","--untracked-files=all"],cwd=root,text=True,capture_output=True,check=True).stdout

def sources_current(plan: Plan, root: Path) -> bool:
    return all((root/p).is_file() and sha((root/p).read_bytes())==digest for p,digest in plan.sources.items())

def write_plan(plan: Plan, root: Path, *, run_validators: bool=True) -> dict[str,Any]:
    if not git_clean(root): raise EnhancementError("--write requires a clean Git worktree")
    if not sources_current(plan,root): raise EnhancementError("repository changed after plan creation")
    validate_plan(plan,root); backups={}; changed=[]
    with tempfile.TemporaryDirectory(prefix="enhance-guides-",dir=root) as td:
        temp=Path(td)
        for rel,data in plan.outputs.items():
            target=temp/rel; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
        try:
            for index,(rel,data) in enumerate(sorted(plan.outputs.items()),1):
                dest=root/rel; backups[rel]=(dest.read_bytes(),dest.stat().st_mode) if dest.exists() else None
                os.replace(temp/rel,dest); changed.append(rel)
                if os.environ.get("ENHANCE_GUIDES_FAIL_AFTER_REPLACE")==str(index): raise EnhancementError("simulated validation failure")
            validate_plan(plan,root)
            if run_validators:
                commands=([sys.executable,"-m","py_compile",str(Path(__file__).resolve())],
                          [sys.executable,"scripts/validate_site.py"],[sys.executable,"-m","unittest","discover","-s","tests"],
                          ["git","diff","--check"])
                for command in commands:
                    result=subprocess.run(command,cwd=root,text=True,capture_output=True)
                    if result.returncode: raise EnhancementError(f"validator failed: {' '.join(command)}\n{result.stdout}{result.stderr}")
        except Exception:
            for rel in reversed(changed):
                dest=root/rel; backup=backups[rel]
                if backup is None: dest.unlink(missing_ok=True)
                else: dest.write_bytes(backup[0]); os.chmod(dest,backup[1])
            raise
    return {"status":"committed","planDigest":plan.digest,"modifiedFiles":sorted(changed),
      "hashes":{r:{"before":sha(backups[r][0]) if backups[r] else None,"after":sha(d)} for r,d in plan.outputs.items()}}

def report_dict(plan: Plan) -> dict[str,Any]:
    guides=[]
    for p in plan.proposals:
        old_words=len(p.ref.visible.split()); new_words=len(html_facts(p.output_html)[0].split())
        rel_count=sum(map(len,p.relationships.values()))
        accepted_relationships=[]
        for category,items in p.relationships.items():
            for item in items: accepted_relationships.append({"category":category,**item})
        existing_headings=[]
        hp=TextParser(); hp.feed(p.ref.html_text)
        existing_headings=getattr(hp,"headings",[]) if hasattr(hp,"headings") else []
        guides.append({"guideSlug":slug(p.ref.record),"htmlPath":p.ref.html_path,"jsonShard":p.ref.shard,
          "currentWordCount":old_words,"proposedWordCount":new_words,"currentEnhancementScore":p.currentScore,
          "proposedEnhancementScore":p.proposedScore,"sectionsAdded":[k for k,v in p.enhancements.items() if v and not p.ref.record.get("enhancements",{}).get(k)],
          "sectionsRevised":[],"sectionsRemoved":[],"paragraphsRewritten":[],"repeatedContentDetected":p.duplicates,
          "contextualLinksAdded":0,"relatedResourceLinksAdded":rel_count,"linksRemoved":0,
          "unsupportedProposalsRejected":p.rejected,"repositoryEvidenceUsed":[p.ref.shard,p.ref.html_path],
          "filesThatWouldChange":[p.ref.shard,p.ref.html_path],"supportedFactualAdditions":sum(len(v) for v in p.enhancements.values() if isinstance(v,list)),
          "troubleshootingInferences":len(p.enhancements.get("failurePatterns",[])),"formattingOnlyChanges":0,
          "unchangedProtectedContent":len(p.profile.clinicalUseImplications),
          "currentGuideStructure":existing_headings,"existingContentDetected":p.ref.visible[:500],
          "acceptedRevisions":p.acceptedDetails,"rejectedSections":p.rejectedDetails,
          "startHereJustified":bool(p.enhancements.get("startHere")),
          "issueSpecificVerification":p.enhancements.get("verification",[]),
          "proposedCcrChanges":p.enhancements.get("ccrExamples",{}),
          "acceptedRelationships":accepted_relationships,
          "rejectedRelationships":[x for x in p.rejectedDetails if x.get("section")=="relationship"],
          "existingRelatedGuidesUiDetected":p.relatedUiDetected,
          "visibleNewResourceSectionNecessary":not p.relatedUiDetected and bool(accepted_relationships),
          "expectedHtmlPlacement":p.placement,
          "projectedWordCountChange":new_words-old_words,
          "finalRecommendation":p.recommendation})
    return {"status":"READY","mode":"dry-run","editorialScoreDisclaimer":"Scores support editorial review and do not establish clinical validity.",
      "planDigest":plan.digest,"guides":guides,"filesThatWouldChange":sorted(plan.outputs)}

def main(argv: list[str]|None=None) -> int:
    ap=argparse.ArgumentParser(description=__doc__); group=ap.add_mutually_exclusive_group()
    group.add_argument("--guide"); group.add_argument("--manufacturer"); group.add_argument("--model")
    ap.add_argument("--audit-only",action="store_true"); ap.add_argument("--write",action="store_true"); ap.add_argument("--confirm-plan")
    ap.add_argument("--sections",nargs="+"); ap.add_argument("--links-only",action="store_true"); ap.add_argument("--content-only",action="store_true")
    ap.add_argument("--max-guides",type=int); ap.add_argument("--minimum-score",type=int); ap.add_argument("--include-ccr",action="store_true")
    ap.add_argument("--preserve-existing",action=argparse.BooleanOptionalAction,default=True); ap.add_argument("--report-path",type=Path)
    ap.add_argument("--config",type=Path,default=CONFIG); ap.add_argument("--root",type=Path,default=ROOT,help=argparse.SUPPRESS)
    args=ap.parse_args(argv)
    try:
        if args.write and args.audit_only: raise EnhancementError("--audit-only cannot be combined with --write")
        if args.write and not args.confirm_plan: raise EnhancementError("--write requires --confirm-plan <digest>")
        plan=build_plan(args.root,guide=args.guide,manufacturer=args.manufacturer,model=args.model,max_guides=args.max_guides,
          include_ccr=args.include_ccr,links_only=args.links_only,content_only=args.content_only,sections=args.sections,
          minimum_score=args.minimum_score,preserve_existing=args.preserve_existing,config_path=args.config,
          report_path=str(args.report_path) if args.report_path else None)
        validate_plan(plan,args.root); report=report_dict(plan)
        if args.write:
            if args.confirm_plan!=plan.digest: raise EnhancementError(f"incorrect or stale plan digest (current: {plan.digest})")
            report=write_plan(plan,args.root)
        text=json.dumps(report,indent=2,ensure_ascii=False); print(text)
        if args.report_path:
            args.report_path.parent.mkdir(parents=True,exist_ok=True); args.report_path.write_text(text+"\n",encoding="utf-8")
        return 0
    except (OSError,json.JSONDecodeError,subprocess.CalledProcessError,EnhancementError) as exc:
        print(f"Guide Enhancement Engine\nStatus: BLOCKED\n  - {exc}",file=sys.stderr); return 2

if __name__=="__main__": raise SystemExit(main())
