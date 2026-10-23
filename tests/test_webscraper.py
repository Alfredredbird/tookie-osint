import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from modules import webscraper


class ExtractFieldsTests(unittest.TestCase):
    @patch("modules.webscraper.WebDriverWait")
    def test_returns_configured_attribute_instead_of_visible_text(self, wait):
        element = Mock(text="Synthetic visible text")
        element.get_attribute.return_value = "https://fixture.invalid/avatar.png"
        wait.return_value.until.return_value = element

        result = webscraper.extract_fields(
            object(),
            {"avatar": {"by": "css", "selector": "img", "attr": "src"}},
        )

        self.assertEqual(result, {"avatar": "https://fixture.invalid/avatar.png"})
        element.get_attribute.assert_called_once_with("src")

    @patch("modules.webscraper.WebDriverWait")
    def test_returns_visible_text_when_no_attribute_is_configured(self, wait):
        element = SimpleNamespace(text="  Synthetic visible text  ")
        wait.return_value.until.return_value = element

        result = webscraper.extract_fields(
            object(), {"name": {"by": "css", "selector": "h1"}}
        )

        self.assertEqual(result, {"name": "Synthetic visible text"})


if __name__ == "__main__":
    unittest.main()
