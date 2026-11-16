import unittest

from cancellation import cancel_places


class CancellationTests(unittest.TestCase):
    def test_partial_cancellation(self):
        self.assertEqual(cancel_places(5, 2), 3)

    def test_minimum_cancellation(self):
        self.assertEqual(cancel_places(5, 1), 4)

    def test_full_cancellation(self):
        self.assertEqual(cancel_places(5, 5), 0)
