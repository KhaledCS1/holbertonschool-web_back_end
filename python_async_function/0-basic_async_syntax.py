#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay between 0 and max_delay
seconds, then returns the actual delay.

Args:
    max_delay (int): Maximum delay in seconds. Defaults to 10.

Returns:
    float: The actual delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay up to max_delay seconds and returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
