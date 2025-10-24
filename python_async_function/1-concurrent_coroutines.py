#!/usr/bin/env python3
"""
Asynchronous routine that spawns wait_random n times with a given max_delay.

Each coroutine runs concurrently and returns its delay. The function returns
a list of all the delays in ascending order (without using sort()).

Args:
    n (int): Number of coroutines to spawn.
    max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

Returns:
    List[float]: List of delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns n coroutines of wait_random and collects their results
    in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
  
