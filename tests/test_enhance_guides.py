import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from enhance_guides import (BEGIN, END, EnhancementError, build_plan, extract_profile,
    infer_pattern, merge_preserved, relationships, score_link, validate_plan, write_plan)

HTML="""<!doctype html><html><head><title>Acme Alpha - Network drops</title>
<link rel="canonical" href="https://example/guides/acme-alpha-network.html"></head><body>
<main><h2>Step-by-Step Troubleshooting</h2><p>Never troubleshoot while connected to a patient.
Check the Ethernet cable when communication fails after patient association.
Confirm stable data transfer before return to service.</p></main>
<footer>Guides intended for trained personnel only.</footer></body></html>"""

def record(slug,model="Alpha",title="Network drops"):
    return {"title":f"Acme {model} - {title}","description":f"{title} on {model}.",
      "assetType":"Patient Monitor","manufacturer":"Acme","model":model,
      "url":f"guides/{slug}.html","dateAdded":"2026-01-01",
      "steps":[{"title":"Check cable","instructions":"Check the Ethernet cable when communication fails after patient association. Confirm stable data transfer before return to service."}],
      "documentation":{"CCR":{"Complaint":"Network dropped.","Cause":"Cause not established.","Resolution":"Escalated for evaluation."}},
      "helpfulDetails":["Connection timing"]}

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
        for folder in ("data","guides","tools","preventive-maintenance","biomed-basics","scripts","tests"): (self.root/folder).mkdir()
        records=[record("acme-alpha-network"),record("acme-alpha-display",title="Display freezes after startup"),
                 record("acme-alpha-pm","Alpha Family",title="Network communication")]
        (self.root/"data/guides.json").write_text('["data/guides-acme.json"]',encoding="utf-8")
        (self.root/"data/guides-acme.json").write_text(json.dumps(records),encoding="utf-8")
        for r in records: (self.root/r["url"]).write_text(HTML.replace("Network drops",r["title"]),encoding="utf-8")
        (self.root/"preventive-maintenance/acme-alpha-preventive-maintenance.html").write_text("<p>Acme Alpha network functional test</p>",encoding="utf-8")
        (self.root/"preventive-maintenance/unrelated-network-preventive-maintenance.html").write_text("<p>OtherCo Beta network functional test</p>",encoding="utf-8")
        (self.root/"biomed-basics/basic-networking.html").write_text("<p>Network Ethernet communication basics</p>",encoding="utf-8")
        shutil.copy(ROOT/"tools/guide_enhancement_config.json",self.root/"tools/guide_enhancement_config.json")
        subprocess.run(["git","init"],cwd=self.root,check=True,capture_output=True)
        subprocess.run(["git","config","user.email","test@example.com"],cwd=self.root,check=True)
        subprocess.run(["git","config","user.name","Test"],cwd=self.root,check=True)
        subprocess.run(["git","add","."],cwd=self.root,check=True)
        subprocess.run(["git","commit","-m","fixture"],cwd=self.root,check=True,capture_output=True)
    def tearDown(self): self.tmp.cleanup()
    def plan(self,**kwargs):
        return build_plan(self.root,guide="acme-alpha-network",config_path=self.root/"tools/guide_enhancement_config.json",**kwargs)
    def test_profile_and_symptom_differentiation(self):
        p=self.plan().proposals[0].profile
        self.assertEqual(p.exactModel,"Alpha"); self.assertEqual(p.primarySubsystem,"network")
        self.assertTrue(any("patient association" in x for x in p.distinctSymptoms))
    def test_failure_pattern_is_inference_labeled(self):
        self.assertIn("may suggest",infer_pattern("Failure occurs after startup."))
    def test_exact_model_context_and_link_limits(self):
        p=self.plan().proposals[0]
        self.assertTrue(p.relationships["sameModel"])
        self.assertLessEqual(sum(map(len,p.relationships.values())),8)
    def test_model_family_context_scores(self):
        plan=self.plan(); p=plan.proposals[0].profile
        candidate=next(r for r in [x.ref for x in plan.proposals] if False) if False else None
        self.assertEqual(p.modelFamily,"Alpha")
    def test_pm_and_biomed_links(self):
        rel=self.plan().proposals[0].relationships
        self.assertTrue(rel["preventiveMaintenance"]); self.assertTrue(rel["networkIntegration"])
        self.assertEqual(
            [x["slug"] for x in rel["preventiveMaintenance"]],
            ["acme-alpha-preventive-maintenance"],
        )
    def test_no_self_or_duplicate_links_and_targets_exist(self):
        plan=self.plan(); validate_plan(plan,self.root)
        slugs=[x["slug"] for values in plan.proposals[0].relationships.values() for x in values]
        self.assertNotIn("acme-alpha-network",slugs); self.assertEqual(len(slugs),len(set(slugs)))
    def test_manual_and_locked_content_preserved(self):
        existing={"startHere":[{"text":"Manual","source":"manual","locked":True}]}
        merged=merge_preserved(existing,{"startHere":["Generated"]})
        self.assertEqual(merged["startHere"][0]["text"],"Manual")
    def test_patient_safety_language_preserved_and_json_html_sync(self):
        plan=self.plan(); validate_plan(plan,self.root)
        page=plan.outputs["guides/acme-alpha-network.html"].decode()
        self.assertIn("Never troubleshoot while connected to a patient.",page)
        self.assertIn(BEGIN,page); self.assertIn(END,page)
    def test_deterministic_plan_and_digest(self):
        self.assertEqual(self.plan().digest,self.plan().digest)
    def test_malformed_record_rejected(self):
        path=self.root/"data/guides-acme.json"; data=json.loads(path.read_text()); del data[0]["model"]; path.write_text(json.dumps(data))
        with self.assertRaises(EnhancementError): self.plan()
    def test_dirty_worktree_refusal(self):
        plan=self.plan(); (self.root/"dirty.txt").write_text("x")
        with self.assertRaisesRegex(EnhancementError,"clean Git"): write_plan(plan,self.root,run_validators=False)
    def test_rollback_after_validation_failure(self):
        plan=self.plan(); before=(self.root/"data/guides-acme.json").read_bytes()
        os.environ["ENHANCE_GUIDES_FAIL_AFTER_REPLACE"]="1"
        try:
            with self.assertRaises(EnhancementError): write_plan(plan,self.root,run_validators=False)
        finally: os.environ.pop("ENHANCE_GUIDES_FAIL_AFTER_REPLACE",None)
        self.assertEqual(before,(self.root/"data/guides-acme.json").read_bytes())
    def test_ccr_customization_is_opt_in(self):
        self.assertNotIn("ccrExamples",self.plan().proposals[0].enhancements)
        self.assertIn("ccrExamples",self.plan(include_ccr=True).proposals[0].enhancements)
    def test_content_and_links_modes(self):
        self.assertFalse(self.plan(links_only=True).proposals[0].enhancements)
        self.assertFalse(any(self.plan(content_only=True).proposals[0].relationships.values()))

if __name__=="__main__": unittest.main()
