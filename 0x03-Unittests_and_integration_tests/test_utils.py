#!/usr/bin/env python3
"""unittest for utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class test nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_value):
        '''test nested_map function'''
        self.assertEqual(access_nested_map(map, path), expected_value)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self,nested_map, path, right_output):
        """raises correct exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(repr(e.exception), repr(right_output))
