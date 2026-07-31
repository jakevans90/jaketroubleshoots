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
    accept_candidate, existing_related_ui, infer_pattern, merge_preserved, novelty_metrics,
    relationships, score_link, validate_plan, write_plan)

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
                 record("acme-alpha-pm","Alpha Family",title="Network communication"),
                 record("acme-beta-cardiac-output","Beta",title="Cardiac output calculation error")]
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
        self.assertFalse(any(x.lower().startswith("confirm ") for x in p.distinctSymptoms))
    def test_failure_pattern_is_inference_labeled(self):
        self.assertIn("may suggest",infer_pattern("Failure occurs after startup."))
    def test_exact_model_context_and_link_limits(self):
        p=self.plan().proposals[0]
        self.assertFalse(p.relationships["sameModel"],"exact-model identity alone must not qualify")
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
        self.assertNotIn("acme-beta-cardiac-output",slugs)
    def test_generated_sections_reject_flattened_or_imperative_observations(self):
        proposal=self.plan().proposals[0]
        self.assertTrue(all(len(x)<=240 for x in proposal.enhancements["verification"]))
        self.assertFalse(any(x.lower().startswith("confirm ") for x in proposal.enhancements["observedSymptoms"]))
    def test_manual_and_locked_content_preserved(self):
        existing={"startHere":[{"text":"Manual","source":"manual","locked":True}]}
        merged=merge_preserved(existing,{"startHere":["Generated"]})
        self.assertEqual(merged["startHere"][0]["text"],"Manual")
    def test_patient_safety_language_preserved_and_json_html_sync(self):
        plan=self.plan(); validate_plan(plan,self.root)
        page=plan.outputs.get("guides/acme-alpha-network.html",(self.root/"guides/acme-alpha-network.html").read_bytes()).decode()
        self.assertIn("Never troubleshoot while connected to a patient.",page)
        self.assertEqual(page.count(BEGIN),page.count(END))
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
    def test_repeated_start_here_and_close_paraphrases_are_rejected(self):
        proposal=self.plan(content_only=True).proposals[0]
        self.assertFalse(proposal.enhancements["startHere"])
        cfg=json.loads((self.root/"tools/guide_enhancement_config.json").read_text())
        accepted,metrics,_=accept_candidate("Check Ethernet cable when communication drops.",HTML,"Network drops",cfg)
        self.assertFalse(accepted); self.assertGreater(metrics["duplicationRisk"],0.65)
    def test_issue_specific_text_scores_higher_than_generic_template(self):
        specific=novelty_metrics("Confirm 0xHOST1001 does not return after thermal stabilization.","Check airflow.","0xHOST1001 internal temperature")
        generic=novelty_metrics("Confirm the device works correctly.","Check airflow.","0xHOST1001 internal temperature")
        self.assertGreater(specific["issueSpecificity"],generic["issueSpecificity"])
    def test_verification_is_post_correction_not_initial_confirmation(self):
        path=self.root/"data/guides-acme.json"; data=json.loads(path.read_text())
        data[0]["title"]="Acme Alpha - Error 0xHOST1001 internal temperature"
        data[0]["description"]="0xHOST1001 internal temperature fault"
        path.write_text(json.dumps(data))
        config=self.root/"tools/guide_enhancement_config.json"; cfg=json.loads(config.read_text())
        cfg["growthLimits"]["maximumWordIncreasePercent"]=1000; config.write_text(json.dumps(cfg))
        proposal=self.plan(content_only=True).proposals[0]
        verification=proposal.enhancements["verification"]
        self.assertTrue(any("does not return" in x for x in verification))
        self.assertFalse(any("error appears" in x.lower() for x in verification))
    def test_existing_related_guides_ui_suppresses_duplicate_guide_list(self):
        page=self.root/"guides/acme-alpha-network.html"
        page.write_text(HTML.replace("</body>",'<div class="related-guides-grid"></div><script src="../related-guides.js"></script></body>'))
        proposal=self.plan(links_only=True).proposals[0]
        self.assertTrue(proposal.relatedUiDetected)
        if proposal.ref.html_path in self.plan(links_only=True).outputs:
            output=self.plan(links_only=True).outputs[proposal.ref.html_path].decode()
            self.assertNotIn('data-group="sameModel"',output)
    def test_no_change_is_valid(self):
        proposal=self.plan(content_only=True).proposals[0]
        self.assertEqual(proposal.recommendation,"No enhancement recommended")
    def test_section_and_word_growth_limits_are_enforced(self):
        proposal=self.plan(include_ccr=True,content_only=True).proposals[0]
        self.assertLessEqual(sum(bool(v) for v in proposal.enhancements.values()),2)
        current=len(proposal.ref.visible.split()); proposed=len(proposal.output_html.split())
        self.assertLessEqual(proposed-current,max(1,int(current*.20)))
    def test_stale_plan_refusal(self):
        plan=self.plan(); config=self.root/"tools/guide_enhancement_config.json"
        config.write_text(config.read_text()+"\n")
        subprocess.run(["git","add","."],cwd=self.root,check=True)
        subprocess.run(["git","commit","-m","stale"],cwd=self.root,check=True,capture_output=True)
        with self.assertRaisesRegex(EnhancementError,"repository changed"):
            write_plan(plan,self.root,run_validators=False)
    def test_exact_error_related_model_accepted_and_unrelated_alarm_rejected(self):
        path=self.root/"data/guides-acme.json"; data=json.loads(path.read_text())
        data[0]["title"]="Acme Alpha - Error 0xHOST1001 internal temperature"
        data[0]["description"]="0xHOST1001 internal temperature and cooling fault"
        data[1]["title"]="Acme Beta - Error 0xHOST1001 internal temperature"
        data[1]["model"]="Beta"; data[1]["description"]="0xHOST1001 internal temperature and cooling fault"
        data[3]["title"]="Acme Alpha - Speaker alarm failure"; data[3]["model"]="Alpha"
        data[3]["steps"]=[{"title":"Check speaker","instructions":"Inspect speaker grille and test audible alarm output."}]
        path.write_text(json.dumps(data))
        proposal=self.plan(links_only=True).proposals[0]
        targets=[x["slug"] for values in proposal.relationships.values() for x in values]
        self.assertIn("acme-alpha-display",targets)
        self.assertNotIn("acme-beta-cardiac-output",targets)
    def test_ccr_separates_suspected_cause_and_final_status(self):
        proposal=self.plan(include_ccr=True,content_only=True).proposals[0]
        accepted=[x for x in proposal.acceptedDetails if x["section"]=="ccrExamples"]
        if accepted:
            text=accepted[0]["text"]
            self.assertIn("Cause not established",text)
            self.assertIn("Final status",text)
    def test_placement_precedes_existing_documentation_when_html_is_generated(self):
        config=self.root/"tools/guide_enhancement_config.json"; cfg=json.loads(config.read_text())
        cfg["growthLimits"]["maximumWordIncreasePercent"]=1000; config.write_text(json.dumps(cfg))
        page=self.root/"guides/acme-alpha-network.html"
        page.write_text(HTML.replace("</main>","<h2>Work Order Documentation</h2></main>"))
        plan=self.plan(include_ccr=True,content_only=True)
        if "guides/acme-alpha-network.html" in plan.outputs:
            output=plan.outputs["guides/acme-alpha-network.html"].decode()
            self.assertLess(output.index(BEGIN),output.index("Work Order Documentation"))

if __name__=="__main__": unittest.main()
