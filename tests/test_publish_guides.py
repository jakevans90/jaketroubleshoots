import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests"))

from publish_guides import build_batch_plan, main  # noqa: E402
from test_publish_guide import PublisherTests  # noqa: E402


class BatchPublisherTests(unittest.TestCase):
    ISSUES = [
        "Battery Runtime Low",
        "Keypad Unresponsive",
        "Display Flickers",
        "Door Latch Sticks",
        "Air Sensor Fault",
        "Network Link Lost",
        "Speaker Volume Low",
        "Occlusion Alarm",
        "Startup Self Test",
        "Power Cord Damage",
    ]

    def make_batch(self, count=10):
        helper = PublisherTests()
        temporary, root = helper.make_repository()
        incoming = root / "incoming"
        incoming.mkdir()
        base = helper.normal_input()
        for index in range(1, count + 1):
            issue = self.ISSUES[index - 1]
            slug = issue.casefold().replace(" ", "-")
            text = (
                base.replace("Error E42", issue)
                .replace("error-e42", slug)
            )
            (incoming / f"guide-{index:02d}.md").write_text(text, encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "batch inputs"], cwd=root, check=True)
        return temporary, root, incoming

    def run_main(self, root, incoming, *extra):
        output, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
            code = main([str(incoming), "--root", str(root), *extra])
        return code, output.getvalue(), error.getvalue()

    def test_successful_ten_guide_batch_combines_shard_and_sitemap(self):
        temporary, root, incoming = self.make_batch()
        with temporary:
            before = (root / "unrelated.txt").read_bytes()
            plan = build_batch_plan(incoming, root)
            self.assertFalse(plan.blocked, plan.errors)
            self.assertEqual(len(plan.guides), 10)
            self.assertEqual(list(plan.outputs).count("data/guides-acme.json"), 1)
            code, output, error = self.run_main(
                root, incoming, "--write", "--confirm-plan", plan.digest
            )
            self.assertEqual((code, error), (0, ""))
            result = json.loads(output)
            self.assertEqual(result["guideCount"], 10)
            shard = json.loads((root / "data/guides-acme.json").read_text(encoding="utf-8"))
            self.assertEqual(len(shard), 11)
            sitemap = (root / "sitemap.xml").read_text(encoding="utf-8")
            for index in range(1, 11):
                issue = self.ISSUES[index - 1]
                slug = issue.casefold().replace(" ", "-")
                self.assertEqual(sitemap.count(f"guides/acme-alpha-{slug}.html"), 1)
                page = (root / f"guides/acme-alpha-{slug}.html").read_text(encoding="utf-8")
                self.assertIn(f"Remove from patient use; do not bypass {issue}.", page)
                self.assertIn(
                    "Removed from service; return only after the E42 test passes.",
                    page,
                )
                self.assertEqual(page.count("CCR = Complaint, Cause, Resolution"), 1)
                self.assertIn(
                    "<p><strong>CCR = Complaint, Cause, Resolution</strong></p>",
                    page,
                )
                self.assertNotIn("<p>CCR = Complaint, Cause, Resolution</p>", page)
                self.assertIn(
                    f'"Staff reported {issue} during O₂ delivery."',
                    page,
                )
                self.assertIn(
                    '"The approved test found flow below 5 L/min."',
                    page,
                )
                self.assertIn(
                    '"Removed from service; return only after the E42 test passes."',
                    page,
                )
                self.assertIn(
                    "Escalate to authorized personnel. Return to service only after all tests pass.",
                    page,
                )
            self.assertEqual((root / "unrelated.txt").read_bytes(), before)

    def test_one_invalid_input_blocks_all_ten(self):
        temporary, root, incoming = self.make_batch()
        with temporary:
            invalid = incoming / "guide-05.md"
            invalid.write_text(
                invalid.read_text(encoding="utf-8").replace("## Final Thought", "## Missing"),
                encoding="utf-8",
            )
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            plan = build_batch_plan(incoming, root)
            self.assertTrue(plan.blocked)
            self.assertFalse(plan.outputs)
            code, _, _ = self.run_main(root, incoming, "--write", "--confirm-plan", plan.digest)
            self.assertEqual(code, 2)
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            self.assertEqual(after, before)

    def test_duplicate_within_batch_and_against_repository(self):
        temporary, root, incoming = self.make_batch(2)
        with temporary:
            (incoming / "guide-02.md").write_bytes((incoming / "guide-01.md").read_bytes())
            plan = build_batch_plan(incoming, root)
            self.assertTrue(any("within the batch" in error for error in plan.errors))
        temporary, root, incoming = self.make_batch(1)
        with temporary:
            path = incoming / "guide-01.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                'title: "Acme Alpha Infusion Pump - Battery Runtime Low"',
                'title: "Acme Alpha Infusion Pump - Existing"',
            ).replace('slug: "acme-alpha-battery-runtime-low"', 'slug: "acme-alpha-existing"')
            path.write_text(text, encoding="utf-8")
            plan = build_batch_plan(incoming, root)
            self.assertTrue(plan.duplicates)

    def test_incorrect_stale_and_dirty_rejection(self):
        temporary, root, incoming = self.make_batch(2)
        with temporary:
            plan = build_batch_plan(incoming, root)
            code, _, error = self.run_main(root, incoming, "--write", "--confirm-plan", "wrong")
            self.assertEqual(code, 2)
            self.assertIn("incorrect or stale", error)
            path = incoming / "guide-01.md"
            path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            code, _, error = self.run_main(root, incoming, "--write", "--confirm-plan", plan.digest)
            self.assertEqual(code, 2)
            self.assertIn("incorrect or stale", error)
            subprocess.run(["git", "checkout", "--", "."], cwd=root, check=True)
            (root / "unrelated.txt").write_text("dirty\n", encoding="utf-8")
            current = build_batch_plan(incoming, root)
            code, _, error = self.run_main(root, incoming, "--write", "--confirm-plan", current.digest)
            self.assertEqual(code, 2)
            self.assertIn("clean Git worktree", error)

    def test_complete_rollback_after_mid_transaction_failure(self):
        temporary, root, incoming = self.make_batch(3)
        with temporary:
            plan = build_batch_plan(incoming, root)
            baseline = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            os.environ["PUBLISH_GUIDES_FAIL_AFTER_REPLACE"] = "3"
            try:
                code, _, _ = self.run_main(root, incoming, "--write", "--confirm-plan", plan.digest)
            finally:
                os.environ.pop("PUBLISH_GUIDES_FAIL_AFTER_REPLACE")
            self.assertEqual(code, 2)
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            self.assertEqual(after, baseline)


if __name__ == "__main__":
    unittest.main()
