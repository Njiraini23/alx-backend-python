#!/usr/bin/env python3
"""Complex types of strings and int to tuples"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes a string and returns k and square of v'''
    return (k, v**2)
