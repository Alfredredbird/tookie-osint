"""
Regression tests for username comparison.

Short names used to be stripped out of the whole HTML document, and a
percent-encoded profile URL was treated as a page that had dropped the user.
No site is requested.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.modules import _CONTROL_USER, is_found, same_response


class _Page:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code


class UsernameCheckTests(unittest.TestCase):
    def test_short_username_echo_still_matches_the_control_page(self):
        html = "<html><div class='banner'>aaaa</div><p>{name}</p></html>"
        candidate = _Page(html.format(name="a"))
        control = _Page(html.format(name=_CONTROL_USER))
        self.assertTrue(same_response(candidate, control, "a"))

    def test_different_pages_stay_different(self):
        candidate = _Page("<html><p>custom profile for a</p><p>a</p></html>")
        control = _Page("<html><p>" + _CONTROL_USER + "</p></html>")
        self.assertFalse(same_response(candidate, control, "a"))

    def test_status_mismatch_is_not_the_same_page(self):
        page = "<html><p>{name}</p></html>"
        candidate = _Page(page.format(name="alice"), status_code=200)
        control = _Page(page.format(name=_CONTROL_USER), status_code=404)
        self.assertFalse(same_response(candidate, control, "alice"))

    def test_missing_control_is_not_the_same_page(self):
        self.assertFalse(same_response(_Page("hello alice"), None, "alice"))

    def test_encoded_username_in_the_path_counts(self):
        self.assertTrue(
            is_found(
                200,
                "profile",
                "",
                "https://example.com/users/alice%20smith",
                "alice smith",
            )
        )

    def test_username_left_only_in_the_query_does_not_count(self):
        self.assertFalse(
            is_found(
                200,
                "login",
                "",
                "https://example.com/login?next=/users/alice",
                "alice",
            )
        )

    def test_plain_profile_url_still_counts(self):
        self.assertTrue(
            is_found(200, "profile", "", "https://example.com/users/alice", "alice")
        )


if __name__ == "__main__":
    unittest.main()
