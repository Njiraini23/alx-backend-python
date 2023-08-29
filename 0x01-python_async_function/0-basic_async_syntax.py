#!/usr/bin/env python3
"""takes an integer argument with default value of 10"""
async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
