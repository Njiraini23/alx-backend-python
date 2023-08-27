#!/usr/bin/env pyhon3
""" async comprehension that takes no arguments"""
import asyncio
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers and return 10 numbers"""
    return [i async for i in async_generator()]
