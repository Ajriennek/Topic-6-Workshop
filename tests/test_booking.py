import unittest

from booking import can_book


class BookingTests(unittest.TestCase):
    def test_valid_booking(self):
        self.assertTrue(can_book(2, 5))

    def test_minimum_boundary(self):
        self.assertTrue(can_book(1, 5))

    def test_capacity_boundary(self):
        self.assertTrue(can_book(5, 5))

    def test_zero_quantity(self):
        self.assertFalse(can_book(0, 5))

    def test_negative_quantity(self):
        self.assertFalse(can_book(-1, 5))

    def test_excess_quantity(self):
        self.assertFalse(can_book(6, 5))

    def test_empty_capacity(self):
        self.assertFalse(can_book(1, 0))
