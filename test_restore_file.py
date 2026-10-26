"""
Regression tests for the restore file.

A missing .tookie and a scan with no hits are normal. They used to print
an exception, and a saved site that is no longer listed aborted the scan.
"""
import os
import sys
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.files import load_restore, make_restore, use_restore_answer
from modules.modules import load_sites


class RestoreFileTests(unittest.TestCase):
    def setUp(self):
        self._cwd = os.getcwd()
        self._tmp = tempfile.TemporaryDirectory()
        os.chdir(self._tmp.name)

    def tearDown(self):
        os.chdir(self._cwd)
        self._tmp.cleanup()

    def test_missing_file_is_quiet(self):
        with patch("sys.stdout", new_callable=StringIO) as out:
            self.assertIsNone(load_restore())
        self.assertNotIn("No such file", out.getvalue())
        self.assertNotIn("Errno", out.getvalue())

    def test_empty_results_do_not_write_or_error(self):
        with patch("sys.stdout", new_callable=StringIO) as out:
            make_restore([], "alice")
        self.assertEqual(out.getvalue(), "")
        self.assertFalse(os.path.exists(".tookie"))

    def test_enter_and_yes_accept_the_prompt(self):
        self.assertTrue(use_restore_answer(""))
        self.assertTrue(use_restore_answer("Y"))
        self.assertTrue(use_restore_answer("yes"))
        self.assertFalse(use_restore_answer("n"))
        self.assertFalse(use_restore_answer("no"))

    def test_enter_uses_the_saved_url(self):
        with open(".tookie", "w", encoding="utf-8") as f:
            f.write(
                "=====Tookie-OSINT Restore File=====\n"
                "URL = https://example.com/users\n"
                "FOUND = True\n"
                "STATUS = 200\n"
            )
        with patch("builtins.input", return_value=""):
            self.assertEqual(load_restore(), "https://example.com/users")

    def test_unknown_restore_site_starts_from_the_beginning(self):
        with patch("sys.stdout", new_callable=StringIO):
            resumed = load_sites(start_site="https://not-in-the-list.example/")
            full = load_sites()
        self.assertEqual(resumed, full)
        self.assertGreater(len(resumed), 0)

    def test_known_restore_site_drops_earlier_entries(self):
        full = load_sites()
        target = full[2]["site"]
        resumed = load_sites(start_site=target)
        self.assertEqual(resumed[0]["site"], target)
        self.assertLess(len(resumed), len(full))


if __name__ == "__main__":
    unittest.main()
