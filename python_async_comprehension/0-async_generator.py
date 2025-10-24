#!/usr/bin/env python3
"""
Measure the runtime of executing async_comprehension four times in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures total runtime for four parallel async_comprehension calls."""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    total_time = time.time() - start_time
    return total_time
