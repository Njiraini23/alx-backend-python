#!/usr/bin/env python3
""" takes lists of integers and returns sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''the mixed sum of lists'''
    return sum(mxd_lst)
