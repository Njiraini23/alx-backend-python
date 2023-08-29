#!/usr/bin/env python3
"""Executing multiple coroutines"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes 2 int arguments"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
