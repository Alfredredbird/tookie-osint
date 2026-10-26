"""
Regression tests for loading the site list before a scan.

A -U file with more than one username used to skip both site-loading
branches in brib.py, so the scan crashed with NameError before the first
request. These tests stay offline: scan_site is replaced before brib runs.
"""
import json
import os
import runpy
import sys
import tempfile
import textwrap
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.modules import load_sites, load_sites_for_scan


ROOT = os.path.dirname(os.path.abspath(__file__))


class LoadSitesForScanTests(unittest.TestCase):
    def test_multiple_users_load_the_full_list_without_restore(self):
        def refuse_restore():
            raise AssertionError("restore must not run for a multi-user scan")

        with patch("modules.modules.load_sites", return_value=["full"]) as load:
            sites = load_sites_for_scan(2, False, restore_loader=refuse_restore)

        self.assertEqual(sites, ["full"])
        load.assert_called_once_with(False)

    def test_single_user_resumes_from_the_restore_point(self):
        with patch("modules.modules.load_sites", return_value=["rest"]) as load:
            sites = load_sites_for_scan(
                1, False, restore_loader=lambda: "https://example.com/u/"
            )

        self.assertEqual(sites, ["rest"])
        load.assert_called_once_with(False, "https://example.com/u/")

    def test_skiprestore_loads_the_full_list(self):
        def refuse_restore():
            raise AssertionError("restore must not run when --skiprestore is set")

        with patch("modules.modules.load_sites", return_value=["full"]) as load:
            sites = load_sites_for_scan(1, True, restore_loader=refuse_restore)

        self.assertEqual(sites, ["full"])
        load.assert_called_once_with(False)

    def test_userfile_scan_reaches_every_site(self):
        with open(os.path.join(ROOT, "sites", "sites.json"), encoding="utf-8") as f:
            site_count = len(json.load(f))

        with tempfile.TemporaryDirectory() as work:
            with open(os.path.join(work, "users.txt"), "w", encoding="utf-8") as f:
                f.write("alpha\nbeta\n")

            runner = textwrap.dedent(
                """
                import os
                import sys

                sys.path.insert(0, os.environ["REPO"])
                os.chdir(os.environ["WORKDIR"])

                import modules.modules as mods

                def fake_scan(*args, **kwargs):
                    with open("scanned", "a", encoding="utf-8") as out:
                        out.write("1\\n")
                    return None

                mods.scan_site = fake_scan
                sys.argv = [
                    "brib.py",
                    "-U",
                    "users.txt",
                    "--script",
                    "--skipheaders",
                    "-t",
                    "2",
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
            self.assertEqual(
                completed.returncode,
                0,
                completed.stderr or completed.stdout,
            )
            with open(os.path.join(work, "scanned"), encoding="utf-8") as f:
                scanned = len(f.readlines())
            self.assertEqual(scanned, site_count * 2)
            # load_sites is still the real one; this guards the assertion above
            self.assertGreater(len(load_sites()), 0)


if __name__ == "__main__":
    unittest.main()
