"""
Regression tests for web-scraper results.

scan_webscraper() used to discard check_site()'s return value, and a delay
of 0 was skipped because 0 is false. These tests stub check_site so no
browser is started and no site is requested.
"""
import os
import runpy
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.modules import record_webscraper_result, scan_webscraper


ROOT = os.path.dirname(os.path.abspath(__file__))
SITES = [
    {"site": "https://example.com/u/", "errorMessage": "missing"},
    {"site": "https://example.org/u/", "errorMessage": "missing"},
]


class WebscraperResultTests(unittest.TestCase):
    def test_hits_are_returned_and_zero_delay_is_passed(self):
        calls = []

        def fake_check(url, message, field_config=None, allsites=False, delay=2):
            calls.append((url, delay))
            return url.endswith("example.com/u/alice")

        with patch("modules.modules.check_site", fake_check), patch(
            "modules.modules.json.load", return_value=SITES
        ):
            results = scan_webscraper("alice", delay=0)

        self.assertEqual(
            calls,
            [
                ("https://example.com/u/alice", 0),
                ("https://example.org/u/alice", 0),
            ],
        )
        self.assertEqual(
            results,
            [{"url": "https://example.com/u/alice", "found": True, "status": None}],
        )

    def test_all_keeps_misses(self):
        with patch("modules.modules.check_site", return_value=False), patch(
            "modules.modules.json.load", return_value=SITES[:1]
        ):
            results = scan_webscraper("alice", allsites=True)

        self.assertEqual(
            results,
            [{"url": "https://example.com/u/alice", "found": False, "status": None}],
        )

    def test_harvest_dict_keeps_data_and_gains_status(self):
        outcome = {"found": True, "data": {"name": "alice"}}
        recorded = record_webscraper_result("https://example.com/u/alice", outcome)
        self.assertEqual(recorded["status"], None)
        self.assertEqual(recorded["data"], {"name": "alice"})
        self.assertEqual(recorded["url"], "https://example.com/u/alice")

    def test_cli_writes_the_returned_hit(self):
        with tempfile.TemporaryDirectory() as work:
            runner = textwrap.dedent(
                """
                import os
                import sys

                sys.path.insert(0, os.environ["REPO"])
                os.chdir(os.environ["WORKDIR"])

                import modules.modules as mods

                def fake_scan(*args, **kwargs):
                    return [{
                        "url": "https://example.com/u/alice",
                        "found": True,
                        "status": 200,
                    }]

                mods.scan_webscraper = fake_scan
                sys.argv = [
                    "brib.py",
                    "-u",
                    "alice",
                    "-W",
                    "--script",
                    "--skipheaders",
                    "--skiprestore",
                    "-o",
                    "json",
                ]
                import runpy
                runpy.run_path(
                    os.path.join(os.environ["REPO"], "brib.py"),
                    run_name="__main__",
                )
                """
            )
            script = os.path.join(work, "run_brib.py")
            with open(script, "w", encoding="utf-8") as f:
                f.write(runner)

            env = os.environ.copy()
            env["REPO"] = ROOT
            env["WORKDIR"] = work
            import subprocess

            completed = subprocess.run(
                [sys.executable, script],
                env=env,
                cwd=work,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
            with open(os.path.join(work, "alice.json"), encoding="utf-8") as f:
                body = f.read()
            self.assertIn("https://example.com/u/alice", body)


if __name__ == "__main__":
    unittest.main()
