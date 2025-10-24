#!/usr/bin/env python3
"""Run time for four parallel comprehensions."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension 4 times concurrently and measure total runtime.

    Returns:
        float: The total elapsed time in seconds.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
