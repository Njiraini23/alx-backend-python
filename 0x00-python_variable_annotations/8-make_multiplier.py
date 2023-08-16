#!/usr/bin/env python3
"""complex function types"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Annotated function that takes a float and returns a function"""
    return lambda x: x * multiplier
