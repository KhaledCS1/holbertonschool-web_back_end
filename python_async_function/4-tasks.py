#!/usr/bin/env python3
"""
Runs task_wait_random n times concurrently with a given max_delay,
and returns the list of delays in ascending order.

Args:
    n (int): Number of tasks to run.
    max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

Returns:
    List[float]: List of delays in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns n task_wait_random coroutines concurrently and
    returns their delays sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
