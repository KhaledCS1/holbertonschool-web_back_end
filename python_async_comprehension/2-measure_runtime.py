#!/usr/bin/env python3
"""
Executes async_comprehension four times in parallel and measures total runtime.

The coroutine runs async_comprehension concurrently using asyncio.gather,
then returns the total execution time.

Note:
    The total runtime is roughly 10 seconds, not 40, because all four
    async_comprehension calls run concurrently.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total elapsed time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    total_time = time.time() - start_time
    return total_time
