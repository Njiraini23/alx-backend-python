#!/usr/bin/env python3
"""measures total execution time"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines.py').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """measures execution time for wait_n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time_per_operation = total_time / n
    return average_time_per_operation
