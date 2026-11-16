import unittest

from amendment import amend_places


class AmendmentTests(unittest.TestCase):
    def test_reduction(self):
        self.assertEqual(amend_places(5, 2, 3), 2)

    def test_increase(self):
        self.assertEqual(amend_places(5, 7, 3), 7)

    # Add independent test methods for the boundaries and invalid requests.
