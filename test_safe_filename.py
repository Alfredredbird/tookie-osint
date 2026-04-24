"""
Regression tests for the filename sanitization added to modules/modules.py.
Ensures a caller-supplied username cannot steer output writes outside the
current working directory via path-traversal or absolute-path inputs.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.modules import _safe_filename, write_txt, write_csv, write_json


class SafeFilenameTests(unittest.TestCase):
    def test_traversal_is_collapsed(self):
        self.assertNotIn("/", _safe_filename("../../../tmp/pwn"))
        self.assertNotIn("..", _safe_filename("../../../tmp/pwn"))

    def test_absolute_path_is_neutralised(self):
        self.assertNotIn("/", _safe_filename("/etc/passwd"))

    def test_control_characters_are_stripped(self):
        self.assertNotIn("\x1b", _safe_filename("osc\x1b]0;X\x07"))
        self.assertNotIn("\x07", _safe_filename("osc\x1b]0;X\x07"))

    def test_empty_input_yields_default(self):
        self.assertEqual(_safe_filename(""), "output")

    def test_ordinary_username_is_unchanged(self):
        self.assertEqual(_safe_filename("alfred"), "alfred")
        self.assertEqual(_safe_filename("a.b-c_d.1"), "a.b-c_d.1")

    def test_writers_do_not_escape_cwd(self):
        for writer, ext in [(write_txt, "txt"), (write_csv, "csv"), (write_json, "json")]:
            with tempfile.TemporaryDirectory() as d:
                cwd = os.getcwd()
                try:
                    os.chdir(d)
                    writer("../escaped", [{"found": True, "url": "x", "status": 200}])
                    parent = os.path.dirname(d)
                    self.assertFalse(
                        any(name.startswith("escaped.") for name in os.listdir(parent)),
                        f"{writer.__name__} wrote outside CWD into {parent}",
                    )
                    self.assertTrue(
                        any(name.endswith("." + ext) for name in os.listdir(d)),
                        f"{writer.__name__} did not produce a file in CWD",
                    )
                finally:
                    os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
