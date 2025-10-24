#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.

The coroutine loops 10 times, waiting 1 second between each iteration,
then yields a random float value.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yields a random float between 0 and 10 every second, 10 times.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
