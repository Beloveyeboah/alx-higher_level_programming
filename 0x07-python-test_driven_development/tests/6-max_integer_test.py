#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer"""
    def test_max_integer(self):
        """Test case for ideal list"""
        testing_list = [1, 3, 2, 4]
        self.assertEqual(max_integer(testing_list), 4)

    def test_empty_list(self):
        """Test case for empty list"""
        testing_list = []
        self.assertEqual(max_integer(testing_list), None)

    def test_none_list(self):
        """Test case for none list"""
        self.assertEqual(None, None)

    def test_floats_list(self):
        """Test case for list of floats"""
        testing_list = [5.2, 2.5, 14.1]
        self.assertEqual(max_integer(testing_list), 14.1)

    def test_negatives_values(self):
        """Test case for list with negative values"""
        testing_list = [2, -5, 12, 0]
        self.assertEqual(max_integer(testing_list), 12)

    def test_too_large_values(self):
        """Test case for really large values"""
        testing_list = [200, 1000, 500000000000000000000]
        self.assertEqual(max_integer(testing_list), 500000000000000000000)

    def test_small_values(self):
        """Test case for small values"""
        testing_list = [0.000009, 0.1, 0.007, 0.002]
        self.assertEqual(max_integer(testing_list), 0.1)
