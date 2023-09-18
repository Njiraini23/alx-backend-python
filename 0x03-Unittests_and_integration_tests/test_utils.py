#!/usr/bin/env python3
"""Unit test for utils.access_nested_map"""
import unnittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import acccess_nested_map, get_json
from unittetest.mock import patch, Mock


class TestAccessNestedMap(unnittest.TestCase):
    """TestAccessNestedMap class that inherits"""
    @parameterized.expand([
        ("a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(
            self,
            nested_map
            path:
            expected_result: Union[Dict, int],
            ) -> None:
        """The tests for access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception_msg: Exception,
            ) -> None:
        """Tests for all exceptions"""
        with self.assertRaise(exception_msg):
            access_nested_map(nested_map, path)
