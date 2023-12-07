#!/usr/bin/env python3
"""unit test for  utils.access_nested_map"""

from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """testing access_nested_map` function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Testing access_nested_map"""
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """Testing for exceptions"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """class implementing the TestGetJson.test_get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """testing test_get_json"""
        # set the mock response to have return value of test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        # function calls requests.get, need patch to get the mock
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that the mocked method called once per input
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    """Testing the memoize function"""

    def test_memoize(self) -> None:
        """Tests memoize function"""

        class TestClass:
            """ The test class """

            def a_method(self):
                """ method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns the memoize property """
                return self.a_method()

    with patch.object(TestClass, "a_method", return_value=42) as patched:
        test_class = TestClass()
        real_return = test_class.a_property
        real_return = test_class.a_property

        self.assertEqual(real_return, 42)
        patched.assert_called_once()
