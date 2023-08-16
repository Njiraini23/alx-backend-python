#!/usr/bin/env pyhon3
"""Typing an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''a function that iterates through list length'''
    return [(i, len(i)) for i in lst]
