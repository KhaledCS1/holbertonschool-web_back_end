#!/usr/bin/env python3
"""
Measures the average execution time per coroutine for wait_n.

Args:
    n (int): Number of coroutines to run.
    max_delay (int): Maximum delay in seconds.

Returns:
    float: Average time per coroutine.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
