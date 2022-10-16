# Disabled for testing:
# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint: disable=too-many-public-methods

from unittest.mock import patch
from django.test import TestCase, override_settings
from django.urls import reverse


class YewtailTests(TestCase):
    @patch("some_module")
    def test_something(self, mock):
        """Ensure a signal is dispatched with the event details"""

        with override_settings(DEBUG=True):
            with self.assertRaises(Exception):
                self.client.post(
                    reverse("something", args=["whatever"]),
                    data="{}",
                    content_type="application/json",
                )
        self.assertTrue(mock.called)
        self.assertEqual(mock.call_count, 1)
