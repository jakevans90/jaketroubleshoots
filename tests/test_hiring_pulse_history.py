import copy
import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("build_hiring_pulse_history", ROOT / "tools" / "build_hiring_pulse_history.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class HiringPulseHistoryTests(unittest.TestCase):
    def test_current_history_matches_validated_records(self):
        self.assertTrue(MODULE.build(ROOT, check=True))
        history = MODULE.public.pulse.load_json(ROOT / MODULE.HISTORY_PATH)
        self.assertEqual(1, history["schemaVersion"])
        self.assertEqual(len(history["weeks"]), len({item["weekStart"] for item in history["weeks"]}))

    def test_same_week_updates_only_latest_week(self):
        entry = {"weekStart": "2026-11-23", "observedAt": "2026-11-24T12:00:00Z", "trackedPostings": 10}
        history = {"schemaVersion": 1, "weeks": []}
        MODULE.update_history(history, copy.deepcopy(entry))
        newer = {**entry, "observedAt": "2026-11-25T12:00:00Z", "trackedPostings": 11}
        MODULE.update_history(history, newer)
        self.assertEqual([newer], history["weeks"])
        with self.assertRaises(ValueError):
            MODULE.update_history(history, entry)

    def test_past_week_is_frozen_and_future_week_appends(self):
        first = {"weekStart": "2026-11-23", "observedAt": "2026-11-24T12:00:00Z"}
        later = {"weekStart": "2026-11-30", "observedAt": "2026-12-01T12:00:00Z"}
        history = {"schemaVersion": 1, "weeks": [first]}
        MODULE.update_history(history, later)
        self.assertEqual([first, later], history["weeks"])
        with self.assertRaises(ValueError):
            MODULE.update_history(history, first)

    def test_counts_new_openings_even_when_closed(self):
        snapshot = MODULE.public.pulse.load_json(ROOT / MODULE.public.PUBLIC_PATH)
        store = MODULE.public.pulse.load_store(ROOT)
        summary = MODULE.summarize(snapshot, store)
        expected = sum(
            item.get("first_seen") is not None and MODULE.week_start(item["first_seen"]) == summary["weekStart"]
            for item in store["postings"]["records"]
        )
        self.assertEqual(expected, summary["newlyObservedPostings"])


if __name__ == "__main__":
    unittest.main()
