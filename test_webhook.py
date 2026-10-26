"""
Regression tests for webhook notifications.

A failed post used to raise out of the scan, and an unknown type raised
UnboundLocalError because payload was never set. requests.post is stubbed.
"""
import os
import sys
import unittest
from io import StringIO
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests
from modules.files import send_webhook


class WebhookTests(unittest.TestCase):
    def test_request_failure_is_reported_and_does_not_raise(self):
        with patch(
            "modules.files.requests.post",
            side_effect=requests.ConnectionError("refused"),
        ), patch("sys.stdout", new_callable=StringIO) as out:
            ok = send_webhook("http://127.0.0.1:9/hook", "alice", "started")
        self.assertFalse(ok)
        self.assertIn("Webhook notification failed", out.getvalue())

    def test_http_error_is_reported(self):
        response = Mock(status_code=500)
        response.raise_for_status.side_effect = requests.HTTPError("500")
        with patch("modules.files.requests.post", return_value=response):
            self.assertFalse(
                send_webhook("http://example.invalid/hook", "alice", "hit", type="site")
            )

    def test_success_posts_once_with_a_timeout(self):
        response = Mock(status_code=204)
        with patch("modules.files.requests.post", return_value=response) as post:
            self.assertTrue(
                send_webhook("http://example.invalid/hook", "alice", "started")
            )
        post.assert_called_once()
        self.assertEqual(post.call_args.kwargs["timeout"], 10)

    def test_unknown_type_does_not_raise(self):
        with patch("modules.files.requests.post") as post, patch(
            "sys.stdout", new_callable=StringIO
        ) as out:
            ok = send_webhook(
                "http://example.invalid/hook", "alice", "started", type="nope"
            )
        self.assertFalse(ok)
        post.assert_not_called()
        self.assertIn("Unknown webhook type", out.getvalue())


if __name__ == "__main__":
    unittest.main()
