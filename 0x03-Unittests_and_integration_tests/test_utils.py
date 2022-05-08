#!/usr/bin/env python3
"""unittest for utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


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

class TestGetJson(unittest.TestCase):
    """ Test for get and get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: dict):
        """ test utils.get_json """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """ test with memoize """
    def test_memoize(self):
        """ Ttest assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock.assert_called_once
